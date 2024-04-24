l_numbers = [1, 1, 1, 1, 8]
f_numbers = [6, 2, 6, 2, 2]

choice = input("What do you wish to print l or f: ")

if choice.lower() == "f":
    for number in f_numbers:
        print("x" * number)

elif choice.lower() == "l":
    for number in l_numbers:
        print("x" * number)
