from pysnmp.entity.rfc3413.oneliner import cmdgen


def getOID(value):
    """ имаем ip, возвращается уровень тонера"""

    ip='172.16.0.234'
    community='public'


    generator = cmdgen.CommandGenerator()
    comm_data = cmdgen.CommunityData('server', community, 1) # 1 means version SNMP v2c
    transport = cmdgen.UdpTransportTarget((ip, 161))

    real_fun = getattr(generator, 'getCmd')
    res = (errorIndication, errorStatus, errorIndex, varBinds)\
        = real_fun(comm_data, transport, value)

    if not errorIndication is None  or errorStatus is True:
           print("Error: %s %s %s %s" % res)
    else:
            # print("%s" % varBinds[0])
            # print("Not parsed string", varBinds[0])
            myvar = str(varBinds[0])
            myvarlist = myvar.split('= ')
            print("Eeeeerrroookkkk value -> ", myvarlist[1])

    oid1911 = int(myvarlist[1])
    return oid1911


value1911=(1,3,6,1,2,1,43,11,1,1,9,1,1)
value1811=(1,3,6,1,2,1,43,11,1,1,8,1,1)

getOID(value1911)
getOID(value1811)



















