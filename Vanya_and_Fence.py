a,b = map(int,input().split())
row = 0
heights = list(map(int,input().split()))
for i in heights:
    if i > b:row += 2
    else: row += 1
print(row)