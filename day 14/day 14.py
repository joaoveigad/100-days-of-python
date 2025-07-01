import random
import time
from data import data

def check_followers(a, b, player_choice):
    if a > b and player_choice == 'a':
        return player_choice
    elif a < b and player_choice == 'b':
        return player_choice
    else:
        return None

def game():
    person_a = random.choice(data)
    person_b = random.choice(data)
    if person_b == person_a:
        person_b = random.choice(data)
    points = 0
    is_game_over = False
    print('Now we are playing a Higher | Lower game!')
    time.sleep(1)
    print('Who do you think has the most followers? A or B?')
    time.sleep(1)

    while not is_game_over:
        print(f"A: {person_a['name']} or B: {person_b['name']}?")
        time.sleep(1)
        player_choice = input('Make your choice! Or press C to stop. ').lower()
        if player_choice not in ('a', 'b', 'c'):
            print('Invalid input! Restarting...')
            time.sleep(2)
            game()
        elif player_choice == 'c':
            print('Game successfully stopped! Bai bai!')
            break
        check = check_followers(person_a['follower_count'],person_b['follower_count'], player_choice)
        if player_choice != check:
            print(f'You died! Your points: {points}' )
            is_game_over = True
        else:
            print('You got this!')
            points = points + 1
            if player_choice == 'a':
                person_b = random.choice(data)
            else:
                person_a = person_b
                person_b = random.choice(data)
                if person_b == person_a:
                    person_b = random.choice(data)

    if is_game_over:
        try_again = input('Want to try again? Yes or no? ').lower()
        if try_again == 'yes':
            game()
        elif try_again == 'no':
            print("Bai bai!")
        else:
            print('It was supposed to be yes or no! You broke the game. You died!')



game()


