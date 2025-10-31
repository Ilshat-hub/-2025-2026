# Задание 2: Функция для нахождения среднего значения. Напишите функцию
# average(numbers), которая принимает список чисел и возвращает их среднее
# значение.

def average(nembers):
    return sum(nembers) / len(nembers)
s = []
while True:
    d = input()
    if d == "" or d == ' ' or d == 'exit':
        break
    else:
        s.append(int(d))
print(average(s))