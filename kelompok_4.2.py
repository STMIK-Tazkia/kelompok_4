# Definisi himpunan
A = {3, 4, 5, 17, 2, 3, 5, 14, 3 , 10, 31, 22, 21, 45}
B = {4, 21, 5, 17, 2, 3, 6, 15, 6, 45, 20}

# Fungsi untuk irisan
def irisan(set_A, set_B):
    return set_A.intersection(set_B)

# Fungsi untuk beda setangkup
def beda_setangkup(set_A, set_B):
    return set_A.symmetric_difference(set_B)

# Fungsi peluang
def peluang(himpunan, semesta):
    return len(himpunan) / len(semesta)

# Menghitung irisan dan beda setangkup
irisan_himpunan = irisan(A, B)
beda_setangkup_himpunan = beda_setangkup(A, B)

# Menghitung peluang P(A) dan P(B)
semesta = A.union(B)  # Gabungan himpunan sebagai semesta
peluang_A = peluang(A, semesta)
peluang_B = peluang(B, semesta)

# Output hasil
print("Irisan (A ∩ B):", irisan_himpunan)
print("Beda setangkup (A Δ B):", beda_setangkup_himpunan)
print("Peluang P(A):", peluang_A)
print("Peluang P(B):", peluang_B)
