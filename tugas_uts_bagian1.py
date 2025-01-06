# Bagian 1 nomor 2
# Mendefinisikan fungsi untuk perkalian matriks
def matrix_multiplication(A, B):
    # Menginisialisasi matriks hasil perkalian
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # melakukan perkalian matriks
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Matriks C
C = [
    [44, 55, 34, 10],
    [33, 5, 75, 13],
    [21, 7, 21, 11],
    [33, 88, 32, 15]
]

# Matriks D
D = [
    [1, 8, 1, 1],
    [0, 1, 7, 0],
    [0, 7, 1, 0],
    [1, 8, 1, 1]
]

# Menghitung hasil perkalian C x D
result = matrix_multiplication(C, D)

# Menampilkan hasilnya
for row in result:
    print(row)