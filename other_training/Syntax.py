a = 'Hello'
b = 25
print(a)
print(b)

f_name = 'Evgen'
s_name = 'Korban'
age = 25

full_name = f_name + ' ' + s_name + ' '
print(full_name + str(age))

F_NAME = 'EVGEN'
print(f_name + '------>' + F_NAME)

num1 = 11111111111111111111
num2 = 4444444444444444444444
num3 = num1 + num2
print(num3)

print('-'*100)
print('STRING INTRO:')





mystring = 'Bla bla bla'
name = 'mr.vasya pupkin'
print(name.title())
print(name.upper())
print(name.lower())
print('Privet stroka N1\nPrivet stroka N2')

print('Message you:\n\tMessage1\n\tMessage2\n\tMessage3\n\tEND')
print('Lower_name:' + ' ' + name.lower())
n = '   ..dydya_vasya  ..'
print(n.strip().strip('.').title())
print('-'*100)
print('NUMBERS')








num1 = 18
num2 = 20
num3 = num1 + 10
print(num3)

x1 = 3333333333333333333333333333333333333333333333
x2 = 777777777777777777777777777777777777777777
print(x1*x2)
print(num2/3)

a = 6
b = 4
print(a/b)
print((10*2/5)+3)
print('-'*100)








print('LISTS INTRO:')
cities = ['Moscow', 'New York', 'new Deli', 'Symferopol', 'Toronto']
print(cities)
len(cities)
print(len(cities))
print(cities[2].upper())


cities[2] = 'Smolensk'
print(cities)
print(cities.append('Yalta'))
print(cities)

print(cities.insert(2, 'San Francisco'))
print(cities)

print(cities.pop(-1))
print(cities)
print(cities.remove('Toronto'))
print(cities)

deleted_city = cities.pop()
print(deleted_city)
print(cities.sort())
cities.reverse()
print(cities)
print(sorted(cities))
print(cities)

print('*'*100)
tuple_example = type(tuple)
list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
tuple_example = tuple(list_keys)
print(tuple_example)
print(sorted(tuple_example))
print(tuple_example)
print(tuple_example[0])
vlans = [10, 20, 30, 40, 100, 10]
print(vlans)
set1 = set(vlans)
print(set1)
type(set1)


set1.add(3000)
print(set1)
set1.discard(300)
print(set1)

set1.clear()
print(set1)

set2 = set()
print(set2)
tuple2 = tuple()
print(tuple2)
print(type(tuple2))
print('*'*100)

