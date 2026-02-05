#START
import random

ranks = [
    ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6),
    ("7", 7), ("8", 8), ("9", 9), ("10", 10),
    ("J", 10), ("Q", 10), ("K", 10), ("A", 11)
]

suits = ["spades", "hearts", "diamonds", "clubs"]

def create_shoe():
    shoe = []
    for _ in range(2):
        for rank, value in ranks:
            for suit in suits:
                shoe.append((rank, f"{rank} {suit}", value))
    random.shuffle(shoe)
    return shoe

shoe = create_shoe()

def draw_card():
    global shoe
    if len(shoe) == 0:
        print("\nDealer shuffle cards")
        shoe = create_shoe()
    return shoe.pop()

def calculate_total(values):
    total = sum(values)
    aces = values.count(11)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total

def is_soft_hand(values):
    return 11 in values and calculate_total(values) <= 21

def is_blackjack(names, values):
    return len(values) == 2 and "A" in names and calculate_total(values) == 21

def player_turn(hand, names, values):
    while True:
        total = calculate_total(values)
        print("\nPlayer hand:", " ".join(hand))
        print("Total:", total)

        if total > 21:
            print("Player BUST")
            return total, True

        choice = input("Choose:\n0 = STAND\n1 = HIT\nYour choice: ")

        if choice == "0":
            return total, False

        if choice == "1":
            name, card, value = draw_card()
            hand.append(card)
            names.append(name)
            values.append(value)
        else:
            print("Invalid choice")

def dealer_turn(hand, names, values):
    while True:
        total = calculate_total(values)

        if total < 17:
            name, card, value = draw_card()
            hand.append(card)
            names.append(name)
            values.append(value)

        elif total == 17 and is_soft_hand(values):
            name, card, value = draw_card()
            hand.append(card)
            names.append(name)
            values.append(value)

        else:
            return total

coins = 100

while coins > 0:
    print("\nCoins:", coins)
    bet = int(input("Enter bet amount: "))

    if bet <= 0 or bet > coins:
        print("Invalid bet")
        continue

    player_hand = []
    player_names = []
    player_values = []

    dealer_hand = []
    dealer_names = []
    dealer_values = []

    for _ in range(2):
        name, card, value = draw_card()
        player_hand.append(card)
        player_names.append(name)
        player_values.append(value)

        name, card, value = draw_card()
        dealer_hand.append(card)
        dealer_names.append(name)
        dealer_values.append(value)

    print("\nDealer shows:", dealer_hand[0])

    if is_blackjack(player_names, player_values):
        print("Player hand:", " ".join(player_hand))
        print("BLACKJACK")
        win = int(bet * 1.5)
        coins += win
        print("Player WINS")
        print("You win", win, "coins")
        continue

    player_total, player_bust = player_turn(
        player_hand, player_names, player_values
    )

    if player_bust:
        coins -= bet
        print("Dealer WINS")
        print("You lose", bet, "coins")
        continue

    dealer_total = dealer_turn(
        dealer_hand, dealer_names, dealer_values
    )

    print("\nDealer hand:", " ".join(dealer_hand))
    print("Dealer total:", dealer_total)

    if dealer_total > 21:
        print("Dealer BUST")
        print("Player WINS")
        coins += bet
    elif dealer_total > player_total:
        print("Dealer WINS")
        coins -= bet
    elif dealer_total < player_total:
        print("Player WINS")
        coins += bet
    else:
        print("PUSH")

    if coins <= 0:
        print("Game over – no coins left")
        break









#STOP
