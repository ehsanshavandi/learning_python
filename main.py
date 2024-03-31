from person.student import Student
from statistics.randomize import Randomize

if __name__ == "__main__":
    ehsan = Student("Ehsan", "Arash street", "CE", "Computer")
    Student.sort("Ehsan")
    print(ehsan)
    print(type(ehsan))
    Randomize.z_test_random_int(0.003)
