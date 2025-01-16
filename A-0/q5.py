# print table of any no

num = int(input("Enter the number that you want to find table of: "))

for x in range(10):
  print(f"{num} x {x+1} = {num*(x+1)}", sep="\n")