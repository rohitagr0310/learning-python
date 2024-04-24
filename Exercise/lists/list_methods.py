numbers = [5, 2, 1, 5, 5, 7, 4]
numbers2 = numbers.copy()

print("Frequency of 5:", numbers.count(5))

print("Is 50 present in list:", 50 in numbers)

numbers.sort()
print("Sorted list:", numbers)

numbers.sort(reverse=True)
print("Reverse sorted lise:", numbers)

numbers.append(20)
print("Adding 20 at the end of the list:", numbers)

numbers.pop()
print("Removing last number from the list:", numbers)

numbers.insert(0, 10)
print("Inserting number at the beginning of the list:", numbers)

numbers.clear()
print("Complete clear the list:", numbers)

print("The original listt:", numbers2)
