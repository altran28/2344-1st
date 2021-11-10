"""Anthony Tran
PSID: 1957342
ZyLab 11.22"""

user_input = input()
list_input = user_input.split()

new_list = []
for word in range(len(list_input)):
    x = list_input.count(list_input[word])
    print(list_input[word], x)
