#строковые методы
pi = 3.15
print (str(pi))

"""Методы, которые используют точечную нотацию работают только со строками.
С другой стороны, Len () и Str () может работать и на других типах данных.
"""
ministry = "The Ministry of Silly Walks"
print(len(ministry))
print(ministry.upper())

#конкатенация строк
print("Spam " + "and " + "eggs")
#объединение строки с чем-то что не является строкой
print("The value of pi is around " + str(3.14))
#форматирование строк. Если вы хотите напечатать переменную со строкой, есть лучший способ, чем конкатенация строк вместе.
name = "Mike"
print("Hello %s" % (name))
string_1 = "Camelot"
string_2 = "place"
print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
#форматирование строк
"""name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")
print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))"""

###################### Date and time library
import datetime
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

print("Formatted date:", "%s-%s-%s" % (now.year, now.month, now.day))
print("Formatted time:", "%s:%s:%s" % (now.hour, now.minute, now.second))
print("Formatted datetime string:", "%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second))

#### User inpit IF ELIF ELSE lesson
"""def clinic():
    print("You've just entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print("Of course this is the Argument Room, I've told you that already!")
    else:
        print("You didn't pick left or right! Try again.")
        clinic()
clinic()"""
# Assign True or False as appropriate on the lines below!
# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!
# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True
# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True
# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False
# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False
"""
    Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True
"""
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print(using_control_once())
print(using_control_again())
# Else problems
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return False        # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False        # Make sure this returns False

# immutable типы bytearray, tuple (кортеж)
# создать пустой корреж(tuple)
mytuple = tuple()
#mutable - list
immutable_1 = (1,2,3,4)
mutable_1 = [1,1,3,4]
mutable_1[0] = False
print(mutable_1)
# положить внутрь списка еще один список
mutable_1[0] = [True, True, True]
print(mutable_1)
# доступ к элементам вложенного списка
mutable_1[0][1] = False
print(mutable_1)
#операции над списками: append[добавить в конец] clear copy count extend index insert[вставка по индексу] pop[удаление из конца] remove reverse sort
mutable_1.append(1111)
print(mutable_1)
# добавление в произвольное место списка
mutable_1.insert(4, 2222)
print(mutable_1)
# bytearray - изменяемая последовательность байтов
b = bytearray(b'abc')

