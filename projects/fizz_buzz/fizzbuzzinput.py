import sys
can_start = False
n = "s"

while can_start == False:
    try:
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        elif len(sys.argv) > 2:
            n = int(input("You supplied too many initial arguments.\nwhat upper limit would you like to use?\n"))
        elif len(sys.argv) == 1:
            n = int(input("Let's play fizz buzz! Enter an upper limit.\n"))
    except ValueError:
        try:
            n = int(input("Positive integers only!\n"))
        except ValueError:
            pass
    try:
        if n == int(n) and n > 0:
            can_start = True
    except ValueError:
        pass
        
print("Fizz buzz counting up to {}".format(n))

for number in range(1,n):
    if (number % 3 == 0 and number % 5 == 0):
        print("fizz buzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)