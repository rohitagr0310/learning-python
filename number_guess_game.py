import os

os.system("cls")

secret_number = int(input("Enter the secret number : "))
guess_limit = 3

os.system("cls")

while guess_limit:
    guess = int(input("Enter your guess: "))
    guess_limit = guess_limit - 1
    if guess == secret_number:
        print("You Won!\n")
        break
    else:
        print("Wrong guess")
        print(f"Guess left {guess_limit}\n")
else:
    print("Sorry, You failed!!")
    print(f"The Answer was {secret_number}\n")
