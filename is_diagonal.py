def is_diagonal(matrix):
    n = len(matrix)
    liste = list()
    for i in range(n):
        liste.append(matrix[i][i])
    count = liste.count(liste[0])
    if count == 3 and liste[0] != 0:
        return True
    else:
        return False
print(is_diagonal([[1,1,1],[2,4,0],[3,3,3]]))