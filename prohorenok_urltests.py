# from urllib.parse import urlparse
from urllib.parse import *

urladdr = urlparse("https://what.cd.ru/keys/")
print(urladdr)
print("Object attribute: netloc ->", urladdr.netloc)
# преобразовываем результат в кортеж
url = tuple(urladdr)
# атрибуты объекта доступны по индексам
print("Proto: ", url[0])
print("Domain: ", url[1])
print("Path: ", url[2])
print("URL join:", urljoin("http://zlobatrix.ru/h1/h1/h1/1111test.php", "../../../file.php"))

# ----------------------- HTTP communication ------------------------------------------------
from http.client import HTTPConnection
conn2 = HTTPConnection("ya.ru", 80)
conn3 = HTTPConnection("ya.ru:80")

conn1 = HTTPConnection("ya.ru")
conn1.request("GET", "/")
result = conn1.getresponse()            # создаем объект результата
# print(result.read().decode("utf-8"))  # вывод HTML-кода
urlheaders = result.getheaders()        # возвращаем заголовки в виде списка кортежей
print(urlheaders[0], urlheaders[1])     # доуступно по индексам
urldict = dict(urlheaders)              # преобразуем в словарь {}
print("Server headers:", urldict)
print("Ключи словаря -> ", urldict.keys())
print("Expires -> ", urldict['Expires'])
try:                                    # обработка наличия поля Server в хедере
    print("Server -> ", urldict['Server'])
except:
    print("Server signature not found!")
print("Last-Modified -> ", urldict['Last-Modified'])
print("Cache-Control -> ", urldict['Cache-Control'])
print("Date -> ", urldict['Date'])







conn1.close()



