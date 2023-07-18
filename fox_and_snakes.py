n,m = map(int,input().split(" "))
a = "#"
b = "."
satir = b*(m-1) + a
for i in range(n):
    liste = list()
    if i % 2 == 0:
        print(a*m)
    elif i%2 != 0:
        print(satir)
        satir = satir[::-1]
