phone = input("Phone No. : ")

digit_mapping = {
    "1": "One",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

output = ""
for number in phone:
    output += digit_mapping.get(number, "!") + " "

print(output)
