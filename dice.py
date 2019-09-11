import random

print("Welcome! Roll the dice :)")

try:
    sides = int(input("How many sides: "))
except:
    print("The dice needs 1+ sides")
    sides = 1

run = "y"

while run.lower() == "y":
    randomNumber = random.randint(1, 6)
    print(randomNumber)

    run = input("Do you want to roll the dice again? Y/N")