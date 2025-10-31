#1
f = input()
f1 = int(input())
f2 = float(input())
#2
name = input()
age = input()
print('Привет,', name, "!", 'Тебе', age, 'лет.')
#3
s1, s2, s3 = int(input()), int(input()), int(input())
print(s1 + s2 + s3)
#4
v1, v2, v3 = int(input()), int(input()), int(input())
print(max(v1, v2, v3))
#5
s = int(input())
if s % 2 == 0:
    print('Четное')
else:
    print("Нечетное")
#6
number = int(input())
if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
#7
for i in range(1, 11):
    print(i ** 2)
#8
name = input()
length = len(name)
if length >= 3:
    print(length)
else:
    print("Имя слишком короткое!")
#9
numbers = [5, 12, 8, 3, 15]
sum_numbers = sum(numbers)
print(sum_numbers)
#10
num1 = float(input())
num2 = float(input())
if num1 > num2:
    print("1 число больше")
elif num2 > num1:
    print("2 число больше")
#11
i = 1
while i <= 20:
    print(i)
    i += 1
#12
age = int(input())
if age >= 18:
    print("Можно голосовать")
else:
    print("Нельзя голосовать")
#13
while True:
    n = input()
    if n == "exit":
        break
#14
for i in range(25):
    if i % 2 == 0:
        continue
    print(i)
#15
s = 1
for i in range(1, 6):
    s *= i
    print(s)
#16
i = 0
while i <= 100:
    if i % 5 == 0:
        print(i)
    i += 1
#17
numbers = [5, 12, 8, 15, 3, 20, 7, 18]

for num in numbers:
    if num > 10:
        print(num)
#18
s = float(input('Введите 1 число'))
s1 = float(input('Введите 2 число'))
op = input('Введите операцию +, -, *, /')
if op == '+':
    print(s + s1)
elif op == '-':
    print(s - s1)
elif op == '*':
    print(s * s1)
elif op == '/':
    print(s / s1)
else:
    print('Неправильная операция')
#19
numbers = []
s = ' '
while s != '':
    s = input()
    if s != '' and s != ' ':
        numbers.append(int(s))
average = sum(numbers) / len(numbers)
print(average)