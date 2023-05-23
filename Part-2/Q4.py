N = int(input())

for i in range(1,N+1):
    print(" "*(N-i),end="")
    a = i
    for j in range(i):
        print(a,end='')
        a += 1
    a -=2
    for k in range(i-1):
        print(a,end="")
        a -= 1
    print()