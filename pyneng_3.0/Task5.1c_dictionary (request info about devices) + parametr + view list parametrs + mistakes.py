"""
Переделать скрипт из задания 5.1b таким образом, чтобы, при запросе параметра, которого
нет в словаре устройства, отображалось сообщение „Такого параметра нет“.
Если выбран существующий параметр, вывести информацию о соответствующем параметре,
указанного устройства.
"""



london_co = {
'r1': {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'ios': '15.4',
'ip': '10.255.0.1'
},
'r2': {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '4451',
'ios': '15.4',
'ip': '10.255.0.2'
},
'sw1': {
'location': '21 New Globe Walk',
'vendor': 'Cisco',
'model': '3850',
'ios': '3.6.XE',
'ip': '10.255.0.101',
'vlans': '10,20,30',
'routing': True
}
}

#Решение:
device = input("Enter name of device:\n")
parameter = (london_co[device]).keys()
parameter = list(parameter)
parameter = ",".join(parameter)

parameter = input("Enter name parameter" + "(" + parameter + "):\n")
print((london_co[device]).get(parameter, "Такого параметра нет."))

