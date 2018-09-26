from itertools import combinations

n = int(input());
a = input().split(); 
b = int(input())
c = list(combinations(a,b))
result = [1 for i in range(len(c)) if 'a' in c[i]]
print(sum(result)/len(c))

