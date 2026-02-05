#START

import random
ans = True
ans_1 = True
i = 1  # Number of cards in the same turn
x = 1  # Determines which player's turn it is
_sum1 = 0
_sum2 = 0
game_over = 0

while True:

    # Player choos if want another card
    while i > 2 or x > 2 and game_over == 0:
        player_input:int = input('Want another card? Answer yes / no only').lower()
        ans = player_input == 'yes'

        # change turn
        if  not ans:
            if x % 2 != 0: # player 1
                print("Player's 2 turn:")
            else: print("Player's 1 turn:")  # Player 2
            x += 1
            i = 1

            # choice:
            if x > 2:
                player_input: int = input('Want another card? Answer yes/no only').lower()
                ans_1 = player_input == 'yes'
                if not ans_1:
                    if _sum1 > _sum2:
                        print('Player 1 win with total:', _sum1)
                        game_over = 1
                    elif _sum2 > _sum1:
                        print('Player 2 win with total:', _sum2)
                        game_over = 1
                    else:
                        print('Same total for two players. draw')
                        game_over = 1
                else:
                    break
        else:
            break

    if ans_1 or ans:
        # take a card
        suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
        card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
        print(suit, card)

        card = (10 if card == "J" or card == "Q" or card == "K" else card)
        card = (1 if card == "A" else card)

        if x % 2 != 0: # player 1
            _sum1 += card
            i += 1

            # win / lose
            if _sum1 == 21:
                print("Player's 1 sum is 21 ! Player 1 win!")
                break
            if _sum1 > 21:
                print("Player's 1 total is",_sum1, ". Player 2 win!")
                break

            # print sum
            if i > 2 or x > 2:
                print("Player's 1 sum: ", _sum1)

        else: # player 2
            _sum2 += card
            i += 1
            if _sum2 == 21:
                print('Players 2 sum is 21 ! Player 1 win!')
                break
            if _sum2 > 21:
                print('Players 2 total is', _sum2, 'Player 2 disqualified. player 1 win!')
                break
            if i > 2 or x > 2:
                print("Player's 2 sum: ", _sum2)
    else:
        break




#STOP
