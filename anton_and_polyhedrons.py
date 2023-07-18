n = int(input())
result = 0
for i in range(n):
    a = str(input())
    if a == "Tetrahedron": result += 4
    elif a == "Cube": result += 6
    elif a == "Octahedron": result += 8
    elif a == "Dodecahedron": result += 12
    else: result += 20
print(result)
    