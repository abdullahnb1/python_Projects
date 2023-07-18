a = input().split()

number = int(a[0])
times = int(a[1])
for i in range(times):
    if number % 10 == 0:
        number /= 10
    else:
        number -= 1
print(int(number))