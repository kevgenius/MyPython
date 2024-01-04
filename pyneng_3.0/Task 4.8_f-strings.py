"""Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод
столбцами, таким образом:
• первой строкой должны идти десятичные значения байтов
• второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
• столбцами
• ширина столбца 10 символов
Пример вывода для адреса 10.1.1.1:
10 1 1 1
00001010 00000001 00000001 00000001
"""
ip = '192.168.3.1'

#Solution2: from f""-strings
ip = '192.168.3.1'

ip = ip.split(".")
octet1 = int(ip[0])
octet2 = int(ip[1])
octet3 = int(ip[2])
octet4 = int(ip[3])

result = f"""
{octet1:<8} {octet2:<8} {octet3:<8} {octet4:<8}
{octet1:08b} {octet2:08b} {octet3:08b} {octet4:08b}
"""
print(result)
