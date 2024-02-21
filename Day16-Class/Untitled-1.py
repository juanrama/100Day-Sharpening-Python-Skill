from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_coffee = Menu
coffee_machine = CoffeeMaker
transaction = MoneyMachine

print(menu_coffee.find_drink(order_name = 'latte'))