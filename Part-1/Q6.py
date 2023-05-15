N = int(input())

for i in range(N):
    a = N-i+65-1
    for j in range(i+1):
        print(chr(a),end="")
        a += 1
    print()