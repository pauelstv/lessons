#строковые методы
pi = 3.15
print (str(pi))

"""Методы, которые используют точечную нотацию работают только со строками.
С другой стороны, Len () и Str () может работать и на других типах данных.
"""
ministry = "The Ministry of Silly Walks"
print (len(ministry))
print (ministry.upper())

#конкатенация строк
print ("Spam " + "and " + "eggs")
#объединение строки с чем-то что не является строкой
print ("The value of pi is around " + str(3.14))
#форматирование строк. Если вы хотите напечатать переменную со строкой, есть лучший способ, чем конкатенация строк вместе.
name = "Mike"
print ("Hello %s" % (name))
string_1 = "Camelot"
string_2 = "place"
print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
#форматирование строк
name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))
