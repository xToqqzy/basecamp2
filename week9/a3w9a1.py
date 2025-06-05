from datetime import datetime, timedelta
from math import ceil


class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingMachine:
    def __init__(self, capacity=10, hourly_rate=2.50, parked_cars={}):
        self.capacity = capacity
        self.hourly_rate = float(hourly_rate)
        self.parked_cars = parked_cars

    def check_in(self, license_plate, check_in=None):
        if not check_in:
            check_in = datetime.now()
        if len(self.parked_cars) >= self.capacity:
            return False
        if license_plate in self.parked_cars:
            return False
        self.parked_cars[license_plate] = ParkedCar(
            license_plate, check_in)
        return True

    def check_out(self, license_plate):
        if license_plate not in self.parked_cars:
            return

        fee = self.get_parking_fee(license_plate)
        del self.parked_cars[license_plate]
        return fee

    def get_parking_fee(self, license_plate):
        parked_car = self.parked_cars[license_plate]
        check_in_time = parked_car.check_in
        duration = datetime.now() - check_in_time
        hours = ceil(duration.total_seconds() / 3600)
        fee = self.hourly_rate * min(hours, 24)
        return fee


if __name__ == "__main__":
    machine = CarParkingMachine(10, 2.50)

    while True:
        print("\n[I] Check-in car by license plate ")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")
        user_command = input("What's your choice: ").strip().upper()

        if user_command == 'Q':
            break
        elif user_command == "I":
            plate = input("License plate: ").strip()
            success = machine.check_in(plate)
            if success:
                print('License registered')
            else:
                print('Capacity reached')
        elif user_command == "O":
            plate = input("Enter license plate: ").strip()
            fee = machine.check_out(plate)
            print(f'Parking Fee: {fee:.2f}eur')
            break
        else:
            print("Invalid choice.")

    # cpm = CarParkingMachine(capacity=2, hourly_rate=4.0)
    # cpm.check_in("BB-494-H")
    # cpm.check_in("HH-494-B", datetime.now() - timedelta(hours=2))

    # print(cpm.hourly_rate)
    # print(cpm.check_out("BB-494-H"))
