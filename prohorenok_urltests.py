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

