n = int(input())
l_x = set(map(int,input().split()[1:]))
l_y = set(map(int,input().split()[1:]))

l_x.update(l_y)
 
if 0 in l_x:
    l_x.remove(0)
 
if len(l_x) == n:
    print("I become the guy.")
else: print("Oh, my keyboard!") 