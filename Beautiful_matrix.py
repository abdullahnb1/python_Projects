liste = [[],[],[],[],[]]
for i in range(5):
    liste[i] = list(map(int,input().split()))

for i in range(5):
    a = liste[i]
    for j in range(5):
        b = a[j]
        if b == 1:
            row = abs(2-j)
            column = abs(2-i)
            print(row + column)