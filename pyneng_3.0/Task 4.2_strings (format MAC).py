"""Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX"""
mac = 'AAAA:BBBB:CCCC'

#Solution:
mac = mac.replace(":", ".")
print(mac)
