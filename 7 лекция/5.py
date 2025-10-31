# Задание 3: Нахождение максимума. Напишите функцию find_max(numbers), которая
# принимает список чисел и возвращает наибольшее число в списке.
def find_max(numbers):
    return max(numbers)
s = []
while True:
    d = input()
    if d == "" or d == ' ' or d == 'exit':
        break
    else:
        s.append(int(d))
print(find_max(s))