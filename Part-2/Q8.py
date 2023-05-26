N = int(input())

for i in range(N):
    print(" "*(N-1-i),end="")
    for j in range(i+1,0,-1):
        print(j,end="")
    
    for k in range(2,i+2):
        print(k,end="")
    print()