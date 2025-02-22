
def Lexico(w):
    w = list(w)
    for i in range(len(w)//2):
        if(ord(w[i]) < ord(w[-(i+1)])):
            w[i], w[len(w) - i - 1] = w[len(w) - i - 1], w[i]
            return "".join(w)
    return "Not possible"       
            
        

T = int(input("1:"))



for i in range(T):
    N = input()
    print(Lexico(N))



