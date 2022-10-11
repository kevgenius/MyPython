"""Обработать строку nat таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.
Ограничение: Все задания надо выполнять используя только пройденные темы."""
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

#Solution:
NAT = NAT.replace("FastEthernet", "GigabitEthernet")
print(NAT)
