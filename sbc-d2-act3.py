from random import randint

print("WELCOME TO SWERTRES!\n")

user_bet = input("Place your 3-digit bet: ")

print(f"Your 3-digit bet: {user_bet}")

winning_num = ([str(randint(0, 9)) for _ in range(3)])

print(f"The winning number is: {winning_num}")

if user_bet == winning_num:
    print("You Won!")
elif sorted(user_bet) == sorted(winning_num):
    print("You partially won!")
else:
    print("Sorry, better luck next time!")
