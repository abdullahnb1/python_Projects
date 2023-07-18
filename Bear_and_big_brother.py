limak, bob = map(int, input().split())
sum = 0
while limak <= bob:
    sum += 1
    limak *= 3
    bob *= 2
    
print(sum)