
# This is blackjack

import random

def random_list(dict):
    i = random.choice(list(dict.keys()))
    return i

def sum_card(x):
    list_2 = x.copy()
    for i in range(len(list_2)):
        list_2[i] = card[list_2[i]]
    total_num = sum(list_2)
    
    if total_num > 21:
        if 'A' in x:
            total_num -= 10
    
    return total_num

def true_false(x):
    value = False
    if x == 'y':
        value = True
    elif x == 'n':
        value = False
        
    return value
        

    
card = {
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K': 10,
    'A' : 11
}

player1 = []
player2 = []



total_num = 0
total_num_2 = 0

continue_game = True

round = 0


while continue_game == True:
    #Add 2 card to each player
    print('---------BLACKJACK GAME---------')
    player1.append(random_list(card))
    player2.append(random_list(card))
    player1.append(random_list(card))
    player2.append(random_list(card))
    
    stand = False
    
    total_num = sum_card(player1)
    total_num_2 = sum_card(player2)
    
    round += 1
    if round == 1 and total_num == 21 and total_num_2 == 21:
        print('Anda seri melawan komputer')
        stand = True
        round = 0
    elif round == 1 and total_num == 21:
        print(f'Jumlah kartu anda {total_num} (blackjack)')
        stand = True
        round = 0
    elif round == 1 and total_num_2 == 21:
        print('Anda kalah, pihak lawan memiliki blackjack')
        stand = True
        round = 0
    
    if stand == False:
        is_stand = input('Do you want to stand or hit (S / H).....').lower
        if is_stand == 's':
            stand = True
        elif is_stand == 'h':
            stand = False

    print(f'#### Kartu pertama lawan adalah {player2[0]} ####')
        
    while stand == False and total_num <= 21:
        
        player1.append(random_list(card))
        print(f'Kartu anda adalah {player1}')
        total_num = sum_card(player1)
        print(f'Nilai kartu anda adalah {total_num}') 
        if total_num < 21:
            is_stand = input('Do you want to stand or hit (S / H).....').lower()
            if is_stand == 's':
                stand = True
                
    stand_2 = random.choice([True, False])
    
    print(f'Kartu lawan adalah {player2}')
            
    while stand_2 == False and total_num_2 < 21:
        player2.append(random_list(card))
        print(f'Kartu lawan adalah {player2}')
        total_num_2 = sum_card(player2)
        stand_2 = random.choice([True, False])
    
    if total_num > total_num_2 and total_num <= 21:
        print(f'Player 1 Win dengan skor player 1 ({total_num}) dan player 2 ({total_num_2})')
    elif total_num > total_num_2 and total_num > 21:
        print(f'Player 2 Win dengan skor player 2 ({total_num_2}) dan player 1 ({total_num})')
    elif total_num_2 > total_num and total_num_2 <= 21:
        print(f'Player 2 Win dengan skor player 2 ({total_num_2}) dan player 1 ({total_num})')
    elif total_num_2 > total_num and total_num_2 > 21:
        print(f'Player 1 Win dengan skor player 1 ({total_num}) dan player 2 ({total_num_2})')
    
    total_num = 0
    total_num_2 = 0
    player1 = []
    player2 = []
    
    continue_game = true_false(input('Apakah anda ingin melanjutkan permainan? '))
    
    
        
        
        
    
    