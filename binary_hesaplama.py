a = int(input())
binary_output = ""
while a >= 1:
    if a%2 == 0: binary_output += "0"
    else: binary_output += "1"
    a = int(a/2)
print(int(binary_output[::-1]))