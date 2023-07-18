n = input()
chars = set()
for i in n:
    if i == "{" or i == "}" or i == " " or i == ",":
        pass
    else:
        chars.update(i)
print(len(chars))