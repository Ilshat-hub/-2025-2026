'''Поменять местами min и max В списке поменять местами минимальный и максимальный элементы.'''
l = list(range(5))
mx = 0
mn = 0
for n in l:
    if n > mx:
        mx = n
    if n < mn:
        mn = n
mni = l.index(mn)
mxi = l.index(mx)
l.remove(mxi)
l.remove(mni)
l.insert(mni, mx)
l.insert(mxi, mn)

print(l)
