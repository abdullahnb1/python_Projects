a = list(map(int,input().split()))
finalist = list()
contestants = list(map(int,input().split()))

for i in range(a[0]):
    if contestants[i] > 0 and contestants[i] >= contestants[a[1]-1]: finalist.append(contestants[i])
    else: continue
if len(finalist) > 0:
    print(len(finalist))
else:
    print(0)