"""Преобразовать MAC-адрес mac в двоичную строку такого вида:
101010101010101010111011101110111100110011001100"""

mac = 'AAAA:BBBB:CCCC' #6байт по 8бит

#Solutions:
mac = mac.split(":")

octet1 = list(mac[0])
octet2 = list(mac[1])
octet3 = list(mac[2])


byte1 = octet1[0] + octet1[1]
byte1 = bin(int(byte1, 16))
byte1 = byte1[2::]

byte2 = octet1[2] + octet1[3]
byte2 = bin(int(byte2, 16))
byte2 = byte2[2::]

byte3 = octet2[0] + octet2[1]
byte3 = bin(int(byte3, 16))
byte3 = byte3[2::]

byte4 = octet2[2] + octet2[3]
byte4 = bin(int(byte4, 16))
byte4 = byte4[2::]

byte5 = octet3[0] + octet3[1]
byte5 = bin(int(byte5, 16))
byte5 = byte5[2::]

byte6 = octet3[2] + octet3[3]
byte6 = bin(int(byte6, 16))
byte6 = byte6[2::]

result = byte1 + byte2 + byte3 + byte4 + byte5 + byte6
print(result)