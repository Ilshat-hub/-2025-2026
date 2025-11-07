"""Задача 3: "Электронный журнал оценок"
Цель: Создать систему учета оценок студентов.
Пошаговые инструкции:
Создай основную структуру:
Словарь, где ключ - имя студента
Значение - список оценок
Реализуй функции:
Добавление студента: имя и начальные оценки
Добавление оценки: выбери студента, добавь оценку
Расчет среднего балла: для каждого студента
Сделай аналитику:
Список студентов с средним баллом
Лучший и худший студент
Количество отличников (средний балл ≥ 4.5)
Система меню:
Добавить студента
Добавить оценку
Показать всех студентов со средними баллами
 •  • Показать статистику"""
students = {
    "иван": [4, 5, 3],
    "мария": [5, 5, 4],
    "петр": [3, 4, 3]
}

while True:
    print("\n1. Добавить студента")
    print("2. Добавить оценку")
    print("3. Все студенты с оценками")
    print("4. Статистика")
    print("5. Выход")

    choice = input("Выберите: ")

    if choice == "1":
        name = input("Имя студента: ").lower()
        if name in students:
            print("Студент уже есть!")
        else:
            students[name] = []
            print(f"Студент {name} добавлен!")

    elif choice == "2":
        name = input("Имя студента: ").lower()
        if name not in students:
            print("Студент не найден!")
        else:
            grade = int(input("Оценка (2-5): "))
            if 2 <= grade <= 5:
                students[name].append(grade)
                print(f"Оценка {grade} добавлена!")
            else:
                print("Оценка должна быть от 2 до 5!")

    elif choice == "3":
        print("\nВсе студенты:")
        for name, grades in students.items():
            if grades:
                avg = sum(grades) / len(grades)
                print(f"- {name}: {grades} (средний: {avg:.1f})")
            else:
                print(f"- {name}: нет оценок")

    elif choice == "4":
        if not students:
            print("Нет студентов!")
            continue

        # Средние баллы
        avg_grades = {}
        for name, grades in students.items():
            if grades:
                avg_grades[name] = sum(grades) / len(grades)

        if avg_grades:
            # Лучший и худший
            best = max(avg_grades, key=avg_grades.get)
            worst = min(avg_grades, key=avg_grades.get)

            # Отличники
            excellent = [name for name, avg in avg_grades.items() if avg >= 4.5]

            print(f"\nСтатистика:")
            print(f"Лучший студент: {best} ({avg_grades[best]:.1f})")
            print(f"Худший студент: {worst} ({avg_grades[worst]:.1f})")
            print(f"Отличников: {len(excellent)}")
            if excellent:
                print(f"Отличники: {', '.join(excellent)}")
        else:
            print("Нет оценок для статистики!")

    elif choice == "5":
        print("До свидания!")
        break

    else:
        print("Неверный выбор")