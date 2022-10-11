enemy = {
            'loc_x': 70,
            'loc_y': 50,
            'color': 'green',
            'health': 100,
            'name': 'Mudilo',
            'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
        }
all_enemies = []

all_enemies.append(enemy.copy())
print(all_enemies)
print('----------------------------------------------------------------------------')

for x in range(0, 10):
    all_enemies.append(enemy.copy())
print(all_enemies)

print('______________________________________________________________________________________________________')
all_enemies[0]['health'] = 30
all_enemies[2]['name'] = 'Kozel'
all_enemies[2]['loc_x'] = all_enemies[2]['loc_x'] + 233    #равносильно записи:  all_enemies[2]['loc_x']  += 10

print('----------------------------------------------------------------------------')
for y in all_enemies:
    print(y)

print('----------------------------------------------------------------------------')

