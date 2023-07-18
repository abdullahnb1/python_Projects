a = int(input())
output = 0
for i in range(a):
    liste = list(map(int,input().split()))
    times = liste.count(1)
    if times >= 2:
        output += 1
    else:
        continue
print(output)