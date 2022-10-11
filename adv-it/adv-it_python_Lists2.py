cars = ["bmw", "vw", "seat", "skoda", "lada"]
print(cars)

for car in cars:
    print(car.upper())

for x in range(1, 6):
    print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)

for num in mynumber_list:
    num = num * 2
    print(num)

print("-"*100)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is: " + str(max(mynumber_list)))
print("Min number is: " + str(min(mynumber_list)))
print("Sum number from list is: " + str(sum(mynumber_list)))
print("-"*100)

mycars = cars[2:4]
print(mycars)

mycars = cars[:4]
print(mycars)

mycars = cars[-3:]
print(mycars)
print(cars)

mycars = cars[-3:-1]
print(mycars)
print("-"*100)

mycars = cars
print(id(cars))
print(id(mycars))

print("*"*10)

mycars = cars[:]
print(id(cars))
print(id(mycars))