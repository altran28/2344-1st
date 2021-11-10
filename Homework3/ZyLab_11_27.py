"""Anthony Tran
PSID: 1957342
ZyLab 11.27"""

diction = {}
for num in range(5):
    player_num = str(num + 1)
    jersey_number = int(input("Enter player " + player_num + "'s jersey number:\n"))
    player_rating = int(input("Enter player " + player_num + "'s rating:\n"))
    if (0 <= jersey_number < 100) and (0 < player_rating < 10):
        diction[jersey_number] = player_rating
    print()
print("ROSTER")
for key in sorted(diction):
    print("Jersey number:", str(key) + ', Rating:', diction[key])

option = ''
while option != 'q':
    print()
    print('MENU')
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    option = input("Choose an option:")
    print()

    if option == 'a':
        jersey_number = int(input("Enter player's jersey number:\n"))
        player_rating = int(input("Enter player's rating:\n"))
        if (0 <= jersey_number < 100) and (0 < player_rating < 10):
            diction[jersey_number] = player_rating
    elif option == 'd':
        jersey_number = int(input("Enter player's jersey number:\n"))
        del diction[jersey_number]
    elif option == 'u':
        jersey_number = int(input("Enter player's jersey number:\n"))
        if jersey_number in diction:
            player_rating = int(input("Enter a new rating for player:\n"))
            diction[jersey_number] = player_rating
    elif option == 'r':
        player_rating = int(input("Enter a rating:\n"))
        print()
        print('ABOVE', player_rating)
        for key in sorted(diction):
            if diction[key] > player_rating:
                print("Jersey number:", str(key) + ', Rating:', diction[key])
    elif option == 'o':
        print("ROSTER")
        for key in sorted(diction):
            print("Jersey number:", str(key) + ', Rating:', diction[key])
    elif option == 'q':
        break
