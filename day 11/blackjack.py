import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1
    return sum(hand)

def determine_winner(player, dealer):
    if player > 21:
        return "You went over 21. You lose!"
    elif dealer > 21:
        return "Dealer went over 21. You win!"
    elif player == dealer:
        return "It's a draw!"
    elif player == 21 and dealer == 21:
        return "Both players got Blackjack! It's a draw!"
    elif player == 21:
        return "Blackjack! You win!"
    elif dealer == 21:
        return "Dealer got Blackjack! You lose!"
    elif player > dealer:
        return "You win! Yay!"
    else:
        return "You lost! Oh no!"

# Main Game Loop
while True:
    insert_coin = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
    if insert_coin == 'n':
        print("Ok, understandable. Have a nice day!")
        break
    else:
        print("Nice! Let's play some cards!")


    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    is_game_over = False

    while not is_game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {player_hand}, total score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score >= 21:
            is_game_over = True
        else:
            draw_another = input("Type 'y' to draw another card, or 'n' to pass: ").lower()
            if draw_another == 'y':
                player_hand.append(deal_card())
            else:
                is_game_over = True


    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    dealer_score = calculate_score(dealer_hand)


    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(determine_winner(player_score, dealer_score))


    play_again = input("Do you want to play another game? Type 'y' or 'n': ").lower()
    if play_again == 'n':
        print("Game over!")
        break
