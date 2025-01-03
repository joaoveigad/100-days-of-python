alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message! \n").lower()
shift = int(input("Type the shift number: \n"))


def cipher(original_text, shift_amount):
    output = ''
    for letter in original_text:
        if letter not in alphabet:
            output += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
            new_index = alphabet.index(letter) + shift_amount
            new_index %= len(alphabet)
            output += alphabet[new_index]
    print(output)

cipher(text, shift)