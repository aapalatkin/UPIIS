class Student:
    def __init__(self, first_name, last_name, birth_date, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades  # List of tuples (subject, exam_date, teacher_name, grade)

students = [
    Student("Иван", "Иванов", "2000-01-15", [
        ("Математика", "2023-05-20", "Петров А.В.", 5),
        ("Физика", "2023-06-15", "Сидоров В.В.", 4),
        ("Химия", "2023-07-01", "Кузнецов Н.Н.", 5)
    ]),
    Student("Петр", "Петров", "1999-03-22", [
        ("Математика", "2023-05-20", "Петров А.В.", 4),
        ("Физика", "2023-06-15", "Сидоров В.В.", 3),
        ("Химия", "2023-07-01", "Кузнецов Н.Н.", 4)
    ]),
    Student("Мария", "Сидорова", "2001-08-30", [
        ("Математика", "2023-05-20", "Петров А.В.", 5),
        ("Физика", "2023-06-15", "Сидоров В.В.", 5),
        ("Химия", "2023-07-01", "Кузнецов Н.Н.", 5)
    ])
]

def best_student(students):
    best_avg = 0
    best_student = None

    for student in students:
        total = sum(grade for subject, exam_date, teacher, grade in student.grades)
        avg = total / len(student.grades)

        if avg > best_avg:
            best_avg = avg
            best_student = student

    return best_student

best = best_student(students)

print(f"Лучший студент: {best.first_name} {best.last_name}")
for subject, exam_date, teacher, grade in best.grades:
    print(f"Предмет: {subject}, Оценка: {grade}")
