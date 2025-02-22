
max = -1

T = int(input("1:"))

N = int(input("2:"))

for i in range(T, N + 1):
    for j in range(T, N + 1):
        if(max <= i^j):
            max = i^j
print( max ) 


