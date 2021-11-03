"""Anthony Tran
PSID: 1957342
Final Project Part 1"""

import csv
from operator import itemgetter
from datetime import datetime

# Empty lists for appending data from files
m_list = []
p_list = []
sd_list = []

# Empty lists for appending certain types of devices
laptop_inventory = []
phone_inventory = []
tower_inventory = []

# Empty list for past inventory
past_service_inventory = []

# Creates variables for list inputs(as according to the requirement of needing to work with any file groups)
man_input = input('Enter the name of the Manufacture List File: ')
price_input = input('Enter the name of the Price List File: ')
sd_input = input('Enter the name of the Service Date List File: ')

# These code below are for reading lines of each input file and appending it to the corresponding variable
with open(man_input, 'r') as csv_file:
    man_li = csv.reader(csv_file)
    for var in man_li:
        m_list.append(var)

with open(price_input, 'r') as csv_file:
    pri_li = csv.reader(csv_file)
    for var in pri_li:
        p_list.append(var)

with open(sd_input, 'r') as csv_file:
    ser_li = csv.reader(csv_file)
    for var in ser_li:
        sd_list.append(var)


# Function that sorts the input lists from above
def sort_list_func(list_sort):
    list_sort = (sorted(list_sort, key=itemgetter(0)))
    return list_sort


# Calling to the above functions with the inputted lists
sorted_man_list = sort_list_func(m_list)
sorted_price_list = sort_list_func(p_list)
sorted_sd_list = sort_list_func(sd_list)

# Makes a new list and appends the sorted lists from above to the new list
new_list = []

for var in sorted_man_list:
    new_list.append(var)

for var in range(0, len(new_list)):
    new_list[var].append(sorted_price_list[var][1])

for var in range(0, len(new_list)):
    new_list[var].append(sorted_sd_list[var][1])

# This list sorts the new list from above
inventory_sorted = (sorted(new_list, key=itemgetter(1)))

''' This loop below goes through the sorted inventory list and checks for damaged items, if found, it will append 
it to a new list, it will also append the damaged factor to the end of the sorted inventory list.'''
damaged_items = []
for var in range(0, len(inventory_sorted), 1):
    if inventory_sorted[var][3] == "damaged":
        inventory_sorted[var].append(inventory_sorted[var][3])
    elif inventory_sorted[var][3] == "damaged":
        damaged_items.append(inventory_sorted[var])
    inventory_sorted[var].remove(inventory_sorted[var][3])

# This code will write the data from the sorted inventory list to the full inventory file
with open('FullInventory.csv', 'w') as csv_file:
    split = csv.writer(csv_file, lineterminator='\n', delimiter=',')
    for var in inventory_sorted:
        split.writerow(var)

# The for loops below take each electronic type and appends it according to the the item type.
for var in range(0, len(inventory_sorted), 1):
    if inventory_sorted[var][2] == 'phone':
        phone_inventory.append(inventory_sorted[var])

for var in range(0, len(inventory_sorted), 1):
    if inventory_sorted[var][2] == 'laptop':
        laptop_inventory.append(inventory_sorted[var])

for var in range(0, len(inventory_sorted), 1):
    if inventory_sorted[var][2] == 'tower':
        tower_inventory.append(inventory_sorted[var])

# These 3 blocks of code takes each of the item type lists and writes the data to the respected item type file.
with open('PhoneInventory.csv', 'w') as csv_file:
    phone_split = csv.writer(csv_file, lineterminator='\n', delimiter=',')
    for var in phone_inventory:
        phone_split.writerow(var)

with open('LaptopInventory.csv', 'w') as csv_file:
    laptop_split = csv.writer(csv_file, lineterminator='\n', delimiter=',')
    for var in laptop_inventory:
        laptop_split.writerow(var)

with open('TowerInventory.csv', 'w') as csv_file:
    tower_split = csv.writer(csv_file, lineterminator='\n', delimiter=',')
    for var in tower_inventory:
        tower_split.writerow(var)

''' This loop checks the sorted inventory lists for dates that are past the current date, using 
the imported date function, and if it is past service, it will append to a new list for past dates'''
today_date = datetime.now().date()
for var in range(0, len(inventory_sorted), 1):
    inv_date = inventory_sorted[var][4].split('/')
    year = int(inv_date[2])
    day = int(inv_date[1])
    month = int(inv_date[0])
    if datetime(year, month, day).date() < today_date:
        past_service_inventory.append(inventory_sorted[var])

# These 2 code blocks will write data from the past service list and damaged item lists to corresponding files.
with open('PastServiceDateInventory.csv', 'w') as csv_file:
    past_split = csv.writer(csv_file, lineterminator='\n', delimiter=',')
    for var in past_service_inventory:
        past_split.writerow(var)

with open('TowerInventory.csv', 'w') as csv_file:
    damaged_split = csv.writer(csv_file, lineterminator='\n', delimiter=',')
    for var in damaged_items:
        damaged_split.writerow(var)
