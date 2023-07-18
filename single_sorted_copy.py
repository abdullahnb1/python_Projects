def single_sorted_copy(liste):
    new_liste = list()
    for i in liste:
        if i in new_liste:
            pass
        else:
            new_liste.append(i)
    return sorted(new_liste)
print(single_sorted_copy([1, 3, 2, 2, 1, 1, 4]))