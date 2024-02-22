import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {key.letter : key.code for (index, key) in data.iterrows()}

name = input('Masukkan nama anda... ')

list_word = [word.upper() for word in name if word != " "]

result = [nato_dict[word] for word in list_word]

print(result)
    