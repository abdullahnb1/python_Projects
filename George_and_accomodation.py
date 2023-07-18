a = int(input())
sum = 0
for i in range(a):
    a, b = map(int, input().split())
    if b-a >= 2: sum+=1
    else: continue
print(sum)