n = int(input())
liste_odd = list()
liste_even = list()
for i in range (n):
    if (i+1) == 1:
        liste_odd.append("I hate it")
    elif (i+1) % 2 == 0:
        if (i+1) == 2:
            liste_even.append("I hate that I love it")
        else:
            liste_even.insert(0,"I hate that I love that")
    else:
        liste_odd.insert(0,"I hate that I love that")
if n % 2 == 0:
    print(" ".join(liste_even))
else:
    print(" ".join(liste_odd))