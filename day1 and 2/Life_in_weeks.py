your_age = input("What is your age?:\n")
#if you live for 90 years
num_of_days = 365*(90-int(your_age))
num_of_weeks = 52*(90-int(your_age))
num_of_months = 12*(90-int(your_age))
print(f"You have {num_of_days} days,{num_of_weeks} weeks and {num_of_months} months")