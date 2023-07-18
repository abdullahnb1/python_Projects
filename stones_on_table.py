sayı = int(input())
stones = str(input())
sum = 0
for i in range(sayı-1):
    if stones[i] == stones[i+1]: sum += 1
    else: continue
print(sum)