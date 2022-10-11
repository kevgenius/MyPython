ip = input('\nPlease, enter your IP:\n')
bytes = ip.split('.')

while True:
    if len(bytes) != 4:
        print('IP incorrect!')
        ip = input('Please, enter your IP again:\n')
        bytes = ip.split('.')
    else:

        for byte in bytes:
            if int(byte) > 255:
                print('IP incorrect')
                ip = input('\nWill be careful, enter your IP again:\n')
                bytes = ip.split('.')
        else:

            if bytes[0] > str(1) and bytes[0] <= str(223):
                print('-=Unicast=')
            elif bytes[0] > str(223) and bytes[0] <= str(239):
                print('-=Multicast=-')
            elif ip == '255.255.255.255':
                print('-=Local_Broadcast=-')
            elif ip == '0.0.0.0':
                print('-=Unassigned=-')
            else:
                print(' Unused :(')
            break


