n = int(input()) ; str = str(input())
liste = list()
kelimeler = list()
for i in range(n):
    if str[i] == str[i].upper():
        if len(liste)!= 0: 
            kelime = str[liste[-1]:i]
            kelimeler.append(kelime)
            liste.append(i)
        else:
            kelime = str[0:i]
            kelimeler.append(kelime)
            liste.append(i)
if len(liste) == 0:
    kelimeler.append(str)
else:
    kelimeler.append(str[liste[-1]:n])

result = "No"
for i in kelimeler:
    a = kelimeler.count(i)
    if a > 1:
        result = "Yes"
print(result)
