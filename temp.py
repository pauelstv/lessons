import random
for num in range(1):
    if random.random() >= 0.5:
        print("Го куреть11")
    else:
        print("Куреву еще не время!")


lottery = [99, 38, 11, 54, 55, 87]
print("Not sorted: ", lottery)
lottery.sort()
print("Sorted:     ", lottery)
lottery.reverse()
print("Reverse sotred: ", lottery)

participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
print("Requested index: ", participant['country'])
print("Type of data:", type(participant))
participant['favorite_language'] = 'Python'
print(participant)
# -----------------------------------------------------------
girls = ['172.16.0.225', '172.16.0.226', '172.16.0.227', '172.16.0.229', '172.16.0.230']
for name in girls:
    print(name)
for i in range(1, 6):
    print(i)

from pycbrf.toolbox import ExchangeRates

# Запрашиваем данные на 26-е июня.
rates = ExchangeRates('2016-06-26')

rates.date_requested  # 2016-06-26 00:00:00
rates.date_received  # 2016-06-25 00:00:00
# 26-е был выходной, а курс на выходные установлен 25-го
rates.dates_match  # False

# Список всех курсов валют на день доступ в rates.rates.

# Поддерживаются разные идентификаторы валют:
rates['USD'].name  # Доллар США
rates['R01235'].name  # Доллар США
rates['840'].name  # Доллар США
print(rates['USD'].value)














