
def numberOfPiece(n):
    if(n%2==0):
        return (n//2)**2
    else:
        return (n//2)*((n//2) + 1)

T = int(input("1:"))



for i in range(T):
    N = int(input())
    print(numberOfPiece(N))

