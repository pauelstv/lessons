#!/usr/bin/python
__author__ = 'aladex'
import iptools
import httplib
from concurrent.futures import ThreadPoolExecutor

list_net = open('list_of_nets.txt')

rtk_ips = iptools.IpRangeList(*[line.strip() for line in list_net])
list_of_ips = []
check_ips = []
file = open('list_of_ips.txt', "a")
def tester(ip):
    try:
        conn = httplib.HTTPConnection(ip, 1234, timeout=1)
        conn.request('GET','/')
        r1 = conn.getresponse()
        list_of_ips.append(ip)
        counter = 0
        for i in open('list_of_ips.txt'):
            if i.strip() == ip:
                counter = counter + 1

        if counter == 0:
            file = open('list_of_ips.txt','a')
            file.write(ip+'\n')
            file.close()
    except: pass


with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(tester,rtk_ips)

file_ips = open('list_of_ips.txt', 'w')

for line in list_of_ips:
    file_ips = open('list_of_ips.txt','a')
    file_ips.write(line+'\n')
    file_ips.close()
