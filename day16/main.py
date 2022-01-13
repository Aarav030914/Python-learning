# importing modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
 
# defining our ingredients
latte = MenuItem(name = "latte", cost = 2.50, water = 20, coffee = 16, milk = 30)
espresso = MenuItem(name = "espresso", cost = 1.50, water = 50, coffee = 18, milk = 0)
cappuchino = MenuItem(name = "cappuchino", cost = 3.00, water = 25, coffee = 24, milk = 50)

# defining coffee machine components
my_coffee_machine = CoffeeMaker()
my_money_collector = MoneyMachine()
my_menu = Menu()

# collecting user order
while True:
    user_choice = input(f"What would you like to have? {my_menu.get_items()}:")
    

    if user_choice == "off":
        exit(0)
    elif user_choice == "report":
        my_coffee_machine.report()
    elif user_choice in ["latte", "cappuchino", "espresso"]:
        user_order = globals()[user_choice]
        if my_coffee_machine.is_resource_sufficient(user_order):
            print(f"Your total cost is {user_order.cost}")
            my_money_collector.make_payment(user_order.cost)   
            my_coffee_machine.make_coffee(user_order)                        
    else:
        print("Please entre a valid input")        

