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