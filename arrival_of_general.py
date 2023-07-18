n = int(input())
liste = list(map(int,input().split(" ")))
max = max(liste)
min = min(liste)
max_i, min_i = 0,0

for i in range(len(liste)):
    if liste[i] == max:
        max_i = i
        break
for i in range(len(liste)):
    if liste[i] == min:
        min_i = i
        continue
if min_i > max_i:
    result = max_i + n - (min_i + 1)
else:
    result = max_i + n - (min_i+2)
print(result)
