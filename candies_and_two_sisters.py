n = int(input())
liste = list()
for i in range(n):
    n = int(input())
    if n == 1 or n == 2: liste.append(0)
    else:
        if n % 2 == 0: liste.append(n//2 - 1)
        else: liste.append(n//2)
for i in range(len(liste)):
    print(liste[i])