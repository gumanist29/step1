N = int(input())

if N%2==0 and 6<=N<=20:
    print("Weird")
elif N%2!=0 and 2<=N<=5:
    print("Weird")
elif N%2!=0:
    print("Weird")
else:
    print("Not Weird")
