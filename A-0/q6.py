# reverse a given no


num = int(input("Enter the number to reverse it: "))

result = 0

while num:
  result = result*10 + num%10
  num = num//10

print(f"The reversed no is: {result}")
