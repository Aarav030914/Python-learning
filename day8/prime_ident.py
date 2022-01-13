def prime_calc(number):
    remainders = []
    for i in range(2,number):
        remainders.append(number%i)
    if 0 in remainders:
        print("It's not a prime number")
    else:
        print("It's a prime number")
prime_calc(47)                