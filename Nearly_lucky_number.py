a = str(input())
sum = 0
for i in a:
    if i == "4" or i == "7": sum += 1
    else:continue
if sum == 7 or sum == 4: print("YES")
else: print("NO")