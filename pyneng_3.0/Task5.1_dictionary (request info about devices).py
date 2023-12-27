"""
В задании создан словарь, с информацией о разных устройствах.
Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1). И вывести ин-
формацию о соответствующем устройстве на стандартный поток вывода (информация будет
в виде словаря).
Ограничение: нельзя изменять словарь london_co.
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

device = input("Enter name of device:\n ")
print(london_co[device])