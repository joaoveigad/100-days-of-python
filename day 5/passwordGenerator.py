import random

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
              'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
              'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', ':',
    ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '}', '~'
]

print("Well now. Let's generate a password!")
passwrdLetters = int(input('How many letters would you like in your password?\n'))
passwrdNumbers = int(input('How many numbers would you like?\n'))
passwrdSymbols = int(input('How many symbols would you like? \n'))

password = ''

for char in range(passwrdLetters):
    password += random.choice(characters)
for num in range(passwrdNumbers):
    password += random.choice(numbers)
for sym in range(passwrdSymbols):
    password += random.choice(symbols)

print(password)  # Pre randomization variable for testing purposes.

# Shuffle implementation

passwordList = list(password)
random.shuffle(passwordList)
cryptoPassword = ''.join(passwordList)
print(cryptoPassword)
