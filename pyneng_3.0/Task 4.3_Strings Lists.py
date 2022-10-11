"""Получить из строки config список VLANов вида: ['1', '3', '10', '20', '30', '100']"""
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

#Solution:
vlan_numbers = (config.split())[-1]  #расчепить по пробелам
result = vlan_numbers.split(",")     #расчепить по запятым
print(result)
