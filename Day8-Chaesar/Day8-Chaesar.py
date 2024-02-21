alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    
    text_list = list(text)
    
    for i in range(len(text_list)):
        shift_amount = alphabet.index(text_list[i]) + shift
        if shift_amount < len(alphabet):
            text_list[i] = alphabet[shift_amount]
        else:
            text_list[i] = alphabet[-1 + shift]
    
    new_text_list = ''.join(text_list)
    
    print(new_text_list)
      

def decrypt(text, shift):
    text_list = list(text)
    
    for i in range(len(text_list)):
        shift_amount = alphabet.index(text_list[i]) - shift
        text_list[i] = alphabet[shift_amount]
    new_text_list = ''.join(text_list)
    
    print(new_text_list)

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift) 
    
