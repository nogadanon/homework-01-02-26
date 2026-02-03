#START

# להוסיף מספר תורים שווה לשני שחקנים


import random

ans = True
ans_1 = True
i = 1
x = 1
_sum1 = 0
_sum2 = 0

while True:
    # take a card
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    print(suit, card)

    card = (10 if card == "J" or card == "Q" or card == "K" else card)
    card = (1 if card == "A" else card)

    if x % 2 != 0: # player 1
        _sum1 += card # Calculating amounts

        # win / lose
        if _sum1 == 21:
            print("Player's 1 sum is 21 ! Player 1 win!")
            break  # no 'break' fair game
        if _sum1 > 21:
            print("Player's 1 total is", _sum1, 'Player 1 disqualified')
            break

        # print sum
        if i >= 2 or x > 2:
            print("Player's 1 sum: ", _sum1)

            # Player selection question
            player_input:str = input('Want another card? Answer yes/no only').lower()
            ans = player_input == 'yes'

            # change turn
        if ans == False:
            print('change turn')
            x += 1
            i = 1
        else:
            i += 1

    else:  # player 2
        ans = True    #reset answer
        _sum2 += card
        if _sum2 == 21:
            print("Player's 2 sum is 21 ! Player 2 win!")
            break
        if _sum2 > 21:
            print("Player's 2 total is",_sum2, "Player 2 disqualified")
            break
        if i >= 2 or x > 2:
            print("Player's 2 sum: ", _sum2)
            player_input = input('Want another card? Answer yes/no only').lower()
            ans = player_input == 'yes'
        if ans == False:
            print('change turn')
            x += 1
            i = 1
        else:
            i += 1
            if

    if _sum1 == _sum2:
        print('*draw* both players total is equal')












#STOP
