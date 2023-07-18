a = str(input()); b = str(input()); c = str(input())
new_str = a+b

liste = list()
liste_2 = list()

for i in range(len(new_str)): liste.append(new_str[i])
for i in range(len(c)): liste_2.append(c[i])
    

liste.sort()
liste_2.sort()

if liste== liste_2: print("YES")    
else: print("NO")