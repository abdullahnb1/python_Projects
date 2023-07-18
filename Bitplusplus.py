a = int(input())
sum = 0
for i in range(a):
    process = str(input())
    liste = list()
    for i in process:
        liste.append(i)
    if "+" in liste: 
        sum += 1
    else: 
        sum -= 1
    liste.clear()
print(sum)