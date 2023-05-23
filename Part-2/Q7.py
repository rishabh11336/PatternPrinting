N = int(input())

for i in range(N):
    print("0"*i,end="")
    print("*",end="")
    print("0"*(N-1-i),end="")
    print("*",end="")
    print()