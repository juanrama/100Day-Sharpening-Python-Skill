bid_finished = False

name_bid = {}
last_bid = 0

def insert_bid(name, value):
    name_bid[value] = name

def find_max(dict):
    list_dict = list(dict.keys())
    max_key = max(list_dict)
    final_name = dict[max_key]
    
    return final_name
    
    
while bid_finished == False:
    print('Selamat datang di Pelelangan')
    state = input('Apakah anda mau melelang? Ketik "y" atau "n" ')
    
    if state == 'n':
        bid_finished = True
        winner = find_max(name_bid)
        print('Pelelangan telah berakhir')
        print(f'Pelelangan dimenangkan oleh {winner}')
    
    if bid_finished == False:
        print(f'Last Bid = {last_bid}')
        nama = input('Masukkan nama anda.... ')
        nilai = int(input('Masukkan nominal yang anda ajukan...'))
        
        if nilai > last_bid:
            insert_bid(nama, nilai)
            last_bid = nilai
        else:
            while nilai <= last_bid:
                print(f'Nilai harus melebihi bid sebelumnya ({last_bid})')
                nilai = int(input('Masukkan nominal yang anda ajukan...'))
                
            insert_bid(nama, nilai)
            last_bid = nilai
            
    
    
    