alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cipher(original_text, shift_amount, encode_or_decode):
    encrypted_text = ''
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            encrypted_text += letter
        else:
            new_index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print(encrypted_text)


while True:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt. Type 'leave' to end: \n").lower()
    if direction == 'leave':
        break
    elif direction not in ["encode", "decode"]:
        print("Please type the correct option!")
        continue

    text = input("Type your message! \n").lower()
    shift = int(input("Type the shift number: \n"))
    cipher(text, shift, direction)
    break
