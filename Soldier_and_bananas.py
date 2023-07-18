k, n, w = map(int, input().split())
sum = 0
for i in range(w):
    sum += (i+1)*k
loan = sum - n
if loan > 0: print(loan)
else: print(0)