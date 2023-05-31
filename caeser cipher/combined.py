# My solution to Caesar Cipher using if statements
from art import logo as logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
print(logo)
print()
repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26


    def caesar(message, shift_amount, cipher_direction):
        if cipher_direction == "encode":
            cipher_Text = ""
            for i in message:
                # added if statement incase user puts in symbols, spaces, numbers and other characters
                if i in alphabet:
                    position = alphabet.index(i)
                    new_position = position + shift_amount
                    new_letter = alphabet[new_position]
                    cipher_Text += new_letter

                else:
                    cipher_Text += i

            print(f"The {cipher_direction}d text is {cipher_Text}")

        elif cipher_direction == "decode":
            cipher_Text = ""
            for i in message:
                if i in alphabet:
                    # added if statement incase user puts in symbols, spaces, numbers and other characters
                    position = alphabet.index(i)
                    new_position = position - shift_amount
                    new_letter = alphabet[new_position]
                    cipher_Text += new_letter

                else:
                    cipher_Text += i

            print(f"The {cipher_direction}d text is {cipher_Text}")

        else:
            print("Try a different direction suggested above")


    caesar(message=text, shift_amount=shift, cipher_direction=direction)
    # Asks the user if they wish to continue or exit the program
    answer = input("Type 'yes' to go again and 'no' to exit: ")
    if answer == "yes":
        repeat = True
    else:
        repeat = False
