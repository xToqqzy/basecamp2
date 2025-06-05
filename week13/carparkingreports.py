import sqlite3
import csv


def report_parked_cars(machine, start_date, end_date):
    conn = sqlite3.connect('carparkingmachine.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT license_plate, check_in, check_out, parking_fee
        FROM parkings
        WHERE car_parking_machine = ?
          AND check_in >= ?
          AND check_in <= ?
          AND check_out IS NOT NULL
        ORDER BY license_plate, check_in
    ''', (machine, start_date, end_date))
    rows = cursor.fetchall()
    filename = f"parkedcars_{machine}_from_{start_date}_to_{end_date}.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow(['license_plate', 'checked_in',
                        'checked_out', 'parking_fee'])
        for row in rows:
            writer.writerow([row[0].upper(), row[1], row[2], row[3]])
    print(f"Report saved to {filename}")
    conn.close()


def report_total_fee(start_date, end_date):
    conn = sqlite3.connect('carparkingmachine.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT SUM(parking_fee)
        FROM parkings
        WHERE check_in >= ?
          AND check_in <= ?
    ''', (start_date, end_date))
    total_fee = cursor.fetchone()[0]
    total_fee = total_fee if total_fee is not None else 0
    filename = f"totalfee_from_{start_date}_to_{end_date}.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['total_parking_fee'])
        writer.writerow([total_fee])
    print(f"Report saved to {filename}")
    conn.close()


def report_complete_parkings(license_plate):
    conn = sqlite3.connect('carparkingmachine.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT car_parking_machine, check_in, check_out, parking_fee
        FROM parkings
        WHERE license_plate = ?
          AND check_out IS NOT NULL
    ''', (license_plate,))
    rows = cursor.fetchall()
    filename = f"completeparkings_{license_plate}.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['parking_machine', 'checked_in',
                        'checked_out', 'parking_fee'])
        for row in rows:
            writer.writerow(row)
    print(f"Report saved to {filename}")
    conn.close()


def main():
    while True:
        print(
            "[P] Report all parked cars during a parking period for a specific parking machine")
        print("[F] Report total collected parking fee during a parking period for all parking machines")
        print(
            "[C] Report all complete parkings over all parking machines for a specific car")
        print("[Q] Quit program")
        choice = input("Your choice: ").strip().upper()
        if choice == 'Q':
            break
        elif choice == 'P':
            data = input(
                "Parking machine ID,Start date (YYYY-MM-DD),End date (YYYY-MM-DD): ").strip()
            machine, start_date, end_date = data.split(',')
            report_parked_cars(machine, start_date, end_date)
        elif choice == 'F':
            data = input(
                "Start date (YYYY-MM-DD),End date (YYYY-MM-DD): ").strip()
            start_date, end_date = data.split(',')
            report_total_fee(start_date, end_date)
        elif choice == 'C':
            license_plate = input("License plate: ").strip()
            report_complete_parkings(license_plate)
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
