from abc import ABC, abstractmethod

class Vehicle(ABC):

    # 코드를 쓰세요
    def __init__(self, speed):
        self._speed = speed

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0


    @abstractmethod
    def __str__(self):
        pass

#자전거
class Bicycle(Vehicle):
    max_speed = 15

    def __init__(self, speed):
        super().__init__(speed)


    def start(self):
        self.speed = self.max_speed / 3
        print ("A bicycle starts!!")

    def __str__(self):
        return "The bicycle runs {}km/h".format(self.speed)


# 일반 자동차
class  NormalCar(Vehicle):
    def __init__(self, speed, max_speed):
        super().__init__(speed)
        self.max_speed = max_speed


    def start(self):
        self.speed = self.max_speed /2
        print ("A car starts!!")


    def __str__(self):
        return "The car runs {}km/h".format(self.speed)

# 스포츠카
class SportsCar(Vehicle):
    def __init__(self,speed, max_speed):
        super().__init__(speed)
        self.max_speed = max_speed


    def start(self):
        self.speed = self.max_speed
        print ("A sports car starts!!")

    def __str__(self):
        return "The sports car runs {}km/h".format(self.speed)

class DrivingSimulator():

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle,Vehicle):
            self.vehicles.append(vehicle)
        else:
            print("{} is not a vehicle".format(vehicle))

    def start_all_vehicles(self):
        print("Start all vehicles.")
        for vehicle in self.vehicles:
            vehicle.start()

    def stop_all_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.stop()
        print("Stop all vehicles.")

    def __str__(self):
        result_str = ""
        for vehicle in self.vehicles:
            result_str += str(vehicle) + "\n"
        return result_str


bicycle = Bicycle(0)
car1 = NormalCar(0, 100)
car2 = NormalCar(0, 120)
sports_car1 = SportsCar(0, 200)
sports_car2 = SportsCar(0, 190)

driving_simulator = DrivingSimulator()

driving_simulator.add_vehicle(bicycle)
driving_simulator.add_vehicle(car1)
driving_simulator.add_vehicle(car2)
driving_simulator.add_vehicle(sports_car1)
driving_simulator.add_vehicle(sports_car2)
driving_simulator.add_vehicle(1)

driving_simulator.start_all_vehicles()
print(driving_simulator)

driving_simulator.stop_all_vehicles()
print(driving_simulator)