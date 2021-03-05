# - *- coding: utf- 8 - *-

from math import sqrt
from abc import  ABC, abstractmethod

class Shape(ABC):

    #너비
    @abstractmethod
    def area(self) -> float:
        pass

    #둘레
    @abstractmethod
    def perimeter(self) -> float:
        pass

class RightTriangle(Shape):

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self) -> float:
        return self.base * self.height / 2

    def perimeter(self) -> float:
        return sqrt(self.base**2 + self.height**2) + self.base + self.height



class Paint:

    def __init__(self):
        self.shapes =[]

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("It should be a shape")

    def total_area_of_shapes(self):
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        return sum([shape.perimeter() for shape in self.shapes])



# 테스트 코드
right_triangle_1 = RightTriangle(3, 4)
right_triangle_2 = RightTriangle(5, 12)
right_triangle_3 = RightTriangle(6, 8)

paint_program = Paint()

paint_program.add_shape(right_triangle_1)
paint_program.add_shape(right_triangle_2)
paint_program.add_shape(right_triangle_3)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())

