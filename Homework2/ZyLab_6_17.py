"""Anthony Tran
PSID: 1957342
ZyLab 6.17"""

old_pass = input()

new_pass = ''

for letter_num in range(0, len(old_pass)):
    letter = old_pass[letter_num]
    if letter == "i":
        new_pass += "!"
    elif letter == "a":
        new_pass += "@"
    elif letter == "m":
        new_pass += "M"
    elif letter == "B":
        new_pass += "8"
    elif letter == "o":
        new_pass += "."
    else:
        new_pass += letter
new_pass = new_pass + "q*s"
print(new_pass)
