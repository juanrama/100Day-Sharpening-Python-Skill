
# Fungsi operasi

def add(a, b):
    c = a + b
    return c

def minus(a, b):
    c = a - b
    return c

def multiply(a, b):
    c = a * b
    return c

def divide(a, b):
    c = a//b
    return c

# App kalkulator

continue_calc = True
continue_num = False

num1 = 0

while continue_calc == True:
    if continue_num == False:
        print('Selamat datang di kalkulator')
        
    operasi = input('Masukkan operasi yang anda inginkan (+, -, /, *).... ')
    
    if num1 == 0:
        num1 = int(input('Masukkan angka pertama... '))
    num2 = int(input('Masukkan angka kedua... '))
    
    if operasi == '+':
        num1 = add(num1, num2)
    elif operasi == '-':
        num1 = minus(num1, num2)
    elif operasi == '/':
        num1 = divide(num1, num2)
    elif operasi == '*':
        num1 = multiply(num1, num2)
        
    print(f'Hasil operasi adalah {num1}')
    
    lanjut = input(f'Apakah anda akan melanjutkan operasi dengan angka {num1}? (y atau n)..')
    if lanjut == 'y':
        continue_num = True
    elif lanjut == 'n':
        continue_num = False
        num1 = 0
        
    