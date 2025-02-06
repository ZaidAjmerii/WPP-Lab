# 2. Sherlock and Squares
# isinstance()
# num**0.5


T = int(input("Enter the value of T(0 <=T <=10): "))

pairs = []  # List to store pairs

for _ in range(T):
  pair = (list(map(int, input("Enter two numbers separated by space: ").split())))
  pairs.append(pair)

count = 0

for x in range(T):
  for y in range(int(pairs[x][0]), int(pairs[x][1] + 1)):
    if(y**0.5 % 1 == 0):
      count = count + 1
    
  print(count)
  count = 0
 