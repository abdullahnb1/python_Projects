n = int(input())
result = 0
if n % 2 == 0:
    result = int(n/2)
else:
    result = int((n-1)/2 - n)
print(result)