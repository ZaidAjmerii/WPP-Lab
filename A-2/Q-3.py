# You are given a number N, you need to print the number of positions where digits exactly
# divides N.

# Input number of test cases
T = int(input("Enter the number of test cases (1 <= T <= 15): "))
while T < 1 or T > 15:
    print("Invalid input. T must be between 1 and 15.")
    T = int(input("Enter the number of test cases (1 <= T <= 15): "))

N = []


for x in range(T):
    n = input(f"Enter the value of N[{x}] (0 <= N <= 10^10): ")
    N.append(n)

for x in range(T):
  temp = 0
  for y in N[x]:
    if y != '0' and int(N[x]) % int(y) == 0:
      temp += 1
  
  print(F"{temp} digits in the number {N[x]} divide the number exactly.")
