import sqlite3
import csv
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'carparkingmachine.db')


def report_parked_cars(machine_id, start_date, end_date):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT license_plate, check_in, check_out, parking_fee
        FROM parkings
        WHERE car_parking_machine = ?
          AND check_in >= ?
          AND check_in <= ?
    ''', (machine_id, start_date, end_date))
    rows = c.fetchall()
    conn.close()

    filename = f"parkedcars_{machine_id}_{start_date}_to_{end_date}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['license_plate', 'check_in',
                        'check_out', 'parking_fee'])
        writer.writerows(rows)
    print(f"Report saved to {filename}")


def report_total_fee(start_date, end_date):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT car_parking_machine, SUM(parking_fee)
        FROM parkings
        WHERE check_in >= ? AND check_in <= ?
        GROUP BY car_parking_machine
    ''', (start_date, end_date))
    rows = c.fetchall()
    conn.close()

    filename = f"totalfee_{start_date}_to_{end_date}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['car_parking_machine', 'total_fee'])
        writer.writerows(rows)
    print(f"Report saved to {filename}")


def report_complete_parkings_for_car(license_plate):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT car_parking_machine, check_in, check_out, parking_fee
        FROM parkings
        WHERE license_plate = ? AND check_out IS NOT NULL
    ''', (license_plate,))
    rows = c.fetchall()
    conn.close()

    filename = f"complete_parkings_{license_plate}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['car_parking_machine', 'check_in',
                        'check_out', 'parking_fee'])
        writer.writerows(rows)
    print(f"Report saved to {filename}")


def main():
    while True:
        print()
        print(
            "[P] Report all parked cars during a parking period for a specific parking machine")
        print("[F] Report total collected parking fee during a parking period for all parking machines")
        print(
            "[C] Report all complete parkings over all parking machines for a specific car")
        print("[Q] Quit program")
        choice = input("What's your choice: ").strip().upper()

        if choice == 'P':
            line = input().strip()
            parts = [p.strip() for p in line.split(',')]
            if len(parts) != 3:
                print("Invalid input, expected 'machine_id,start_date,end_date'")
                continue
                machine_id, start_date, end_date = parts
                report_parked_cars(machine_id, start_date, end_date)

        if choice == 'F':
            start_date = input("Start date (YYYY-MM-DD): ").strip()
            end_date = input("End date (YYYY-MM-DD): ").strip()
            report_total_fee(start_date, end_date)
        elif choice == 'C':
            license_plate = input("License plate: ").strip()
            report_complete_parkings_for_car(license_plate)
        elif choice == 'Q':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == '__main__':
    main()
