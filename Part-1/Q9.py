N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(1)
    print(11)
else:
    print(1)
    print(11)
    for i in range(2,N):
        print(1,end="")
        for j in range(i-1):
            print(2,end="")
        print(1,end="")
        print()