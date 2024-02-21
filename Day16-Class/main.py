from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_coffee = Menu()
coffee_machine = CoffeeMaker()
transaction = MoneyMachine()

turn_on = True
    
while turn_on == True:
    coffee = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if coffee == 'report':
        coffee_machine.report()
    
    else:
        coffee_true = menu_coffee.find_drink(order_name = coffee)
    
        if coffee_true != None and coffee_true != 'report':
            if coffee_machine.is_resource_sufficient(drink=coffee_true) == True:
                money = transaction.make_payment(coffee_true.cost)
                if money == True:
                    coffee_machine.make_coffee(order=coffee_true)
            
    
        




