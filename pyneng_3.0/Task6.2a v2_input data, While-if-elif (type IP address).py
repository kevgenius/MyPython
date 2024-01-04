while True:
    ip = input('\nPlease, enter your IP:\n')
    bytes_ip = ip.split('.')

    while True:
        if len(bytes_ip) != 4:
            print('IP incorrect!')
            ip = input('Please, enter your IP again:\n')
            bytes_ip = ip.split('.')
        else:

            for byte in bytes_ip:
                if int(byte) > 255:
                    print('IP incorrect')
                    ip = input('\nWill be careful, enter your IP again:\n')
                    bytes_ip = ip.split('.')
                    break
            else:

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
    break