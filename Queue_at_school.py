n, t = map(int, input().split())
queue = str(input())
while t>0:
    queue = queue.replace("BG","GB")
    t-=1
print(queue)