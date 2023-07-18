a = int(input())
b = str(input()).upper()
danik = 0 
anton = 0
for i in range(a):
    if b[i] == "D": danik += 1
    elif b[i] == "A": anton += 1
if anton > danik: 
    print("Anton")
elif danik > anton: 
    print("Danik")
else: 
    print("Friendship")