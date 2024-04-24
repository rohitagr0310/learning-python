import os

os.system("cls")

secret_word = input("Enter the secret word (Not case-sensetive) : ")
hint = input("Do you have any hint to share : ")
guess_limit = 3

secret_word.upper
os.system("cls")

print(f"The hint is = {hint}")
while guess_limit:
    guess = input("Guess the secret word (Not case-sensetive) : ")
    guess.upper
    guess_limit = guess_limit - 1
    if guess == secret_word:
        print("You Won!\n")
        print(f"The Secret word was {secret_word}")
        break

    else:
        print("\nWrong guess")
        print(f"Rember The hint is = {hint}")
        print(f"Guess left {guess_limit}\n")
else:
    print("Sorry, You failed!!")
    print(f"The Answer was {secret_word}\n")
