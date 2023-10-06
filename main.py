import math


class Figure:
    def square(self):
        raise NotImplementedError('Method "square" should be used to subclasses')


class Circle(Figure):
    def __init__(self, radius):

        if radius < 0:
            raise ValueError("Radius should be non-negative number!")

        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):

    def __init__(self, first_side, second_side, third_side):
        if first_side < 0 or second_side < 0 or third_side < 0:
            raise ValueError("Side should be non-negative number!")

        if not (first_side + second_side > third_side
                and first_side + third_side > second_side
                and second_side + third_side > first_side):

            raise ValueError('Triangle does not exist!')

        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def square(self):
        half_meter = (self.first_side + self.second_side + self.third_side) // 2
        return (half_meter * (half_meter - self.first_side) * (half_meter - self.second_side) *
                (half_meter - self.third_side)) ** 0.5

    def is_right(self):
        return self.first_side ** 2 + self.second_side ** 2 == self.third_side ** 2 \
               or self.first_side ** 2 + self.third_side ** 2 == self.second_side ** 2 \
               or self.second_side ** 2 + self.third_side ** 2 == self.first_side ** 2


if __name__ == 'main':
    pass
