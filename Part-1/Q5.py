N = int(input())

for i in range(N):
    a = i+65
    for j in range(i+1):
        print(chr(a),end="")
        a += 1
    print()