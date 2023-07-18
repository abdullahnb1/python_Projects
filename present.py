a = int(input()); b = list(map(int, input().split()))
p = list()
for i in range(1, a+1):
    c = b.index(i)+1
    p.append(str(c))
adana = " ".join(p)
print(adana)