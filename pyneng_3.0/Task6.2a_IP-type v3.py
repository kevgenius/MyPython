while True:
    ip = input('\nPlease, enter your IP:\n')
    bytes_ip = ip.split('.')

    if len(bytes_ip) != 4:
        print('IP incorrect!')
        continue
    # for byte in bytes_ip:
    #     if int(byte) > 255:
    #         print('IP incorrect')
    #         continue
    if any(filter(lambda byte: byte > 255, map(int, bytes_ip))):
        print('IP incorrect')
        continue

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
