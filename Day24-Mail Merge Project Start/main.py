#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


new_text = []
list_name = []

with open('./Input/Names/invited_names.txt', 'r') as j:
    names = j.read()
    name = map(str, names.split())
    for i in name:
        list_name.append(i)

print(list_name)

for name in list_name:
    with open('./Input/Letters/starting_letter.txt', 'r') as i:
        text = i.readlines()
        x = text[0].replace('[name]', name)
        text[0] = x
        new_text.append(text)

for num in range(len(new_text)):
    with open(f'./Output/ReadyToSend/{list_name[num]} Letter', 'w') as w:
        y = ''.join(new_text[num])
        w.write(y)
        
    
    
    