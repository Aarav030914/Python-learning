weight = input("What is your weight(kg):\n")
height = input("What is your height(m):\n")
bmi = int(weight)/int(height)**2
print(bmi) 
if bmi <= 18.5:
    print("You are underweight")
elif 18.5 < bmi <= 25:
    print("you have a normal weight")
elif 25 < bmi <= 30:
    print("You are obese")
else:
    print("You are clinically obese")

