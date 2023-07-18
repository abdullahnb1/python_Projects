n = int(input())
liste = list()
result = 0
for i in range(n):
    team = list(map(str,input().split(" ")))
    liste.append(team)

for i in range(n):
    team = liste[i]
    home = liste[i][0]
    guest = liste[i][1]
    liste.remove(liste[i])
    for j in range(len(liste)):
        guest = liste[j][1]
        if str(home) == str(guest):
            result += 1
        else: pass
    liste.insert(0,team)
print(result)
