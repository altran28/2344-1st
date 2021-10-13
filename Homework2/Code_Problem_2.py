"""Anthony Tran
PSID: 1957342
Code Problem 2"""

month_list = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6", "july": "7",
              "august": "8", "september": "9", "october": "10", "november": "11", "december": "12"}

i = 0
list1 = []
list2 = []
list3 = []

while True:
    user_input = input()
    if user_input == "-1":
        break
    list1.append(user_input)
list1.append("-1")

while list1[i] != "-1":
    new_lis = list1[i].split(" ")
    if new_lis[0].lower() in month_list:
        end_of_date = new_lis[1]
        if end_of_date.endswith(","):
            if (new_lis[2]) <= "2021":
                date_month = str(month_list[new_lis[0].lower()])
                date_day = str(new_lis[1][:-1])
                date_year = str(new_lis[2])
                new_date = date_month + '/' + date_day + '/' + date_year
                list2.append(new_date)
    i += 1
print('\n'.join(list2))
