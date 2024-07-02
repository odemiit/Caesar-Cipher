alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    for letter in plain_text:
        original_index = alphabet.index(letter)
        if original_index + shift_amount < len(alphabet):
            encrypted_text += alphabet[original_index + shift_amount]
        else:
            encrypted_text += alphabet[(original_index + shift_amount) - len(alphabet)]

    print(f"The encoded text is {encrypted_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    decrypted_text = ""
    for letter in cipher_text:
        original_index = alphabet.index(letter)
        if original_index - shift_amount >= 0:
            decrypted_text += alphabet[original_index - shift_amount]
        else:
            decrypted_text += alphabet[(original_index - shift_amount) + len(alphabet)]

    print(f"The decoded text is {decrypted_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#encrypt(text, shift)
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)