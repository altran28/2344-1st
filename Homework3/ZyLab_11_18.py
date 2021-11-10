"""Anthony Tran
PSID: 1957342
ZyLab 11.18"""

user_input = [int(i) for i in input().split()]

sorted_numbers = sorted(user_input)
new_list = []
for val in range(len(user_input)):
    if user_input[val] >= 0:
        new_list.append(user_input[val])
new_list.sort()
print(*new_list, end=' ')
