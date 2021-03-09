# - *- coding: utf- 8 - *-

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        """추상 메소드 start: 교통 수단의 주행을 시작한다"""
        pass

    @property
    @abstractmethod
    def speed(self):
        """변수 _speed(교통 수단의 속도)에 대한 추상 getter 메소드"""
        pass


    def stop(self):
        """일반 메소드 stop: 교통 수단의 속도를 0으로 바꾼다"""
        self.speed = 0


class Bicycle(Vehicle):
    max_speed = 15

    def __init__(self, speed):
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_value):
        self.__speed = new_value if 0 <= new_value <= Bicycle.max_speed else 0

    def start(self):
        print ("Start the bicycle.")
        self.speed = Bicycle.max_speed / 3

    def __str__(self):
        return "The bicyle is running at {}km/h".format(self.speed)

class NormalCar(Vehicle):

    def __init__(self, speed, max_speed):
        self.__speed = speed
        self.max_speed = max_speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_value):
        self.__speed = new_value if 0<= new_value <= self.max_speed else 0

    def start(self):
        print ("A normal car starts")
        self.speed = self.max_speed / 2

    def __str__(self):
        return "The normal car is running at {}km/h.".format(self.speed)


class SportsCar(Vehicle):

    def __init__(self, speed, max_speed):
        self.__speed = speed
        self.max_speed = max_speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_value):
        self.__speed = new_value if 0 <= new_value <= self.max_speed else 0

    def start(self):
        print ("The sports car starts")
        self.speed = self.max_speed

    def __str__(self):
        return "The sports car is running at {}km/h.".format(self.speed)

# 자전거 인스턴스
bicycle = Bicycle(0)

# 일반 자동차 인스턴스
car = NormalCar(0, 100)

# 스포츠카 인스턴스
sports_car = SportsCar(0, 200)

# 정의한 인스턴스들을 모두 주행 시작시킨다
bicycle.start()
car.start()
sports_car.start()


# 자전거의 속도를 출력한다
print(bicycle)

# 자전거만 주행을 멈춰준다
bicycle.stop()

# 결과 값을 출력한다
print(bicycle)
print(car)
print(sports_car)

# print(Vehicle.mro())
# print(dir(Vehicle))
