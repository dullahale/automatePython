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
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_Text += new_letter

        else:
            cipher_Text += i

        print(f"The decoded text is {cipher_Text}")


# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(message, shift_amount):
    # Inside the 'decrypt' function, shift each letter of the 'text'

    cipher_Text = ""
    for i in message:
        position = alphabet.index(i)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_Text += new_letter
    print(f"The decoded text is {cipher_Text}")


# Check if the user wanted to encrypt or decrypt the message by checking the 'direction'
# variable. Then call the correct function based on that 'drection' variable.
# You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(message=text, shift_amount=shift)
elif direction == "decode":
    decrypt(message=text, shift_amount=shift)
else:
    print("Enter correct direction!!!")


