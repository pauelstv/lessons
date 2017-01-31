title = "azaza kek lol"

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a
b[0] = 4
print("A=", a)
print("B=", b)

s = 'Привет, Python'
print('Длина строки: ', len(s))
print('Тип данных: ', type(s))
print('Первые [8]: ', s[:8])
print('Последние 8: ', s[8:-1])
print('Каждый второй: ', s[::2])
print('Наоборот: ', s[::-1])

for num in a:
    print(a[num])
for num in a:
    print(a[num], end=" ")

