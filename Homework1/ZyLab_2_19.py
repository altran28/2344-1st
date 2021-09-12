"""Anthony Tran
PSID: 1957342
ZyLab 2.19"""

print('Enter amount of lemon juice (in cups):')
lemjui = float(input())
print('Enter amount of water (in cups):')
water = float(input())
print('Enter amount of agave nectar (in cups):')
agave = float(input())
print('How many servings does this make?')
servings = int(input())

print('\nLemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemjui), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar\n')

print('How many servings would you like to make?\n')

servings2 = int(input())
servings3 = servings2 / servings
print('Lemonade ingredients - yields', '{:.2f}'.format(servings2), 'servings')
lemjui = lemjui * servings3
water = water * servings3
agave = agave * servings3
print('{:.2f}'.format(lemjui), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar\n')

print('Lemonade ingredients - yields', '{:.2f}'.format(servings2), 'servings')
lemjui = lemjui / 16
water = water / 16
agave = agave / 16
print('{:.2f}'.format(lemjui), 'gallon(s) lemon juice')
print('{:.2f}'.format(water), 'gallon(s) water')
print('{:.2f}'.format(agave), 'gallon(s) agave nectar')
