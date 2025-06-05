from datetime import datetime, timedelta
from math import ceil


class ParkedCar:
    def __init__(self, license_plate, check_in=None):
        self.license_plate = license_plate
        self.check_in = check_in or datetime.now()

# nieuwe class om te loggen


class CarParkingLogger:
    def __init__(self, machine_id, log_file_path="carparklog.txt"):
        self.machine_id = machine_id
        self.log_file_path = log_file_path

    def log_event(self, license_plate, action, fee=None):
        now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        # de volgorde die ze wilde
        log_line = f"{now};cpm_name={self.machine_id};license_plate={license_plate};action={action}"
        if fee is not None:
            log_line += f";parking_fee={int(fee)}"
            # hier open je de folder en stuur je de nieuwe logs naar je txt
        with open(self.log_file_path, "a") as f:
            f.write(log_line + "\n")


class CarParkingMachine:
    def __init__(self, id="North", capacity=10, hourly_rate=2.50, log_file_path="carparklog.txt"):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = float(hourly_rate)
        self.parked_cars = {}
        self.logger = CarParkingLogger(self.id, log_file_path)

    def check_in(self, license_plate, check_in_time=None):
        if len(self.parked_cars) >= self.capacity:
            return False
        if license_plate in self.parked_cars:
            return False
        self.parked_cars[license_plate] = ParkedCar(
            license_plate, check_in_time)
        # dit is de nieuwe functie logger om te loggen
        self.logger.log_event(license_plate, "check-in")
        return True

    def check_out(self, license_plate):
        if license_plate not in self.parked_cars:
            return None
        fee = self.get_parking_fee(license_plate)
        self.logger.log_event(license_plate, "check-out", fee)
        del self.parked_cars[license_plate]
        return fee

    def get_parking_fee(self, license_plate):
        parked_car = self.parked_cars[license_plate]
        duration = datetime.now() - parked_car.check_in
        hours = ceil(duration.total_seconds() / 3600)
        fee = self.hourly_rate * min(hours, 24)
        return fee


if __name__ == "__main__":
    machine = CarParkingMachine()

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
                print('Cannot register (maybe already parked or full)')
        elif user_command == "O":
            plate = input("Enter license plate: ").strip()
            fee = machine.check_out(plate)
            if fee is not None:
                print(f'Parking Fee: {fee:.2f} EUR')
            else:
                print('License plate not found')
        else:
            print("Invalid choice.")
