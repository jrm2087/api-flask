class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student('José D.', (90, 95, 91, 87))
print(student.name)
print(student.grades)
print('AVG:', student.average_grade())

student2 = Student('Annie', (95, 98, 99, 89))
print(student2.name)
print(student2.grades)
print('AVG:', student2.average_grade())
