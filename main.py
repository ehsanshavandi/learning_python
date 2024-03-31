from person.student import Student

if __name__ == "__main__":
    ehsan = Student("Ehsan", "Arash street", "CE", "Computer")
    Student.sort("Ehsan")
    print(ehsan)
    print(type(ehsan))
