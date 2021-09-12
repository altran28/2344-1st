"""Anthony Tran
PSID: 1957342
ZyLab 5.22"""

print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")
print('Select first service:')
first = input('')
print('Select second service:')
second = input('')

serv1 = ''
cost = 0
if first == 'Oil change':
    cost = 35
    serv1 = 'Service 1: Oil change, $35'
elif first == 'Tire rotation':
    cost = 19
    serv1 = 'Service 1: Tire rotation, $19'
elif first == 'Car wash':
    cost = 7
    serv1 = 'Service 1: Car wash, $7'
elif first == 'Car wax':
    cost = 12
    serv1 = 'Service 1: Car wax, $12'
else:
    serv1 = 'Service 1: No service'

serv2 = ''
cost2 = 0
if second == 'Oil change':
    cost2 = 35
    serv2 = 'Service 2: Oil change, $35'
elif second == 'Tire rotation':
    cost2 = 19
    serv2 = 'Service 2: Tire rotation, $19'
elif second == 'Car wash':
    cost2 = 7
    serv2 = 'Service 2: Car wash, $7'
elif second == 'Car wax':
    cost2 = 12
    serv2 = 'Service 2: Car wax, $12'
else:
    serv2 = 'Service 2: No service'

print("\nDavy's auto shop invoice\n")
print(serv1)
print(serv2)

print('\nTotal: ', '$', (cost + cost2), sep='')
