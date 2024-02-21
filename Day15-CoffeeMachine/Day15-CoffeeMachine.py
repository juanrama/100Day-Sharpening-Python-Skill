MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}

def yes_no(x):
    if x == 'y':
        return True
    else:
        return False

def coffee_machine():
    turn_on = True
    
    while turn_on == True:
        coffee = input('What would you like? (espresso/latte/cappuccino): ').lower()
        
        if coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
            total_bill = MENU[coffee]['cost']
            is_enough = True
            for i in MENU[coffee]['ingredients']:
                if resources[i] < MENU[coffee]['ingredients'][i]:
                    is_enough = False

            if is_enough == False:
                print('Mohon maaf bahan tidak cukup, silahkan memesan yang lain')
            
            elif is_enough == True:
                quarter = int(input('How many quarter? ')) * 0.25
                dimes = int(input('How many dimes? ')) * 0.10
                nickles = int(input('How many nickles? ')) * 0.05
                pennies = int(input('How many pennies? ')) * 0.05
                
                user_money = quarter + dimes + nickles + pennies
                
                if user_money >= total_bill:
                    charge = user_money - total_bill
                    print(f'Ini kopi {coffee} anda ☕, silahkan menikmati')
                    print(f'Ini kembalian anda, ${round(charge)}')
                    for i in MENU[coffee]['ingredients']:
                        resources[i] = resources[i] - MENU[coffee]['ingredients'][i]
                    resources["money"] = resources["money"] + user_money
                    turn_on = yes_no(input('Apakah anda ingin membeli kopi lagi? (y/n)... '))
                elif user_money < total_bill:
                    print('Mohon maaf uang anda, tidak cukup.')
                    turn_on = yes_no(input('Apakah anda ingin membeli kopi lagi? (y/n)... '))
                    
        elif coffee == 'report':
            print(f'Water : {resources["water"]}ml')
            print(f'Milk : {resources["milk"]}ml')
            print(f'Coffee : {resources["coffee"]}gr')
            print(f'Money : ${resources["money"]}')

if __name__ == "__main__":
    coffee_machine()
        
        
        
            
        
        