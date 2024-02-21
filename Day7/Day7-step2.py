
import random

word_list = ["aardvark", "baboon", "camel"]

solution = word_list[random.randint(0,len(word_list) - 1)]

print(f'Jawabannya... {solution}')

kunjaw = []

live = 5

for i in range(len(solution)):
    kunjaw.append('_')

while '_' in kunjaw and live > 0:

    answer = input('Sebutkan 1 huruf... ').lower()
    
    if answer not in solution:
        live -= 1

    for i in range(len(solution)):
        if solution[i] == answer:
            kunjaw[i] = answer
    print(f'Sisa nyawa : {live}')
    print(kunjaw)
    
if live == 0:
    print('LOSER!!!!')

if '_' not in kunjaw:
    print('Kamu menang!!!')