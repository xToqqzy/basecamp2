from datetime import datetime
from math import ceil
import sqlite3
import os
import sys
import csv


class ParkedCar:
    def __init__(self, id=None, license_plate=None, check_in=None, check_out=None, parking_fee=0.0):
        self.id = id
        self.license_plate = license_plate
        self.check_in = datetime.strptime(
            check_in, "%m-%d-%Y %H:%M:%S") if isinstance(check_in, str) else check_in
        self.check_out = datetime.strptime(
            check_out, "%m-%d-%Y %H:%M:%S") if isinstance(check_out, str) and check_out else None
        self.parking_fee = float(parking_fee)


class CarParkingMachine:
    def __init__(self, id="North", capacity=10, hourly_rate=2.50):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}  # memory only
        self.db_conn = sqlite3.connect(
            os.path.join(sys.path[0], 'carparkingmachine.db'))
        self.db_conn.execute(
            '''CREATE TABLE IF NOT EXISTS parkings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_parking_machine TEXT NOT NULL,
                license_plate TEXT NOT NULL,
                check_in TEXT NOT NULL,
                check_out TEXT DEFAULT NULL,
                parking_fee NUMERIC DEFAULT 0 
            );'''
        )
        self.load_state_from_db()

    def load_state_from_db(self):
        self.parked_cars.clear()
        cursor = self.db_conn.cursor()
        cursor.execute('''
            SELECT id, license_plate, check_in FROM parkings 
            WHERE car_parking_machine = ? AND check_out IS NULL
        ''', (self.id,))
        for row in cursor.fetchall():
            car = ParkedCar(id=row[0], license_plate=row[1], check_in=datetime.strptime(
                row[2], "%m-%d-%Y %H:%M:%S"))
            self.parked_cars[car.license_plate] = car

    def find_by_id(self, id) -> ParkedCar:
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT * FROM parkings WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return ParkedCar(id=row[0], license_plate=row[2], check_in=row[3], check_out=row[4], parking_fee=row[5])
        return None

    def find_last_checkin(self, license_plate) -> int:
        cursor = self.db_conn.cursor()
        cursor.execute('''
            SELECT id FROM parkings 
            WHERE license_plate = ? AND check_out IS NULL 
            ORDER BY check_in DESC LIMIT 1
        ''', (license_plate,))
        row = cursor.fetchone()
        return row[0] if row else None

    def insert(self, parked_car: ParkedCar) -> ParkedCar:
        check_in_str = parked_car.check_in.strftime("%m-%d-%Y %H:%M:%S")
        cursor = self.db_conn.cursor()
        cursor.execute('''
            INSERT INTO parkings (car_parking_machine, license_plate, check_in)
            VALUES (?, ?, ?)
        ''', (self.id, parked_car.license_plate, check_in_str))
        self.db_conn.commit()
        parked_car.id = cursor.lastrowid
        return parked_car

    def update(self, parked_car: ParkedCar) -> None:
        check_out_str = parked_car.check_out.strftime(
            "%m-%d-%Y %H:%M:%S") if parked_car.check_out else None
        cursor = self.db_conn.cursor()
        cursor.execute('''
            UPDATE parkings 
            SET check_out = ?, parking_fee = ?
            WHERE id = ?
        ''', (check_out_str, parked_car.parking_fee, parked_car.id))
        self.db_conn.commit()

    def check_in(self, license_plate, check_in_time=None):
        if len(self.parked_cars) >= self.capacity:
            return False
        if license_plate in self.parked_cars:
            return False

        if check_in_time is None:
            check_in_time = datetime.now()

        parked_car = ParkedCar(
            license_plate=license_plate, check_in=check_in_time)
        parked_car = self.insert(parked_car)
        self.parked_cars[license_plate] = parked_car
        return True

    def check_out(self, license_plate):
        if license_plate not in self.parked_cars:
            return None

        parked_car = self.parked_cars[license_plate]
        now = datetime.now()
        duration = now - parked_car.check_in
        hours = ceil(duration.total_seconds() / 3600)
        fee = self.hourly_rate * min(hours, 24)

        parked_car.check_out = now
        parked_car.parking_fee = fee
        self.update(parked_car)

        del self.parked_cars[license_plate]
        return fee

    # Reporting methods
    def report_parked_cars(self, start_date, end_date):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            SELECT license_plate, check_in, check_out, parking_fee 
            FROM parkings 
            WHERE car_parking_machine = ? 
              AND check_in >= ? 
              AND check_in <= ?
        ''', (self.id, start_date, end_date))
        rows = cursor.fetchall()

        filename = f"parkedcars_{self.id}_from_{start_date.replace('-', '')}_to_{end_date.replace('-', '')}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['license_plate', 'checked_in',
                            'checked_out', 'parking_fee'])
            for r in rows:
                writer.writerow([r[0], r[1], r[2] if r[2] else "", r[3]])
        print(f"Report saved to {filename}")

    def report_total_fee(self, start_date, end_date):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            SELECT car_parking_machine, SUM(parking_fee)
            FROM parkings
            WHERE check_in >= ? AND check_in <= ?
            GROUP BY car_parking_machine
        ''', (start_date, end_date))
        rows = cursor.fetchall()

        filename = f"totalfee_from_{start_date.replace('-', '')}_to_{end_date.replace('-', '')}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['car_parking_machine', 'total_parking_fee'])
            for r in rows:
                writer.writerow([r[0], r[1]])
        print(f"Report saved to {filename}")

    def report_complete_parkings_for_car(self, license_plate):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            SELECT car_parking_machine, check_in, check_out, parking_fee 
            FROM parkings 
            WHERE license_plate = ? AND check_out IS NOT NULL
        ''', (license_plate,))
        rows = cursor.fetchall()

        filename = f"all_parkings_for_{license_plate}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['car_parking_machine', 'check_in',
                            'check_out', 'parking_fee'])
            for r in rows:
                writer.writerow(r)
        print(f"Report saved to {filename}")


if __name__ == "__main__":
    machine = CarParkingMachine()

    while True:
        print(
            "[P] Report all parked cars during a parking period for a specific parking machine")
        print("[F] Report total collected parking fee during a parking period for all parking machines")
        print(
            "[C] Report all complete parkings over all parking machines for a specific car")
        print("[Q] Quit program")

        user_command = input("What's your choice: ").strip().upper()

        if user_command == 'Q':
            break
        elif user_command == 'P':
            start = input("Start date (YYYY-MM-DD): ").strip()
            end = input("End date (YYYY-MM-DD): ").strip()
            machine.report_parked_cars(start, end)
        elif user_command == 'F':
            start = input("Start date (YYYY-MM-DD): ").strip()
            end = input("End date (YYYY-MM-DD): ").strip()
            machine.report_total_fee(start, end)
        elif user_command == 'C':
            plate = input("License plate: ").strip()
            machine.report_complete_parkings_for_car(plate)
        elif user_command == 'I':
            plate = input("License plate: ").strip()
            result = machine.check_in(plate)
            if result[0]:
                print(f"Checked in at {result[1]}")
            else:
                print("Check-in failed (duplicate or full).")
        elif user_command == 'O':
            plate = input("License plate: ").strip()
            fee = machine.check_out(plate)
            if fee is not None:
                print(f"Parking fee: €{fee:.2f}")
            else:
                print("Car not found.")
        else:
            print("Invalid choice.")
