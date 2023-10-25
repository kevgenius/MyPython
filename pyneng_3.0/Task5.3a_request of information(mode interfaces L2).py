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

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режи-
ма, задавались разные вопросы в запросе о номере VLANа или списка VLANов:
• для access: „Введите номер VLAN:“
• для trunk: „Введите разрешенные VLANы:“
Ограничение: Все задания надо выполнять используя только пройденные темы. То есть эту
задачу можно решить без использования условия if и циклов for/while.
"""


# Решение:
mode_interface = input("Введите режим работы интерфейса (access/trunk):\n")
typenumber_interface = input("Введите тип и номер интерфейса:\n")
dict_modes_interfaces = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы:"}
vlan = input(dict_modes_interfaces[mode_interface] + "\n")

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

access_template = "\n".join(access_template)
access_template = access_template.format(vlan)

trunk_template = "\n".join(trunk_template)
trunk_template = trunk_template.format(vlan)

dict_results = {"access": access_template, "trunk": trunk_template}
result = dict_results[mode_interface]

print("-"*40)
print("""interface {}""".format(typenumber_interface))
print(result)
print("-"*40)
