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
conn1.request("GET", "/")
result = conn1.getresponse()
print(result.read().decode("cp1251"))
conn1.close()



