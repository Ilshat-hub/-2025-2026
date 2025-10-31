""" 10. Дана строка "abracadabra".
 • Выведите все символы с чётными индексами.
 • Уберите все буквы "a".
 • Посчитайте, сколько раз встречается буква "b"."""
str = 'abracadabra'
print(str[::2])
print(str.replace('a', ' '))
print(str.count('b'))