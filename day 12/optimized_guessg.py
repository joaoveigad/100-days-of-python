import random
import time

random_number = random.choice(range(1, 21))

EASY_LIVES = 7
HARD_LIVES = 3


def set_difficulty():
    diff = input('Choose your destiny! Easy or hard.').lower()
    if diff == 'easy':
        return EASY_LIVES
    elif diff == 'hard':
        return HARD_LIVES
    else:
        print('You just broke the game. You died!')
        return None

def check_number(user_guess, answer, lives):
    if user_guess > answer:
        print(f"Too high!")
        return lives - 1
    elif user_guess < answer:
        print(f"Too low!")
        return lives - 1
    else:
        print(f"You got it! The answer is {answer}")
        return None



def game():
    print('Been a while! We will now resume with a number guessing game.')
    time.sleep(2)
    print('The rules are simple. You choose a number between 1 and 20, and if you get it wrong you lose a life!')
    time.sleep(2)
    print("When your life points get to zero you die without any ceremony and that's it.")
    time.sleep(2)
    answer = random.randint(a=1, b=20)
    print(f"Spoiler: the answer is: {answer}!")

    player_lives = set_difficulty()
    print(f"You have {player_lives} to make your guess.")
    time.sleep(2)
    guess = int(input('Choose a number: '))

    check_number(guess, answer, player_lives)



