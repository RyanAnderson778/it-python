from banner import banner
banner("ZIP CODE SORTER", "Ryan Anderson")
print("")

print("Welcome to the Newaygo County zip code sorter.")

again = "Y"

while again != "N":
    print("")
    zc = input("Please enter a zip code: ")
    if zc == "49309":
        print("The zip code 49309 is for Bitely.")
        again = input("Would you like to enter another zip code (Y/N)? ")
        while again != "Y":
            if again == "N":
                break
            else:
                print("")
                print("Please choose a valid input")
                again = input("Would you like to enter another zip code (Y/N)? ")
    elif zc == "49312":
        print("The zip code 49312 is for Brohman.")
        again = input("Would you like to enter another zip code (Y/N)? ")
        while again != "Y":
            if again == "N":
                break
            else:
                print("")
                print("Please choose a valid input")
                again = input("Would you like to enter another zip code (Y/N)? ")
    elif zc == "49337":
        print("The zip code 49337 is for Croton and Newaygo.")
        again = input("Would you like to enter another zip code (Y/N)? ")
        while again != "Y":
            if again == "N":
                break
            else:
                print("")
                print("Please choose a valid input")
                again = input("Would you like to enter another zip code (Y/N)? ")
    elif zc == "49412":
        print("The zip code 49412 is for Fremont.")
        again = input("Would you like to enter another zip code (Y/N)? ")
        while again != "Y":
            if again == "N":
                break
            else:
                print("")
                print("Please choose a valid input")
                again = input("Would you like to enter another zip code (Y/N)? ")
    elif zc == "49413":
        print("The zip code 49413 is for Fremont.")
        again = input("Would you like to enter another zip code (Y/N)? ")
        while again != "Y":
            if again == "N":
                break
            else:
                print("")
                print("Please choose a valid input")
                again = input("Would you like to enter another zip code (Y/N)? ")
    elif zc == "49327":
        print("The zip code 49327 is for Grant.")
        again = input("Would you like to enter another zip code (Y/N)? ")
        while again != "Y":
            if again == "N":
                break
            else:
                print("")
                print("Please choose a valid input")
                again = input("Would you like to enter another zip code (Y/N)? ")
    elif zc == "49349":
        print("The zip code 49349 is for White Cloud.")
        again = input("Would you like to enter another zip code (Y/N)? ")
        while again != "Y":
            if again == "N":
                break
            else:
                print("")
                print("Please choose a valid input")
                again = input("Would you like to enter another zip code (Y/N)? ")
    else:
        print(f"The zip code {zc} is not in Newaygo County")
        again = input("Would you like to enter another zip code (Y/N)? ")
        while again != "Y":
            if again == "N":
                break
            else:
                print("")
                print("Please choose a valid input")
                again = input("Would you like to enter another zip code (Y/N)? ")

print("")
print("Thank you for using the Newaygo County zip code sorter. Goodbye!")