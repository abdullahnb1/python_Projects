a = int(input())
liste = list()
result = 1
for i in range(a):
    b = int(input())
    liste.append(b)
for i in range(a-1):
    if liste[i] == liste[i+1]:
        pass
    else:
        result += 1
print(result)