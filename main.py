from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(sample_text, shift_amount, direction):
    final_text = ""
    if direction == "decode":
          shift_amount *= -1
    
    for letter in sample_text:
        if letter not in alphabet:
            final_text += letter
        else:
            original_index = alphabet.index(letter)
            
    
            if original_index + shift_amount < len(alphabet):
                final_text += alphabet[original_index + shift_amount]
            else:
                final_text += alphabet[(original_index + shift_amount) - len(alphabet)]
        
    print(f"Here's the {direction}d result: {final_text}")

#print the logo from art.py when the program starts.
print(logo)

restart = True

while restart is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % len(alphabet)
    #print(shift)

    caesar(text, shift, direction)
    
    restart_answer = input("Do you want to restart the caesar cipher program? Type 'yes' or 'no'\n").lower()
    
    if restart_answer == "no":
        restart = False

