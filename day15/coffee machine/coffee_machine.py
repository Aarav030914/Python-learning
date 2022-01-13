# TODO:1 Prompt the user to choose any one of these Espresso, Cappuchino, Latte
# TODO:2 Check whether there are all the necessary resources to make that drink
# TODO:3 If there are not enough resources then let the user know about it
# TODO:4 If resources are enough then ask the user to pay with the coin and tell them the price
# TODO:5 If coins are not enough then ask the user to pay more or abort the operation
# TODO:6 Give user the change and the coffee and prompt them again to choose a drink

from data import RESOURCES_REQUIRED, resources_available, CURRENCY, COST

user_choice_list = ["report","off","espresso","cappuchino","latte"]

# check resources
def check_resources():
    defeciency = False
    if resources_available["water"] < 0:
        print("Enough Water is not there")
        defeciency = True
    if resources_available["coffee"] < 0:
        print("Enough coffee is not there")
        defeciency = True
    if resources_available["milk"] < 0:
        print("Enough milk is not there")
        defeciency = True
    if defeciency == True:
        exit(0)
    else:
        pass

def user_choice(user_input):
    
    if user_input == "report":
        print(resources_available)
    else:
        for item in RESOURCES_REQUIRED:
            if item["name"] == user_input:
                # change the resources available in the coffee machine
                resources_available["water"] -= item["water"]
                resources_available["milk"] -= item["milk"]
                resources_available["coffee"] -= item["coffee"]
                resources_available["money"] += item["money"] 
                print(f"you ordered {user_input} and you total amount is ${COST[user_input]}") # print the price of the item
                check_resources()
            else:
                pass
    

# collect money function    
def collect_money(user_input):
    print("Please pay the money")
    
    # recieve input coins from the user
    user_quaters = int(input("Quaters:"))
    user_dimes = int(input("Dimes:"))
    user_pennies = int(input("Pennies"))
    user_nickles = int(input("Nickles:"))
    
    #calculate total money
    total_money = CURRENCY["quater"]*user_quaters + CURRENCY["dime"]*user_dimes + CURRENCY["pennie"]*user_pennies + CURRENCY["nickle"]*user_nickles
    
    # calculate change
    for item in RESOURCES_REQUIRED:
        if item["name"] == user_input:
            change = total_money - item["money"]
            if change < 0:
                print(" Please pay more money\n" "Money Refunded" )
            print(f"Your Change is ${change}")    
    print(f"Here is your {user_input}, Enjoy!")
   
# Final output    
while True:
    user_drink = input("What would you like to have?(Espresso/Cappuchino/Latte):").lower()
    if user_drink == "off":
        exit(0)
    if user_drink not in user_choice_list:
        print("Please enter a valid input")
    else:
        user_choice(user_drink)
        collect_money(user_drink)
    

        


             

