n = int(input())
liste = list(map(int,input().split(" ")))
result,a  = 0,0

police = list()
for i in range(n):
    if liste[i] > 0: 
        a += liste[i]
    else:
        if a == 0:
            result += 1
        else:
            a-= 1
print(result)