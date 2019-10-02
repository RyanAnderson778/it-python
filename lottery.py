from banner import banner
import random
banner("LOTTERY", "Ryan Anderson")

balance = 20

print("Welcome to the Lottery Game. Choose a number between 1 and 999. If you choose the")
print("same as the computer you will win 10 times your bet amount.")
print("")
while balance != 0:
    number = random.randint(1, 999)
    print(f"BALANCE: ${balance}")
    bet_text = input("How much do you want to bet? ")
    bet = int(bet_text)
    balance = balance - bet
    if balance < 0:
        print(f"You bet {bet}, but you only have {balance + bet}! Please try again!")
        balance = balance + bet
        continue
    pick = int(input("What number do you pick? "))
    randompick = 1
    if pick == number:
        bet_reward = bet * 11
        balance = balance + bet_reward
        print(f"Awesome, you chose {pick}, and so did the computer! You win ${bet_reward} this round.")
    else:
        print(f"I'm sorry, but you chose {pick} and the computer chose {number}. You lose ${bet} this round.")
    if balance > 999999:
        print("")
        print("You win!")
        print(f"BALANCE: ${balance}")
        break
if balance == 0:
    print("You lose! Try again!")