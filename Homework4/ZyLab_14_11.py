"""Anthony Tran
PSID: 1957342
ZyLab 14.11"""


def selection_sort_descend_trace(num):
    for var in range(len(num) - 1):
        var2 = var
        for i in range(var + 1, len(num)):
            if num[i] > num[var2]:
                var2 = i
        num[var], num[var2] = num[var2], num[var]
        str_new = [str(x) for x in num]
        str2 = ' '.join(str_new) + ' '
        print(str2)
    return num


if __name__ == "__main__":
    numbers = [int(val) for val in input().split()]
    selection_sort_descend_trace(numbers)
