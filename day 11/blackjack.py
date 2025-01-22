import random

player_hand = []
dealer_hand = []
player_score = 0
is_game_over = False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    cards.remove(card)
    return card

def calculate_score(score):
    if sum(score) == 21 and len(cards) == 2:
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
    score_total = sum(score)
    return score_total

while not is_game_over:
    player_hand.clear()
    dealer_hand.clear()

    insert_coin = input("Do you want to play a game of blackjack? Type 'y' or 'n'. \n").lower()

    if insert_coin == 'n':
        print("Ok, understandable. Have a nice day!")
        break
    elif insert_coin == 'y':
        print("Nice! Let's draw some cards.")

    for i in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print(player_score)

    print(f"Your cards: {player_hand}. Total score: {player_score}")
    print(f"The CPU's first card is: {dealer_hand[0]}")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
        is_game_over = True

    else:
        draw_another = input("Type 'y' to draw another card, type 'n' to pass. \n").lower()
        if draw_another == 'y':
            player_hand.append((deal_card()))
            player_score = calculate_score(player_hand)
            print(f"Your cards: {player_hand}. Total score: {player_score}")
            print(f"The CPU's first card is: {dealer_hand[0]}. And the total is: {dealer_score}")
        else:
            is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    if player_score >= 21 and player_score > dealer_score:
        print('You win! Yay!')
        is_game_over = True
    elif player_score >= 21 and player_score == dealer_score:
        print("It's a draw!")
        is_game_over = True
    else:
        print('You lost! Oh no!')
        is_game_over = True
    insert_coin = input("Do you want to play another game? 'y' or 'n' \n").lower()
    if insert_coin == 'n':
        is_game_over = True

print("Game over!")
