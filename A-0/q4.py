# swap two numbers without the 3rd variable

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

num1 = num1 - num2

num2 = num2 + num1

num1 = num2 - num1

print(f"Swapped No1: {num1} Swapped No2: {num2}")