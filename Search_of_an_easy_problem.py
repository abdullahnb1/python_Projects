a = int(input()); b = list(map(int,input().split()))
easy = 0; hard = 0
for i in range(a):
    if b[i] == 1: hard += 1
    else: easy += 1
if hard >= 1: print("HARD")
else: print("EASY")