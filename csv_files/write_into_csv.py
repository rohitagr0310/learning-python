def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
    

a = input()

for char in a:
    number = ord(char)
    print(DecimalToBinary(number))