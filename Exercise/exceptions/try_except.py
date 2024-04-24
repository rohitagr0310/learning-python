try:
    age = int(input("Enter your age - "))

    income = int(input("Enter incone - "))
    risk = income / age

    print(f"age is {age}")
    print(f"risk is {risk}")

except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
    print("Invalid Value")

# it returns the coder defind error message in case of in build message
