if __name__ == '__main__':
    f=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        f.append([score,name])
f.sort()
k=0
for x in range(n):
    if f[x][0]>f[0][0]:
        k=x
        break
for x in range(n):
    if f[k][0]==f[x][0]:
        print(f[x][1])

