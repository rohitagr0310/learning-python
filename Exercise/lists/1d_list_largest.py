numbers = [8, 9, 7, 6, 4, 5, 1, 3, 2]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(f"Largest number in list is {max}")
