"""
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
• „unicast“ - если первый байт в диапазоне 1-223
• „multicast“ - если первый байт в диапазоне 224-239
• „local broadcast“ - если IP-адрес равен 255.255.255.255
• „unassigned“ - если IP-адрес равен 0.0.0.0
• „unused“ - во всех остальных случаях

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
• состоит из 4 чисел разделенных точкой,
• каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение: „Неправильный IP-адрес“

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

#Решение:
ip_address = input("Enter ip address: \n")
octets_list = ip_address.split(".")

for octet in octets_list:
    if int(octet) in range(0, 256) and len(octets_list) == 4:
        if int(octets_list[0]) in range(224) and ip_address != "0.0.0.0":
            print("unicast")
        elif int(octets_list[0]) in range(224, 240):
            print("multicast")
        elif ip_address == "255.255.255.255":
            print("local broadcast")
        elif ip_address == "0.0.0.0":
            print("unassigned")
        else:
            print("unused")
        break
    else:
        print("this is error address!")
        ip_address = input("Enter ip address: \n")
        octets_list = ip_address.split(".")
        continue


