print("Welcome to Mr.piza's")
print("The pizzas are\n Small sized pizza:15$\n Medium sized pizza:20$\n Large sized pizza:25$")
total_price = 0
pizza_size = input("What size of pizza do you want?(s,m or l):")
if pizza_size == "s":
    total_price += 15
elif pizza_size == "m":
    total_price += 20
elif pizza_size == "l":
    total_price += 25
else:
    print("Please enter a valid size")   
print("Extra price for pepproni in s,m and l is $3,$4 and $5 respectively")
toppings = input("Do you want pepproni in your pizza?(type y or n):")
if toppings =="y":
    if pizza_size == 's':
        total_price += 3
    elif pizza_size =='m':
        total_price += 4
    elif pizza_size == 'l':
        total_price += 5
cheese = input("Do you want extra cheese?extra price:2$(type y or n):")
if cheese =="y":
   total_price += 2

else:
   total_price += 0
print(f"Your total price is {total_price}$")   


