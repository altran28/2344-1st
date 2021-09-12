"""Anthony Tran
PSID: 1957342
Coding Problem 1"""
print('Birthday Calculator')
print('Current Day')
cmonth = int(input('Month: '))
cday = int(input('Day: '))
cyear = int(input('Year: '))
print('Birthday')
bmonth = int(input('Month: '))
bday = int(input('Day: '))
byear = int(input('Year: '))
age = 0
if cmonth < bmonth:
    age = (cyear - byear) - 1
elif cmonth > bmonth:
    age = cyear - byear
elif cmonth == bmonth:
    if cday > bday:
        age = cyear - byear
    elif cday < bday:
        age = (cyear - byear) - 1
    else:
        age = cyear - byear
print('You are', age, 'years old.')
