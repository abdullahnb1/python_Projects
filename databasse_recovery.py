def reinstall(str):
    liste = str.split(" ")
    new_liste = list()
    dictionary = dict()
    for i in liste:
        if i == "|" or i == "|=|" or i == ":":
            pass
        else:
            i = i.lower().capitalize()
            new_liste.append(i)
    for i in range(len(new_liste)):
        if i % 2 == 0:
            dictionary[new_liste[i]] = int(new_liste[i+1])
    return dictionary
print(reinstall("| ahmet : 16 |=| Mehmet : 19 |=| selin : 32 |=| PINAR : 8 |"))