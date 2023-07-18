a = int(input())
liste = list()
for i in range(a):
    b = str(input())
    b += b[::-1]
    liste.append(b)

for i in range(a):
    print(liste[i])