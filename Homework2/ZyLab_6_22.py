"""Anthony Tran
PSID: 1957342
ZyLab 6.22"""

coe1 = int(input())
coe2 = int(input())
result1 = int(input())
coe3 = int(input())
coe4 = int(input())
result2 = int(input())

check = "no"


def equation1(num1, num2):
    ans = coe1 * num1 + coe2 * num2
    return ans


def equation2(num1, num2):
    ans2 = coe3 * num1 + coe4 * num2
    return ans2


for num_x in range(-10, 11):
    for num_y in range(-10, 11):
        if (equation1(num_x, num_y) == result1) and (equation2(num_x, num_y) == result2):
            check = "yes"
            print(num_x, num_y)

if check == "no":
    print("No solution")
