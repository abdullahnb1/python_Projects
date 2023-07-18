a = input()
liste = list()

for i in range(len(a)):
    liste.append(a[i])
length = len(liste)
if length % 2 == 0:
    mid = int((length-2)/2)
    print(a[mid:mid+2])
else:
    mid = int((length-1)/2)
    print(a[mid])

    
    