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