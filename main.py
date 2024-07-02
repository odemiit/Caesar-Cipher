alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(sample_text, shift_amount, direction):
    final_text = ""
    if direction == "encode":
        for letter in sample_text:
            original_index = alphabet.index(letter)
            if original_index + shift_amount < len(alphabet):
                final_text += alphabet[original_index + shift_amount]
            else:
                final_text += alphabet[(original_index + shift_amount) - len(alphabet)]

        print(f"The encoded text is {final_text}")
    elif direction == "decode":
        for letter in sample_text:
            original_index = alphabet.index(letter)
            if original_index - shift_amount >= 0:
                final_text += alphabet[original_index - shift_amount]
            else:
                final_text += alphabet[(original_index - shift_amount) + len(alphabet)]

        print(f"The decoded text is {final_text}")
    
    

# def encrypt(plain_text, shift_amount):
#     encrypted_text = ""
#     for letter in plain_text:
#         original_index = alphabet.index(letter)
#         if original_index + shift_amount < len(alphabet):
#             encrypted_text += alphabet[original_index + shift_amount]
#         else:
#             encrypted_text += alphabet[(original_index + shift_amount) - len(alphabet)]

#     print(f"The encoded text is {encrypted_text}")

# def decrypt(cipher_text, shift_amount):
#     decrypted_text = ""
#     for letter in cipher_text:
#         original_index = alphabet.index(letter)
#         if original_index - shift_amount >= 0:
#             decrypted_text += alphabet[original_index - shift_amount]
#         else:
#             decrypted_text += alphabet[(original_index - shift_amount) + len(alphabet)]

#     print(f"The decoded text is {decrypted_text}")

#Call the correct function based on what "direction" the user inputs
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)