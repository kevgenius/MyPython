password = 'megasecret'
your_password1 = input('Enter your password: ')
your_password2 = input('Repeat enter your password: ')


while password1 != your_password1:
    password1 = input('Input your password: ')
    if password1 != your_password1:
        print('Wrong password, left 3 attempts...')
        print('-'*100)
    else:
        print('Welcome!')
        print('-'*100)
        exit()

