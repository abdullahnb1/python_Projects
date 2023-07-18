a = input()
max = list()
min = list()
for i in a:
    if ord(i)>64 and ord(i)<97:
        max.append(i)
    else: min.append(i)
if len(max) <= len(min):
    print(a.lower())
else:print(a.upper())