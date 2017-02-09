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
conn2 = HTTPConnection("telros-telecom.lan", 80)
conn3 = HTTPConnection("telros-telecom.lan:80")

conn1 = HTTPConnection("telros-telecom.lan")
conn1.request("GET", "/drupal/")
result = conn1.getresponse()
# print(result.read().decode("utf-8"))  # вывод HTML-кода
urlheaders = result.getheaders()
print(urlheaders[0], urlheaders[1])  # доуступно по индексам
urldict = dict(urlheaders)
print("Server headers:", urldict)
print("Ключи словаря -> ", urldict.keys())
print("Content-Type -> ", urldict['Content-Type'])
print("Set-Cookie -> ", urldict['Set-Cookie'])
print("Expires -> ", urldict['Expires'])
print("Server -> ", urldict['Server'])
print("Transfer-Encoding -> ", urldict['Transfer-Encoding'])
print("Last-Modified -> ", urldict['Last-Modified'])
print("ETag -> ", urldict['ETag'])
print("Cache-Control -> ", urldict['Cache-Control'])
print("Date -> ", urldict['Date'])







conn1.close()



