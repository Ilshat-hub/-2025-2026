"""Задание 2: Проверка четности. Создайте функцию is_even(number), которая принимает
целое число и возвращает True, если число четное, и False, если нечетное."""
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(5264375))