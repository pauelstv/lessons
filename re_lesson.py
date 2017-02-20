import re
# string_parse = 'azaza kek  azaza'
result = re.match(r'AV', 'AV kek AV')
print(result.group(0))

result = re.findall(r'AV', 'AV azaza AV')
print(result)

pattern = re.compile('AV')
result = pattern.findall('AV Analytics Vidhya AV')
print(result)
result2 = pattern.findall('AV is largest analytics community of India')
print(result2)
"""Оператор	Описание
.	Один любой символ, кроме новой строки \n.
?	0 или 1 вхождение шаблона слева
+	1 и более вхождений шаблона слева
*	0 и более вхождений шаблона слева
\w	Любая цифра или буква (\W — все, кроме буквы или цифры)
\d	Любая цифра [0-9] (\D — все, кроме цифры)
\s	Любой пробельный символ (\S — любой непробельнй символ)
\b	Граница слова
[..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
\	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
^ и $	Начало и конец строки соответственно
{n,m}	От n до m вхождений ({,m} — от 0 до m)
a|b	Соответствует a или b
()	Группирует выражение и возвращает найденный текст
\t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
"""

## любой сомвол .
import re
result = re.findall(r'.', 'AV is largest Analytics community of India')
print(result)
print('Count list symbols: ', len(result))

# удалим пробел из выдачи
result = re.findall(r'\w', 'AV is largest Analytics community of India')
print(result)
print('Count list symbols withot space: ', len(result))

# парсим выделяя каждое слово
result = re.findall(r'\w*', 'AV is largest Analytics community of India')
print(result)

# И снова в результат попали пробелы, так как * означает «ноль или более символов». Для того, чтобы их убрать, используем +:
result = re.findall(r'\w+', 'AV is largest Analytics community of India')
print(result)

#  Теперь вытащим первое слово, используя ^:
result = re.findall(r'^\w+', 'AV is largest Analytics community of India')
print(result)

# Если мы используем $ вместо ^, то мы получим последнее слово, а не первое:
result = re.findall(r'\w+$', 'AV is largest Analytics community of India')
print(result)

# Задача 2: Вернуть первые два символа каждого слова
# Вариант 1: используя \w, вытащить два последовательных символа, кроме пробельных, из каждого слова:
result = re.findall(r'\w\w', 'AV is largest Analytics community of India')
print(result)

# Вариант 2: вытащить два последовательных символа, используя символ границы слова (\b):
result = re.findall(r'\b\w.', 'AV is largest Analytics community of India')
print(result)

# Задача 3: вернуть список доменов из списка адресов электронной почты
# Давайте снова рассмотрим решение пошагово. Сначала вернем все символы после «@»:
result = re.findall(r'@\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)

#  Как видим, части «.com», «.in» и т. д. не попали в результат. Изменим наш код:
result = re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)

# Второй вариант — вытащить только домен, используя группировку — ( ):
result = re.findall(r'@\w+.(\w+)', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)

# Задача 4: Извлечь дату из строки
result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print(result)

#  Для извлечения только года нам опять помогут скобки:
result = re.findall(r'\d{2}-\d{2}-(\d{4})', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print(result)

