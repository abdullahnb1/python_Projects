n = int(input())
liste = list()
for i in range(n):
    a,b = map(int,input().split())
    if b > a:
        liste.append(b-a)
    else:
        if a%b == 0:
            liste.append(0)
        else:
            result = (((a // b)+1) * b) - a
            liste.append(result)
for i in liste:
    print(i)