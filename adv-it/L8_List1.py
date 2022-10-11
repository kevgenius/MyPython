cities = ['New York', 'Moscow', 'new deli', 'Simferopol', 'Toronto']
print(cities)
print(len(cities))
print(cities[-3])
cities[2] = 'Tula'
print(cities)

cities.append('Kursk')   #добавление элемента в конец листа
cities.append('Yalta')   #добавление элемента в конец листа
cities.insert(2, 'Feodosiya') #добавление элемента на позицию

del cities[0]  #удалить элемент на позиции
print(cities)

print(cities.index('Yalta'))   #узнать индекс элемента листа

cities.remove('Kursk')   #удалить конкретный элемент
print(cities)

a = cities.pop()    #удалить последн.элемент
print('Deleted city is: ' +  a)
print(cities)

cities.sort()  #сортировка
print(cities)

cities.sort(reverse=True)    #сортировка в обратном порядке
print(cities)

cities.reverse()             #сортировка в обратном порядке
print(cities)