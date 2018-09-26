t = int(input())
for v in range (t):
    a = 0
    n = int(input())
    b = [int(x) for x in input().split()]
    for i in range(int(n/2)):
        if b[i]<b[i+1] and b[n-i-1]<b[n-i-2]:
            print("No")
            a = 1
            break
        else:
            continue
    if a != 1:
        print("Yes")

