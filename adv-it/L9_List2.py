#        0      1      2       3        4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for x in cars:         # в "х" засовываются элементы из "cars" и перебираются циклом
    print(x.upper())

for y in range(1, 6):  # в "х" засовываются элементы из "от 1 до 6" и перебираются циклом
    print(y)

print('----------------------------------------------------------')
mynumber_list = list(range(0, 10))
print(mynumber_list)

for a in mynumber_list:
    a=a*2
    print(a)
print('----------------------------------------------------------')


print(mynumber_list)
mynumber_list.sort(reverse=True)
print(mynumber_list)
print('----------------------------------------------------------')

print(max(mynumber_list))
print(min(mynumber_list))
print(sum(mynumber_list))

print('----------------------------------------------------------')

#        0      1      2       3        4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
mycars = cars[1:4] #выводится лист mycars из элементов от 1 до 3 из cars
print(mycars)
print('----------------------------------------------------------')
A = cars[:]
print(A)
B = cars[:4]   #до 4ех не включая
print(B)
C = cars[1:3]  #до 3ех не включая
print(C)
D = cars[-3:-1]  #от -3 включая до -1 не включая
print(D)

print('----------------------------------------------------------')
#        0      1      2       3        4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
CARS = cars.copy()
print(CARS)
print(id(cars))
print(id(CARS))