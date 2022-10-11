
#           <---Item---->
#             KEY    VALUE
enemy = {
            'loc_x = ': 70,
            'loc_y = ': 50,
            'color': 'green',
            'health': 100,
            'name': 'Mudilo'
        }
print(enemy)

print(enemy['loc_y = '])
print('Location_X :' +str(enemy['loc_x = ']))
print('Locatyion_Y: ' + str(enemy['loc_y = ']))
print('His name is '+ enemy['name'])

enemy['rank'] = 'Admiral'   #add element to end
print(enemy)

del enemy['rank']  #delete element
print(enemy)

enemy['loc_x = '] = 60
print('---------------------------------------------------------------------------------------------------')

enemy['loc_x = '] = enemy['loc_x = '] + 50
enemy['health'] = enemy['health'] - 21
if enemy['health'] < 80:
    enemy['color'] = 'yellow'
print(enemy)
print(enemy.keys())
print(enemy.values())