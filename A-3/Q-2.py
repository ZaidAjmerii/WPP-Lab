def is_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

# Read input
T = int(input("Enter the value of T: "))  # Number of test cases
for x in range(T):
    N = int(input(f"Enter the value of {x} Number: "))  # Read each test case normally
    if is_fibonacci(N):
        print("IsFibo")
    else:
        print("IsNotFibo")
