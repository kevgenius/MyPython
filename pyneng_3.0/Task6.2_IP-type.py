ip = input('Please, input your IP:\n')
bytes = ip.split('.')

if bytes[0] >= str(1) and bytes[0] <= str(223):
    print('this is Unicast!')
elif bytes[0] > str(223) and bytes[0] <= str(239):
    print('this is Multicast!')
elif ip == '255.255.255.255':
    print('this is Local_Broadcast!')
elif ip == '0.0.0.0':
    print('this is Unassigned!')
else:
    print('Unused :(')



