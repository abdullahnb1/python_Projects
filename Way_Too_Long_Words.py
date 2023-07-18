number = int(input())
for i in range(number):
    a  = str(input())
    if len(a) > 10:
        b = str(len(a) - 2)
    
        print(a[0] + b + a[:-2:-1])
    else: print(a)