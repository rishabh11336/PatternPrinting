N = int(input())

for i in range(N):
    for j in range(N):
        if i==j:
            print("*",end="")
        else:
            print("0",end="")
    print("*",end="")

    for k in range(N):
        if k == N-1-i:
            print("*",end="")
        else:
            print("0",end="")
    print()