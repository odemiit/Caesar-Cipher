from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(sample_text, shift_amount, direction):
    final_text = ""
    if direction == "decode":
          shift_amount *= -1
    
    for letter in sample_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if letter not in alphabet:
            final_text += letter
        else:
            original_index = alphabet.index(letter)
            
    
            if original_index + shift_amount < len(alphabet):
                final_text += alphabet[original_index + shift_amount]
            else:
                final_text += alphabet[(original_index + shift_amount) - len(alphabet)]
        
    print(f"Here's the {direction}d result: {final_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

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

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

