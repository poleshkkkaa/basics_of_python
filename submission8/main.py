# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут

class StudentGrades:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

student = StudentGrades()

n = int(input())

for _ in range(n):
    grade = float(input())
    student.add_grade(grade)

avg = student.average()

print("Середній бал:", round(avg))
