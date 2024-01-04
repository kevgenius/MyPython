"""
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
• „unicast“ - если первый байт в диапазоне 1-223
• „multicast“ - если первый байт в диапазоне 224-239
• „local broadcast“ - если IP-адрес равен 255.255.255.255
• „unassigned“ - если IP-адрес равен 0.0.0.0
• „unused“ - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

#Решение:
ip_address = input("Enter ip address: \n")
bytes_list = ip_address.split(".")

for byte in bytes_list:
    if int(byte) in range(0, 256) and len(bytes_list) == 4 and byte.isdigit():
        if int(bytes_list[0]) in range(224) and ip_address != "0.0.0.0":
            print("unicast")
        elif int(bytes_list[0]) in range(224, 240):
            print("multicast")
        elif ip_address == "255.255.255.255":
            print("local broadcast")
        elif ip_address == "0.0.0.0":
            print("unassigned")
        else:
            print("unused")
        break
    else:
        print("Bad address!")
        break
