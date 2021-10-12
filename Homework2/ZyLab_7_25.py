"""Anthony Tran
PSID: 1957342
ZyLab 7.25"""


def exact_change(user_total):
    if user_total == 0:
        print("no change")
    elif user_total > 0:
        dollars = user_total // 100
        user_total = user_total % 100
        quarters = user_total // 25
        user_total = user_total % 25
        dimes = user_total // 10
        user_total = user_total % 10
        nickels = user_total // 5
        user_total = user_total % 5
        pennies = user_total // 1
        return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars > 0:
        if 0 < num_dollars < 2:
            print(num_dollars, "dollar")
        else:
            print(num_dollars, "dollars")
    if num_quarters > 0:
        if 0 < num_quarters < 2:
            print(num_quarters, "quarter")
        else:
            print(num_quarters, "quarters")
    if num_dimes > 0:
        if 0 < num_dimes < 2:
            print(num_dimes, "dime")
        else:
            print(num_dimes, "dimes")
    if num_nickels > 0:
        if 0 < num_nickels < 2:
            print(num_nickels, "nickel")
        else:
            print(num_nickels, "nickels")
    if num_pennies > 0:
        if 0 < num_pennies < 2:
            print(num_pennies, "penny")
        else:
            print(num_pennies, "pennies")
