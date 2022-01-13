for i in range(1,101):
    div_by_3 = i%3
    div_by_5 = i%5
    if div_by_3 == 0 and div_by_5 == 0:
        print("Fizzbuzz")
    elif div_by_5 == 0 and div_by_3 != 0:
        print("buzz")
    elif div_by_3 == 0 and div_by_5 !=0:
        print("Fizz")
    else:
        print(i)
                    
