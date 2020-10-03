class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_details(self):
        print(f'Firstname: {self.firstname}, Lastname: {self.lastname}')


class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.year = year

    def graduation(self):
        print(f'{self.firstname} {self.lastname} is graduated in the year {self.year}')


if __name__ == "__main__":
    s = Student('John', 'Smith', 2016)
    s.print_details()
    s.graduation()
