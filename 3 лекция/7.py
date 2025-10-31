"""Заменить все отрицательные числа Из списка заменить все элементы меньше нуля на 0"""
l = list()
l1 = list()
for s in l:
    if s < 0:
        l1.append(0)
    else:
        l1.append(s)
print(l1)