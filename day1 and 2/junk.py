condition2 = input("User input2:")
condition1 = input("User input1:")
if condition1 == "true":
    print("Access granted")
elif condition1 =="false":
    print("Access denied")
else:
    print("input invalid")
    exit(0)
if condition2 == condition1:
    print("conditions match")
elif condition2 != condition1:
    print("Conditions do not match")
            

