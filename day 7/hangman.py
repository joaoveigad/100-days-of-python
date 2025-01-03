import random

words = [
    "bridge", "mountain", "apple", "river", "chair", "cloud", "banana", "city", "forest",
    "bicycle", "book", "stone", "tiger", "carpet", "desert", "lamp", "keyboard", "mirror",
    "giraffe", "ocean", "village", "garden", "orange", "castle", "umbrella", "island",
    "window", "pencil", "sandwich", "planet", "candle", "backpack", "robot", "jungle",
    "grape", "station", "spoon", "pyramid", "camera", "guitar", "painting", "pillow",
    "rocket", "flower", "pebble", "canyon", "bridge", "shoe", "tornado", "coin"
]

chosen_word = random.choice(words)

hidden_word = ''
for letter in chosen_word:
    hidden_word += '_'
print(hidden_word)

player_lives = 6

while player_lives > 0:
    player_letter = input('Guess a letter! \n').lower()

    if len(player_letter) > 1 or not isinstance(player_letter, str):
        print('Please type a single letter.')

    elif player_letter in chosen_word:
        hidden_word_list = list(hidden_word)

        for index, letter in enumerate(chosen_word):
            if letter == player_letter:
                hidden_word_list[index] = player_letter

        hidden_word = ''.join(hidden_word_list)
        print(hidden_word)
        print('Good! Time to guess another one.')
        if not '_' in hidden_word:
            print(f'You did it! You won! The word is indeed {chosen_word}!')
            break

    else:
        print('Bad!')
        player_lives -= 1
        print(f'You now have {player_lives} lives.')

if player_lives == 0:
    print(f'You died! Anywho, the word was: {chosen_word}.')
