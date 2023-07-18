f_n = str(input())
s_n = str(input())

string = ""
for i in range(len(f_n)):
    if f_n[i] == s_n[i]:
        string += "0"
    else:
        string += "1"
print(string)