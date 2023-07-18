def capitalize_letter(str):
    liste = str.split(" ")
    n = 0
    for i in liste:
        liste[n] = i.capitalize()
        n += 1
    return " ".join(liste)
print(capitalize_letter('lorem. ipsum? dolor sit amet, consectetur! adipiscing elit.'))