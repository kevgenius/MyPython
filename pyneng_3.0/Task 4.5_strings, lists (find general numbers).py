"""Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2.
Результатом должен быть список: ['1', '3', '8']"""

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

#Solution:
numbers_vlans1 = (command1.split())[-1]
numbers_vlans1 = (command2.split())[-1]

numbers_vlans1 = (numbers_vlans1).split(",")
numbers_vlans2 = (numbers_vlans2).split(",")

numbers_vlans1 = set(numbers_vlans1)
numbers_vlans2 = set(numbers_vlans2)
numbers_vlans = numbers_vlan_command1.intersection(numbers_vlan_command2)

result = sorted(list(numbers_vlan))
print(result)
