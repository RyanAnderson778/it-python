import math
import time
from banner import banner
banner("PYTHAGOREAN CALCULATOR", "Ryan Anderson")

time.sleep(.4)
print("We will help you find the missing side of a right triange. The lengths of the two")
print("legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")

playagain = None

while playagain != "N":
    a = None
    b = None
    c = None
    num = None
    length = None
    eq1 = None
    eq2 = None
    eq3 = None
    eq_a = None
    eq_b = None
    eq_c = None
    inv_eq = None
    time.sleep(.8)
    print("")
    print("Please enter the length of each side, or leave it blank if you don't know.")
    a = input("a =  ")
    b = input("b =  ")
    c = input("c =  ")

    if a != "":
        eq_a = 1
        a = float(a)
    else:
        eq_a = 0

    if b != "":
        eq_b = 1
        b = float(b)
    else:
        eq_b = 0

    if c != "":
        eq_c = 1
        c = float(c)
    else:
        eq_c = 0

    inv_eq = eq_a+eq_b+eq_c
    if inv_eq == 3:
        print("You have no missing sides. Please try again.")
        continue

    eq1 = eq_a+eq_b
    eq2 = eq_a+eq_c
    eq3 = eq_b+eq_c

    if eq1 == 2:
        num = float(a*a+b*b)
        length = math.sqrt(num)
        print(f"Your missing side is c and it's length is {length}")
    elif eq2 == 2:
        num = float(c*c-a*a)
        length = math.sqrt(num)
        print(f"your missing side is b and it's length is {length}")
    elif eq3 == 2:
        num = float(c*c-b*b)
        length = math.sqrt(num)
        print(f"Your missing side is a and it's length is {length}")
    else:
        print("There is not enough information to determine the missing side and its length.")

    while playagain != "Y":
        time.sleep(.5)
        print("")
        playagain = input("Would you like to calculate another triangle (Y/N)? ")
        if playagain == "N":
            break
        elif playagain == "Y":
            break
        else:
            print("Please enter a valid input")


time.sleep(.5)
print("")
print("Thank you for using the Pythragorean Calculator")