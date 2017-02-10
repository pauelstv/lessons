from pysnmp.entity.rfc3413.oneliner import cmdgen

def getOID(targetIPaddr,value):
    """ имаем ip, oid: возвращается значение oid"""
    community='public'

    generator = cmdgen.CommandGenerator()
    comm_data = cmdgen.CommunityData('server', community, 1) # 1 means version SNMP v2c
    transport = cmdgen.UdpTransportTarget((targetIPaddr, 161))

    real_fun = getattr(generator, 'getCmd')
    res = (errorIndication, errorStatus, errorIndex, varBinds)\
        = real_fun(comm_data, transport, value)

    try:
        #if not errorIndication is None  or errorStatus is True:
        #    print("Error: %s %s %s %s" % res)
            myvarlist = ['Host not respond...']
    except:
        #else:
            # print("%s" % varBinds[0])
            # print("Not parsed string", varBinds[0])
            myvar = str(varBinds[0])
            myvarlist = myvar.split('= ')
            # print("Eeeeerrroookkkk value -> ", myvarlist[1])
    print("indexes in list ->", myvarlist[0])
    oidValue = int(myvarlist[1])
    return oidValue

def getLevels(targetIPaddr):
    value1911=(1,3,6,1,2,1,43,11,1,1,9,1,1)
    value1811=(1,3,6,1,2,1,43,11,1,1,8,1,1)
    snmpint1911 = getOID(targetIPaddr,value1911)
    snmpint1811 = getOID(targetIPaddr, value1811)
    CurrentTonerLevel = 100 * (snmpint1911/snmpint1811)

    return CurrentTonerLevel
targetGroup = ['172.16.0.225', '172.16.0.226', '172.16.0.227', '172.16.0.228',
               '172.16.0.229', '172.16.0.230', '172.16.0.231', '172.16.0.232',
               '172.16.0.233', '172.16.0.234', '172.16.0.235', '172.16.0.236',
               '172.16.0.237', '172.16.0.238', '172.16.0.239']
for indexValue, valueFrormList in enumerate(targetGroup):
    print("Current toner Level is:", getLevels(targetGroup[indexValue]))





















