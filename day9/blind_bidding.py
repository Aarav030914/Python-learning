import os
bidders = {}
other_person = "yes"
def bidding():
    name = input("What is your name?:")
    price = int(input("What is your bid? : ₹"))
    bidders[name] = price
while other_person == "yes":
    bidding()
    other_person = input("Is there any person?(yes/no):")
    os.system("cls")
max_key = max(bidders, key=bidders.get)
all_values = []
for key in bidders:
    all_values.append(bidders[key])    
max_value = max(all_values)
if all_values.count(max_value)> 1 :
    print("It is a tie, nobody won")
else:
    print(f"The winner is {max_key} with a bid of ₹{max_value}")



