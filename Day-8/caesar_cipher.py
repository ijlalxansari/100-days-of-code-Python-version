alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# encoding




def encrypt(plain_text , shift_amount):
    encoded_text =""
    for letter in plain_text:
       if letter in alphabet:  
            current_pos = alphabet.index(letter)
            new_pos = (current_pos + shift_amount)%len(alphabet) 
            new_alphabet =  alphabet[new_pos]    
            encoded_text +=  new_alphabet 
       else:
            print(f"Character '{letter}' is not a valid alphabet. It will be skipped.")
    
     
    print("the encrypted text is " ,encoded_text )       






# decoding

def decode(plained_text , steps_shift):
    decoded_text=""
    for letter in plained_text:
        if letter in alphabet:   
            current_pos = alphabet.index(letter)
            new_pos = (current_pos - steps_shift)%len(alphabet) 
            new_alphabet =  alphabet[new_pos]    
            decoded_text += new_alphabet 
        else:
            print(f"Character '{letter}' is not a valid alphabet. It will be skipped.")

        
    print("the decrypted text is " ,decoded_text )       


# main code



    
while True:
        cipher_art = """
  ____ _ _                _             
 / ___(_) | ___  ___  ___| |_ ___  _ __  
| |   | | |/ _ \/ __|/ _ \ __/ _ \| '_ \ 
| |___| | |  __/\__ \  __/ || (_) | | | |
 \____|_|_|\___||___/\___|\__\___/|_| |_|                            
"""

        print(cipher_art)

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt , type 'exit' for exiting the program :\n")
         
        if  direction == 'exit':
             print("The program will terminate now")
             break  
        
        elif direction  in ['encode' , 'decode']:
            text = input("Type your message:\n").lower()
            try:
                shift = int(input("Type the shift number:\n"))
                if direction =="encode":
                    encrypt(text,shift)
                elif direction == "decode":
                    
                    decode(text ,shift)    
                                   
            except ValueError:
                print("Please enter valid integer number , enter a valid integer ")
        
        else:
            print("Invalid input , please enter either 'encode' or 'decode' ")
            
    
    
    

    
# main ceaseor




