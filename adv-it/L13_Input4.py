password = 'megasecret'

your_password1 = input('Enter your password: ')
your_password2 = input('Repeat enter your password: ')

print('-'*100)

for x in range(1):
    if your_password1 != your_password2:
        print('True one more time, left 3 attempts')
        password1 = input('Repeat input your password: ')
    else:
        print('Password were created');break

if password1 != your_password1:
    print('True one more time, left 2 attempts')
    password2 = input('Repeat input your password: ')
else:
    print('Password were created');

if password2 != your_password1:
    print('True one more time, left 1 attempts')
    password3 = input('Repeat input your password: ')
else:
    print('Password were created');


if password3 != your_password1:
    print('Password were not created. ')
    exit()
else:print('Password were created');

print('-'*100)
print('Welcome to My site')
print('-'*100)
