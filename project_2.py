
num_fib = int(input("How many number of the fibonacci sequence would you like to add? "))
even_odd = input("Would you like to add the even or odd of the numbers? ")

def is_even(x):
    return x % 2

def fib():
    a = 0
    b = 1
    x = a + b
    total = 0
    for i in range(num_fib):
        a = b
        b = x
        x = a + b
        is_even(x)
        if is_even and even_odd == "even" or (is_even and even_odd == "odd"):
            total = total + x
    print(total)

fib()


#def is_even(x):
#    return x % 2
#
#for i in range ():
#    if(i a_even(i))
#    print(i)
