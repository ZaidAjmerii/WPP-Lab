# same as 2

num = int(input("Enter the number you want to find factorial of: "))

result = 1

for x in range(num):
  result = result*(x+1)


print(f"The factorial of {num} is {result}")