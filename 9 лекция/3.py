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
shkola = {
    "Саша": [3, 4, 5],
    "Мария": [5, 5, 4],
    "Петр": [3, 4, 3]
}
def dop_st():
    name = input('Имя студента ').strip().capitalize()
    if name.capitalize() in shkola:
        print('Такой уже есть...')
    else:
        oc = input('Запишите оценки через запятую ').strip()
        oc_lit = [ocn.strip() for ocn in oc.split(',')]
        new_lst = []
        for item in oc_lit:
            new_lst.append(int(item))
        shkola[name] = new_lst
def dop_ocenka():
    imya = input('Назовите имя студента ').strip().lower()
    if imya.capitalize() not in shkola:
        print('Такого нету')
        return
    else:
        dop_oc = input('Введите оценку(и) через запятую которые, хотите доббавить ')
        dop_oc1 = []
        for o in dop_oc.split(','):
            dop_oc1.append(int(o))
        shkola[imya.capitalize()].extend(dop_oc1)

def vse_st():
    for name, oc in shkola.items():
        if oc:
            grades = sum(oc) / len(oc)
            print(f'{name}: оценки {oc}, средний {grades:.2f}')
        else:
            print('Оценек нету')
def stata():
    slov = {}
    for name, oc in shkola.items():
        if oc:
            grades = sum(oc) / len(oc)
            slov[name] = grades
            print(f'{name}: оценки {oc}, средний {grades:.2f}')
        else:
            print('Оценек нету')
    otl = sum(1 for sl in slov.values() if sl >= 4.5)
    print(f'Всего отличников {otl}!')
    luch = max(slov, key=slov.get)
    huch = min(slov, key=slov.get)
    print(f'Лучший студент это - {luch}!')
    print(f'Худший студент это - {huch}!')

while True:
    print("\n1. Добавить студента")
    print("2. Добавить оценку")
    print("3. Все студенты с оценками")
    print("4. Статистика")
    print("5. Выход")

    vibpr = input('Выберите функцию ')

    if vibpr == '1':
        dop_st()
    elif vibpr == '2':
        dop_ocenka()
    elif vibpr == '3':
        vse_st()
    elif vibpr == '4':
        stata()
    elif vibpr == '5':
        print('До свидания! До новых встреч')
        break
