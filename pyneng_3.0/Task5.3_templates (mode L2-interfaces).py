"""
Скрипт должен запрашивать у пользователя:
• информацию о режиме интерфейса (access/trunk)
• номере интерфейса (тип и номер, вида Gi0/3)
• номер VLANа (для режима trunk будет вводиться список VLANов)

В зависимости от выбранного режима, на стандартный поток вывода, должна возвращать-
ся соответствующая конфигурация access или trunk (шаблоны команд находятся в списках
access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем
соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Ограничение: Все задания надо выполнять используя только пройденные темы. То есть эту
задачу можно решить без использования условия if и циклов for/while.
Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:
$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): access
Введите тип и номер интерфейса: Fa0/6
Введите номер влан(ов): 3
interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Пример выполнения скрипта, при выборе режима trunk:
$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): trunk
Введите тип и номер интерфейса: Fa0/7
Введите номер влан(ов): 2,3,4,5
interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
"""

access_template = [
'switchport mode access', 'switchport access vlan {}',
'switchport nonegotiate', 'spanning-tree portfast',
'spanning-tree bpduguard enable'
]
trunk_template = [
'switchport trunk encapsulation dot1q', 'switchport mode trunk',
'switchport trunk allowed vlan {}'
]

#Решение:
mode = input("Введите режим работы интерфейса (access/trunk):\n")
type_interface = input("Введите тип и номер интерфейса:\n")
number_vlans = input("Введите номер влан(ов):\n")

access_template = [
'switchport mode access', 'switchport access vlan {}',
'switchport nonegotiate', 'spanning-tree portfast',
'spanning-tree bpduguard enable'
]

arg0_acc = access_template[0]
arg1_acc = access_template[1]
arg2_acc = access_template[2]
arg3_acc = access_template[3]
arg4_acc = access_template[4]

result_access_template = """
interface {0}
{1}
{2}
{3}
{4}
""".format(type_interface, arg0_acc, arg1_acc.format(number_vlans), arg2_acc, arg3_acc, arg4_acc)




trunk_template = [
'switchport trunk encapsulation dot1q', 'switchport mode trunk',
'switchport trunk allowed vlan {}'
]

arg0_trunk = trunk_template[0]
arg1_trunk = trunk_template[1]
arg2_trunk = trunk_template[2]

result_trunk_template = """
interface {0}
{1}
{2}
{3}
""".format(type_interface, arg0_trunk, arg1_trunk, arg2_trunk.format(number_vlans))

dict_templates_interfaces = {"access": result_access_template, "trunk": result_trunk_template}
result = dict_templates_interfaces[mode]
print(result)