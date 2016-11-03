from abc import ABC, abstractmethod


class MetabolismCommonData(ABC):

    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("age can't be a negative number")
        self._age = age

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight < 0:
            raise ValueError("weight can't be a negative number")
        self._weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("height can't be a negative number")
        self._height = height
