class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        return f"{self.name} is a student at {self.school}."


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 19

    def __repr__(self):
        return f"{self.name} is a working student at {self.school}."


def main():
    anna = WorkingStudent("Anna", "MIT", 12)
    jen = Student("Jen", "Stanford")
    print(jen)
    print(anna)
    anna.grades.append(95)
    anna.grades.append(80)
    print(anna.average_grades())


if __name__ == "__main__":
    main()
