print("Welcome to the tip calculator")
bill = int(input("What is the total Bill?: $"))
no_of_people = int(input("How many people do you want to split the bill into?:"))
tip = int(input("What percentage of tip do you want to give?(12, 15 or 20):"))
percentage = 1 + tip/100
amount = (bill/no_of_people)*percentage
final_amount = round(amount,2)
print(f"The amount each person has to pay is:{final_amount} $")