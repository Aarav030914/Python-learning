n = 0
def our_function():
    global n
    if n < 10:
        print("Hello World!")
        n = n + 1
        our_function()
our_function()                