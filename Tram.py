a = int(input())
sum = 0
liste = list()
for i in range(a):
    a,b = map(int,input().split())
    sum += (b-a) 
    liste.append(sum)
print(max(liste))