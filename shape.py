from math import sqrt
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self)->float:
        pass


class Paint:
    def __init__(self):
        self.shapes = []


    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print ("Cannot add when it is not a shape.")

    def total_area_of_shapes(self):
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        return sum([shape.perimeter() for shape in self.shapes ])


class RightTriangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height /2

    def perimeter(self) -> float:
        return sqrt(self.width**2 + self.height**2 ) + self.width + self.height


class Human():
    def __init__(self):
        pass



right_triangle1 = RightTriangle(3,4)
right_triangle2 = RightTriangle(5,12)
right_triangle3 = RightTriangle(6,8)

human = Human()

paint_program=Paint()

paint_program.add_shape(right_triangle1)
paint_program.add_shape(right_triangle2)
paint_program.add_shape(right_triangle3)
paint_program.add_shape(human)


print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())


