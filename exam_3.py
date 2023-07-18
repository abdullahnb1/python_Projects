keyword_list = eval(input())
factor_list = eval(input())
liste = list()

for i in range(len(factor_list)):
    a = ""
    for j in keyword_list[i]:
        a += j*int(factor_list[i])
    liste.append(a)
output = "-".join(liste)

print(output)