N = int(input())

for i in range(N):
    if i==0 or i==N-1:
        print("*",end="")
    else:
        if i<(N//2)+1:
            print(" "*i,end="")
            print("* "*(i+1), end="")
        else:
            print(" "*(N-i-1), end="")
            print("* "*(N-i),end="")
    print()