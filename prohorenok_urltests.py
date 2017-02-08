from urllib.parse import urlparse

urladdr = urlparse("https://azaza.ru/kekhuypidor/")
# print(urladdr)
# преобразовываем результат в кортеж
url = tuple(urladdr)
print("Proto: ", url[0])
print("Domain: ", url[1])
print("Path: ", url[2])



