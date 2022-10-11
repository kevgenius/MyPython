while True:
    message = input('Enter your Password: ');
    if message == '$ecret':
        break
    print('Your input Password is not correct')
print('Congratulations, your Password is correct!)

#вводим значения и постоянно выводится сообщение об ошибке, пока вводимое нами значение не станет равно '$ecret',
#после - прерывание и вывод поздравления!
