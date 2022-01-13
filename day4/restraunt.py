import random
people = input("Give me the list of everyone seperated by a comma:")
people_list = people.split(",")
randint = random.randint(0,len(people_list)-1)
name = people_list[randint]
print(f"{name} will pay the bill")
