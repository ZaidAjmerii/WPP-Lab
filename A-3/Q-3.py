def utopian_tree(n):
    height = 1  # Initial height of the tree
    for cycle in range(n):
        if cycle % 2 == 0:  # Monsoon (even cycles) -> height doubles
            height *= 2
        else:  # Summer (odd cycles) -> height increases by 1
            height += 1
    return height

# Read input
T = int(input("Enter the value of T: "))  # Number of test cases
for x in range(T):
    N = int(input(f"Enter the value of {x} Number: "))  # Number of cycles
    print(utopian_tree(N))
