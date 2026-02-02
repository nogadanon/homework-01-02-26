#START

import random

player_score = 0
computer_score = 0


while True:
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    print("Your card is:   ", suit, card)

    computer_suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    computer_num = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    print("Computer card is:", computer_suit, computer_num)

    card, computer_num = (11 if card == "J" else card), (11 if computer_num == "J" else computer_num)
    card, computer_num = (12 if card == "Q" else card), (12 if computer_num == "Q" else computer_num)
    card, computer_num = (13 if card == "K" else card), (13 if computer_num == "K" else computer_num)
    card, computer_num = (14 if card == "A" else card), (14 if computer_num == "A" else computer_num)

    if card > computer_num:
        player_score += 1
    if computer_num > card:
        computer_score += 1
    print('your score:', player_score, '  computer score:', computer_score)
    if player_score == 10:
        print("You win!")
        break
    if computer_score == 10:
        print("Computer win!")
        break

#STOP
