#from urllib.parse import urlparse
from urllib.parse import *


urladdr = urlparse("https://what.cd.ru/keys/")
# print(urladdr)
# преобразовываем результат в кортеж
url = tuple(urladdr)
print("Proto: ", url[0])
print("Domain: ", url[1])
print("Path: ", url[2])




