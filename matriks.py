import numpy as np

# cara membuat matriks manual
matriks = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# dengan numpy
matriks2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# deklarasi array dgn default value
matriks3 = [[0 for j in range(4)] for i in range(3)] # angka 4 sbg kolom(m) dan 3 sbg baris(n)
# print(matriks3)

# cara mengakses matriks index baris dan kolomnya dimulai dari 0, spt array
# nama_matriks[baris][kolom]
var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
print(var_mat[1][3])

# matriks 2x2
# perkalian matriks dgn konstanta
var_matt = [[5, 0],
            [1, -2]]
def_matt = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_matt)):
    for j in range(len(var_matt[0])):
        def_matt[i][j] = var_matt[i][j] * 2

print(def_matt)

# perkalian matriks dgn konstanta dgn cara nge cheat
var_mattt = np.array([[5, 0],[1, -2]])
result = var_mattt*2
print(result)