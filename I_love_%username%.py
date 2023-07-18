n = int(input())
liste = list(map(int, input().split(" ")))
result = 0
for i in range(n-1):
    if liste[i+1] > liste[i]: result +=1
    else:
        a = liste[i] - liste[i+1]
        if a < 26: result+=1
        else: pass
    
    
print(result)