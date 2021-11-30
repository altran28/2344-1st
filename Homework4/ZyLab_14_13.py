"""Anthony Tran
PSID: 1957342
ZyLab 14.13"""

num_calls = 0


def partition(ids, i, k):
    pivot = ids[k]
    index = i - 1
    for var in range(i, k):
        if ids[var] <= pivot:
            index += 1
            ids[index], ids[var] = ids[var], ids[index]
    ids[index + 1], ids[k] = ids[k], ids[index + 1]
    return index + 1


def quicksort(r_ids, i, k):
    if i < k:
        var2 = partition(r_ids, i, k)
        quicksort(r_ids, i, var2 - 1)
        quicksort(r_ids, var2 + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)
    var_calls = 2 * len(user_ids)
    num_calls = int(var_calls - 1)
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
