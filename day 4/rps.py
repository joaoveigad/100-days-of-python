import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
       _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """  
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

choices = [rock, paper, scissors]

playerChoice = int(input("Let's play rock-paper-scissors game! What will be your choice? Type 0 for rock, 1 for paper "
                         "and 2 for scissors: "))

wincons = {  # or win conditions, for short.
    (0, 2): "Rock crushes Scissors! You win!",
    (1, 0): "Paper covers Rock! You win!",
    (2, 1): "Scissors cut Paper! You win!"
}

computerChoice = random.choice(choices)

if playerChoice < 0 or playerChoice > len(choices) - 1:
    print('Invalid number! Please try again.')
else:
    computerChoice = random.randint(0, 2)
    print(f'You chose: \n{choices[playerChoice]}')
    print(f'The computer chose: \n {choices[computerChoice]}')

    if playerChoice == computerChoice:
        print("It's a tie!")

    elif (playerChoice, computerChoice) in wincons:
        print(wincons[(playerChoice, computerChoice)])

    else:
        print('You lose!')
