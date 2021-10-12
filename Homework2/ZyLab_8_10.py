"""Anthony Tran
PSID: 1957342
ZyLab 8.10"""


def space(string):
    no_space = string.replace(" ", "")
    return no_space


def pal(word):
    word.replace(" ", "")
    new_word = word[::-1]
    return new_word


if __name__ == '__main__':
    input_word = input("")
    space_word = space(input_word)
    pal_word = pal(space_word)

    if space_word == pal_word:
        print(input_word, "is a palindrome")
    else:
        print(input_word, "is not a palindrome")
