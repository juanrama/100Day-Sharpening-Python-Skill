import random

lanjut = True
attempt = 0
answer = 0

def attempt_num(x):
    y = 0
    if x == "easy":
        y = 5
    elif x == "hard":
        y = 3
        
    return y

def true_false(x):
    if x == 'y':
        return True
    
    elif x == 'n':
        return False
        
    

while lanjut == True :
    print("Selamat datang")
    attempt = attempt_num(input("Pilih tingkat kesulitan (easy/hard)..... ").lower())
    
    answer = random.randint(1,100)
    
    print(answer)
    
    user_answer = int(input('Tebak angkanya....(1-100)'))
    
    while user_answer != answer and attempt > 0 :
        if user_answer > answer:
            print("Too high")
            attempt -= 1
            print(f"Sisa percobaan anda tinggal {attempt} lagi, semangat")
            user_answer = int(input('Tebak angkanya....(1-100)'))
        elif user_answer < answer:
            print("Too low")
            attempt -= 1
            print(f"Sisa percobaan anda tinggal {attempt} lagi, semangat")
            user_answer = int(input('Tebak angkanya....(1-100)'))
    
    if user_answer == answer:
        print("Selamat jawaban anda benar!!!") 
        print("-----------------------------")
    else:
        print("Mohon maaf jawaban anda salah dan jumlah percobaan anda telah habis :(")
        print("-----------------------------")
    
    lanjut = true_false(input("Apakah anda ingin mengulangi permainannya? (y/n)...... "))
    print("--------------------------------------------")
    