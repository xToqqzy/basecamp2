from datetime import datetime
from math import ceil
import json
import os

log_file_path = 'carparklog.txt'


class ParkedCar:
    def __init__(self, license_plate, check_in=None):
        if isinstance(check_in, str):
            check_in = datetime.strptime(check_in, "%m-%d-%Y %H:%M:%S")
        self.license_plate = license_plate
        self.check_in = check_in or datetime.now()


class CarParkingLogger:
    def __init__(self, machine_id, log_file_path):
        self.machine_id = machine_id
        self.log_file_path = log_file_path

    def log_event(self, license_plate, action, fee=None):
        now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        log_line = f"{now};cpm_name={self.machine_id};license_plate={license_plate};action={action}"
        if fee is not None:
            log_line += f";parking_fee={int(fee)}"
        with open(self.log_file_path, "a") as f:
            f.write(log_line + "\n")


class CarParkingMachine:
    def __init__(self, id="North", capacity=10, hourly_rate=2.50, log_file_path=log_file_path):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = float(hourly_rate)
        self.parked_cars = {}
        self.logger = CarParkingLogger(self.id, log_file_path)
        self.filename = id + '_state.json'
        self.load_json()
        # for item in data:
        #     self.parked_cars[item["license_plate"]] = ParkedCar(
        #         item["license_plate"], item["check_in"]
        #     )

    def check_in(self, license_plate, check_in_time=None):
        if len(self.parked_cars) >= self.capacity:
            return False, None
        if license_plate in self.parked_cars:
            return False, None

        if check_in_time is None:
            check_in_time = datetime.now()
        elif isinstance(check_in_time, str):
            check_in_time = datetime.strptime(
                check_in_time, "%m-%d-%Y %H:%M:%S")

        self.parked_cars[license_plate] = ParkedCar(
            license_plate, check_in_time)
        self.logger.log_event(license_plate, "check-in")
        self.store_json()
        return True, check_in_time.strftime("%m-%d-%Y %H:%M:%S")

    def check_out(self, license_plate):
        if license_plate not in self.parked_cars:
            return None
        fee = self.get_parking_fee(license_plate)

        self.logger.log_event(license_plate, "check-out", fee)

        del self.parked_cars[license_plate]
        self.store_json()
        return fee

    def get_parking_fee(self, license_plate):
        parked_car = self.parked_cars[license_plate]
        check_in_time = parked_car.check_in
        duration = datetime.now() - check_in_time
        hours = ceil(duration.total_seconds() / 3600)
        return self.hourly_rate * min(hours, 24)

    def load_json(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for car in data:
                    license = car["license_plate"]
                    check_in = car["check_in"]
                    self.parked_cars[license] = ParkedCar(
                        license, check_in)

    # store json
    # load json

    def store_json(self):
        data = []
        for plate, car in self.parked_cars.items():
            data.append({
                'license_plate': plate,
                'check_in': car.check_in.strftime("%m-%d-%Y %H:%M:%S")

            })

        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    machine = CarParkingMachine()

    while True:
        print("\n[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")
        user_command = input("What's your choice: ").strip().upper()

        if user_command == 'Q':
            break

        elif user_command == "I":
            plate = input("License plate: ").strip()
            check_in_result = machine.check_in(plate)
            if check_in_result:
                # print('License registered')
                print(f'License registered at {check_in_result}')
                # data.append({
                #     "license_plate": plate,
                #     "check_in": check_in_time
                # })
                # with open(self, 'w') as file:
                #     json.dump(data, file, indent=4)
            else:
                print('Cannot register (maybe already parked or full)')

        elif user_command == "O":
            plate = input("Enter license plate: ").strip()
            fee = machine.check_out(plate)

            if fee is not None:
                print(f'Parking Fee: {fee:.2f} EUR')

                # for i, item in enumerate(data):
                #     if item["license_plate"] == plate:
                #         del data[i]
                #         break

                # with open(filename, 'w') as file:
                #     json.dump(data, file, indent=4)
            else:
                print('License plate not found')

        else:
            print("Invalid choice.")
