from person.student import Student
from statistics.randomize import Randomize


def main():
    # ehsan = Student("Ehsan", "Arash street", "CE", "Computer")
    # Student.sort("Ehsan")
    # print(ehsan)
    # print(type(ehsan))
    # Randomize.z_test_random_int(0.003)
    # print(Randomize.own_shuffle([1, 2, 3, 4, 5]))
    Randomize.z_test_own_shuffle()


if __name__ == "__main__":
    main()
