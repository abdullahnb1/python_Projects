first_str = str(input()).upper()
second_str = str(input()).upper()

liste_1 = list()
liste_2 = list()

for i in first_str:
    liste_1.append(i)
for j in second_str:
    liste_2.append(j)
    
sum = 0
for i in range(len(liste_1)):
    if liste_1[i] != liste_2[i]:
        
        if liste_1[i] < liste_2[i]:
            sum = -1
            break
        elif liste_1[i] > liste_2[i]:
            sum = 1
            break
    else: continue
print(sum)

