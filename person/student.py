import random
from person.person import Person


class Student(Person):

    def __init__(self, name, house, major, department):

        super().__init__(name, house)
        self.major = major
        self.department = department

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        self._major = major

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    def __str__(self):
        return f"name: {self.name}, house: {self.house}, major: {self.major}  department: {self.department}"
