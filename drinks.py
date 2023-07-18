n = int(input())
b = list(map(int, input().split(" ")))
result = 0
for i in b:
    result += int(i)
print(result/n)