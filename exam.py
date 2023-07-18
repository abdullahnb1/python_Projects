sayi = eval(input())
liste = list()
for i in range(len(sayi)):
    x = int(sayi[i])
    liste.append(x)
a = float(input())
d_t = liste[0]

for i in range(1, len(liste)):
    d_t = float(liste[i]*a + (1-a)*d_t)
print('%.2f' % d_t)
