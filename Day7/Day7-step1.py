#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0,len(word_list) - 1)]

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
answer = input('Sebutkan 1 huruf... ').lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if answer in chosen_word:
    print('Huruf tersebut ada')
else:
    print('Huruf tersebut tidak ada')

