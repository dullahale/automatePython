alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))
shift = shift % 26


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(message, shift_amount):
    # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift

    cipher_Text = ""
    for i in message:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_Text += new_letter

        else:
            cipher_Text += i

    print(f"The encoded text is {cipher_Text}")


# Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(message=text, shift_amount=shift)
