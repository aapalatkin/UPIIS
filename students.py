class Student:
    def __init__(self, first_name, last_name, birth_date, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades  # List of tuples (subject, exam_date, teacher_name, grade)

    def average_grade(self):
        return sum(grade for _, _, _, grade in self.grades) / len(self.grades)


students = [
    Student("Иван", "Иванов", "2000-01-15", [
        ("Математика", "2023-05-20", "Петров А.В.", 5),
        ("Физика", "2023-06-15", "Сидоров В.В.", 4),
        ("Химия", "2023-07-01", "Кузнецов Н.Н.", 5),
        ("Информатика", "2023-08-10", "Смирнов В.В.", 5)
    ]),
    Student("Петр", "Петров", "1999-03-22", [
        ("Математика", "2023-05-20", "Петров А.В.", 4),
        ("Физика", "2023-06-15", "Сидоров В.В.", 3),
        ("Химия", "2023-07-01", "Кузнецов Н.Н.", 4),
        ("Биология", "2023-09-10", "Васильев А.А.", 5)
    ]),
    Student("Мария", "Сидорова", "2001-08-30", [
        ("Математика", "2023-05-20", "Петров А.В.", 5),
        ("Физика", "2023-06-15", "Сидоров В.В.", 5),
        ("Химия", "2023-07-01", "Кузнецов Н.Н.", 5),
        ("Информатика", "2023-08-10", "Смирнов В.В.", 5),
        ("Литература", "2023-10-15", "Иванова Е.В.", 5)
    ])
]

def best_student(students):
    best_student = max(students, key=lambda student: student.average_grade())
    return best_student

best = best_student(students)

print(f"Лучший студент: {best.first_name} {best.last_name}, Средний балл: {best.average_grade():.2f}")
print("Оценки по предметам:")
for subject, exam_date, teacher, grade in best.grades:
    print(f"Предмет: {subject}, Оценка: {grade}, Преподаватель: {teacher}")
