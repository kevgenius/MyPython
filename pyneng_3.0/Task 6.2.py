ip = input('Please, input your IP:\n')
byte1 = int(ip.split('.')[0])


if byte1 in range(1, 224):
    print('this is Unicast!')
elif byte1 in range(224, 240):
    print('this is Multicast!')
elif ip == '255.255.255.255':
    print('this is Local_Broadcast!')
elif ip == '0.0.0.0':
    print('this is Unassigned!')
else:
    print('Unused :(')


