import random
import time

random_number = random.choice(range(1, 21))

def check_number():
    print('Now, to choose your difficulty!')
    player_lives = 0
    time.sleep(2)
    diff = input('Easy | Hard: ').lower()
    if diff == 'easy':
        player_lives = 10
    elif diff == 'hard':
        player_lives = 5
    else:
        print('Now you broke the game! Good job >:(')
    while player_lives > 0:
        chosen_number = int(input('Choose a number, please: '))
        if chosen_number > random_number:
            player_lives -= 1
            print(f'Too high! Your current lives: {player_lives}.')
        elif chosen_number < random_number:
            player_lives -= 1
            print(f'Too low! Your current lives: {player_lives}')
        else:
            print("That's it! You win!")
            break
    if player_lives == 0:
        print('I guess you died!')

print('Been a while! We will now resume with a number guessing game.')
time.sleep(2)
print('The rules are simple. You choose a number between 1 and 20, and if you get it wrong you lose a life!')
time.sleep(2)
print("When your life points get to zero you die without any ceremony and that's it.")
time.sleep(2)
check_number()
