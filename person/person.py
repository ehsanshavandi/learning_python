import random


class Person:
    """Class's variables"""

    rooms = ["Gryffindor", "Hufflepuff", "Ravenclaw"]

    def __init__(self, name, house):
        """Go through the setters"""
        """Instance's variables"""
        # This is a convention: To have difference between name and name function we need to use _name
        self.name = name
        self.house = house

    @property
    def name(self):
        """dot operator without assignment"""
        return self._name

    @name.setter
    def name(self, name):
        """dot operator without assignment"""
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        self._house = house

    def __str__(self):
        return f"{self.name}, {self.house}"

    @classmethod
    def sort(cls, name):
        """Always first argument of classmethod is the own class who called method"""
        print(name, "is in", random.choice(cls.rooms))
