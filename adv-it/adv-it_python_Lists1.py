cities = ["New York", "Moscow", "new deli", "Simferopol", "Toronto"]
print(cities)
print(len(cities))

print(cities[4])
print(cities[-1])


print(cities[2].upper())
cities[2] = "Tula"
print(cities)


cities.append("Kursk")
print(cities)

cities.append("Yalta")
print(cities)

cities.insert(2, "Feodosia")
print(cities)

cities.pop(-1)
print(cities)

cities.remove("Kursk")
print(cities)

cities.pop()  #если индекс не указан явно, то удаляет последний элемент
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)