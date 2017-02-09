__author__ = "pauelstv"
"""from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public', mpModel=0),
           UdpTransportTarget(('172.16.0.235', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
"""

import os, sys
import socket
import random
from struct import pack, unpack
from datetime import datetime as dt

from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto.rfc1902 import Integer, IpAddress, OctetString

ip='172.16.0.234'
community='public'
value=(1,3,6,1,2,1,43,11,1,1,9,1,1)

generator = cmdgen.CommandGenerator()
comm_data = cmdgen.CommunityData('server', community, 1) # 1 means version SNMP v2c
transport = cmdgen.UdpTransportTarget((ip, 161))

real_fun = getattr(generator, 'getCmd')
res = (errorIndication, errorStatus, errorIndex, varBinds)\
    = real_fun(comm_data, transport, value)

if not errorIndication is None  or errorStatus is True:
       print("Error: %s %s %s %s" % res)
else:
       print("%s" % varBinds[0])
myvar = str(varBinds)
print("MyVAR collections:", int(myvar[79:-3]))






