a = list(map(int,input().split()))

b = a[0]/1 * a[1]/2
c = a[0]/2 * a[1]/1
if b > c:
    print(int(b))
else: print(int(c))