"""
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
"""

"""
# Bagian 2 nomor 2
# Definisikan himpunan A dan B
A = {37, 41, 50, 17, 22, 3, 5, 14, 3, 19}
B = {41, 12, 56, 17, 21, 3, 50, 15, 6, 4, 20}

# Buat fungsi untuk mengambil irisan dari dua himpunan 
def irisan_himpunan(set1, set2):
    return set1.intersection(set2)

# Panggil fungsi dan cetak hasilnya 
hasil = irisan_himpunan(A, B)
print("Irisan dari himpunan A dan B adalah:", hasil)
"""

# Bagian 3
## Soal 1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Himpunan A
A = [109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 21, 378, 400, 101, 201, 301, 1]

# Mengurutkan himpunan A
sorted_A = bubble_sort(A)
print("Himpunan A setelah diurutkan:", sorted_A)

## Soal 2
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1 # Jika x tidak ditemukan

# Nilai yang dicari
x = 300

# Mencari nilai x dalam himpunan A
index_x = linear_search(A, x)
if index_x != -1:
    print(f"nilai {x} ditemukan pada indeks ke-{index_x}")
else:
    print(f"nilai {x} tidak ditemukan dalam himpunan A")

### Hasil Gabungan
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1 # Jika x tidak ditemukan

# Himpunan A
A = [109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 21, 378, 400, 101, 201, 301, 1]

# Mengurutkan himpunan A
sorted_A = bubble_sort(A)
print("Himpunan A setelah diurutkan:", sorted_A)

# Nilai yang dicari
x = 300

# Mencari nilai x dalam himpunan A
index_x = linear_search(A, x)
if index_x != -1:
    print(f"nilai {x} ditemukan pada indeks ke-{index_x}")
else:
    print(f"nilai {x} tidak ditemukan dalam himpunan A")