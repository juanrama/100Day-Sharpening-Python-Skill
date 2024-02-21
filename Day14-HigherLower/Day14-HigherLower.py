import random

data = [
    {
        'nama' : 'Tom Holland',
        'num_follower' : 66000000,
        'pekerjaan' : 'Aktor'
    },
    {
        'nama' : 'Billie Ellish',
        'num_follower' : 110000000,
        'pekerjaan' : 'Penyanyi'
    },
    {
        'nama' : 'Taylor Swift',
        'num_follower' : 279000000,
        'pekerjaan' : 'Penyanyi'
    },
    {
        'nama' : 'Robert Downey Jr',
        'num_follower' : 57000000,
        'pekerjaan' : 'Aktor'
    },
    {
        'nama' : 'Mark Zuckenburg',
        'num_follower' : 12000000,
        'pekerjaan' : 'CEO'
    },
    {
        'nama' : 'Zulfikar Juan Pramasta',
        'num_follower' : 10000000,
        'pekerjaan' : 'Data Scientist (Aamiin)'
    },
    {
        'nama' : 'Joko Widodo',
        'num_follower' : 57000000,
        'pekerjaan' : 'Presiden'
    }
]

def compare(a, b):
    if a['num_follower'] > b['num_follower']:
        return 'a'
    elif a['num_follower'] < b['num_follower']:
        return 'b'

def yes_no(x):
    if x == 'y':
        return True
    else:
        return False
    

def higher_lower():
    skor = 0
    is_true = True
    
    while is_true == True:
        if skor > 0:
            print(f'Skor anda sekarang : {skor}')
        a = data[random.randint(1,len(data) - 1)]
        b = data[random.randint(1,len(data) - 1)]
        while a == b or a['num_follower'] == b['num_follower']:
            a = data[random.randint(1,len(data) - 1)]
            b = data[random.randint(1,len(data) - 1)]
        print(f'Nama : {a["nama"]}, Pekerjaan : {a["pekerjaan"]}')
        print(' ')
        print(' ')
        print("           _______ ")
        print("|\\     /|\\(  ____ \\")
        print("| )   ( || (    \\/")
        print("| |   | || (_____ ")
        print("( (   ) )(_____  )")
        print(" \\ \\_/ /       ) |")
        print("  \\   /  /\\____) |")
        print("   \\_/   \\_______)")
        print(' ')
        print(' ')
        print(f'Nama : {b["nama"]}, Pekerjaan : {b["pekerjaan"]}')
        
        answer = compare(a, b)
        
        guess = input('Manakah yang memiliki follower lebih besar??(a/b) ')
        
        if guess == answer:
            skor += 1
            print('Selamat jawaban anda benar, skor + 1')
        else:
            print('Mohon maaf, jawaban anda salah')
            print(f'Skor yang anda dapatkan = {skor}')
            is_true = yes_no(input('Apakah anda ingin bermain lagi? (y/n)...').lower())
            print('-------------------------------------')
            if is_true == True:
                skor = 0
        

        
        
        
            
            
            
            
            
            
            