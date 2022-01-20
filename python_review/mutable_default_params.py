from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):  # this is a bad idea []
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


jose = Student('Jose')
dario = Student('Dario')

jose.take_exam(90)
# dario.take_exam(90)

print(jose.grades)
print(dario.grades)
