import random
from art import logo
 
def deal_card():
    Cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card= random.choice(Cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(users_score, computers_score):
    if users_score == computers_score:
        return "draw"
    elif computers_score == 0:
        return "you Lose,   The opponent has the BlackJack"
    elif users_score == 0:
        return "You Win,   You has the BlackJack"
    elif users_score > 21:
        return "You went over,  You Lose"
    elif computers_score > 21:
        return "Oponent went over,   You Win"
    elif users_score > computers_score:
        return "You Win"
    else:
        return "You Lose"
def Play_game():
    print(logo)
    user_cards= []
    computer_cards= []

    IS_GAMEOVER= False
    computer_score= -1
    user_score= -1
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not IS_GAMEOVER:

        user_score= calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"computer's cards: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            IS_GAMEOVER= True
        else:
            WANT_TO_CONTINUE= input("Type 'y' to get another card, type 'n' to pass: ")
            if WANT_TO_CONTINUE == 'y':
                user_cards.append(deal_card())
            else:
                IS_GAMEOVER = True
    while computer_score < 17 and not IS_GAMEOVER and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards},  Your final score: {user_score}")
    print(f"Computers final hand: {computer_cards},  Computers final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack?  Type 'y' or 'n': ") == "y":
    print("\n" * 50)
    Play_game()
print("Tschüss! Bis später")
