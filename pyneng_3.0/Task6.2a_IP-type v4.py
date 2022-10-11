while True:
    ip = input('\nPlease, enter your IP:\n')
    bytes_ip = ip.split('.')
    try:
        if len(bytes_ip) == 4:
            for byte in bytes_ip:
                if int(byte) in range(0, 256):
                    if 1 <= int(bytes_ip[0]) < 224:
                        print('-=Unicast=')
                    elif 224 <= int(bytes_ip[0]) <= 239:
                        print('-=Multicast=-')
                    elif ip == '255.255.255.255':
                        print('-=Local_Broadcast=-')
                    elif ip == '0.0.0.0':
                        print('-=Unassigned=-')
                    else:
                        print(' Unused :(')
                    break
                else:
                    print("Неправильный адрес")
    except ():
        print("Должно быть 4 байта!")






