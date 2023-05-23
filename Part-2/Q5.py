n = int(input())


N = int(n//2)+1
for i in range(1,N+1):
    print(" "*(N-i),end="")
    print("*"*((2*i)-1))
bn = int(n//2)
for j in range(0,bn):
    print(" "*(j+1),end="")
    print("*"*((2*(bn-j))-1))