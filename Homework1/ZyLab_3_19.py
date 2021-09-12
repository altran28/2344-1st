"""Anthony Tran
PSID: 1957342
ZyLab 3.19"""

import math

print('Enter wall height (feet):')
wallh = int(input())
print('Enter wall width (feet):')
wallw = int(input())
print('Wall area:', (wallh * wallw), 'square feet')
paintn = (wallh * wallw) / 350
print('Paint needed:', '{:.2f}'.format(paintn), 'gallons')
print('Cans needed:', math.ceil(paintn), 'can(s)\n')

print('Choose a color to paint the wall:')
redpn = math.ceil(paintn) * 35
bluepn = math.ceil(paintn) * 25
greenpn = math.ceil(paintn) * 23
color = input('')
if color == 'red':
    print('Cost of purchasing red paint: ' '$', redpn, sep='')
elif color == 'blue':
    print('Cost of purchasing blue paint: ' '$', bluepn, sep='')
else:
    print('Cost of purchasing green paint: ' '$', greenpn, sep='')
