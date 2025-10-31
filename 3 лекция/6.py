""" Подсчет уникальных элементов Посчитать, сколько в списке уникальных элементов."""
l = list()
l1 = list()
for s in l:
    if s not in l1:
        l1.append(s)
print(len(l1))