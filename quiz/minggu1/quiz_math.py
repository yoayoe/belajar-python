'''
Quiz 2: Operasi Matematika
-----------------------
Tujuan: Memahami operator matematika dasar di Python dan urutan operasi
'''

# Challenge 1: Operasi Matematika Dasar
# Buatlah variabel untuk dua angka, lalu lakukan operasi:
# - Penjumlahan
# - Pengurangan
# - Perkalian
# - Pembagian
# - Pembagian bulat (floor division)
# - Modulus (sisa bagi)
# - Pangkat

# Kode Anda di sini:
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("\n--- Hasil Operasi Matematika ---")
print(f"{angka1} + {angka2} = {angka1 + angka2}")  # Penjumlahan
print(f"{angka1} - {angka2} = {angka1 - angka2}")  # Pengurangan
print(f"{angka1} * {angka2} = {angka1 * angka2}")  # Perkalian
print(f"{angka1} / {angka2} = {angka1 / angka2}")  # Pembagian

# Konversi ke integer untuk operasi floor division dan modulus
if angka2 != 0:
    print(f"{angka1} // {angka2} = {angka1 // angka2}")  # Pembagian bulat
    print(f"{angka1} % {angka2} = {angka1 % angka2}")    # Modulus (sisa bagi)
else:
    print("Tidak bisa melakukan pembagian bulat dan modulus dengan nol")

print(f"{angka1} ** {angka2} = {angka1 ** angka2}")  # Pangkat

# Challenge 2: Urutan Operasi (PEMDAS)
# Hitunglah hasil dari ekspresi berikut dan tunjukkan langkah-langkahnya:
# 10 + 5 * 2 - 6 / 2

# Kode Anda di sini:
ekspresi = "10 + 5 * 2 - 6 / 2"
hasil = 10 + 5 * 2 - 6 / 2

print("\n--- Urutan Operasi (PEMDAS) ---")
print(f"Ekspresi: {ekspresi}")
print("Langkah-langkah:")
print("1. Evaluasi dalam kurung (Parentheses) - tidak ada kurung")
print("2. Evaluasi pangkat (Exponents) - tidak ada pangkat")
print("3. Evaluasi perkalian dan pembagian dari kiri ke kanan:")
print("   5 * 2 = 10")
print("   6 / 2 = 3")
print("4. Evaluasi penjumlahan dan pengurangan dari kiri ke kanan:")
print("   10 + 10 - 3 = 17")
print(f"Hasil: {hasil}")

# Bonus Challenge: Kalkulator Luas dan Keliling
# Buatlah program yang menghitung luas dan keliling:
# 1. Persegi
# 2. Persegi panjang
# 3. Lingkaran (gunakan pi = 3.14)

# Kode Anda di sini:
print("\n--- Kalkulator Luas dan Keliling ---")
bentuk = input("Pilih bentuk (persegi/persegi panjang/lingkaran): ").lower()

if bentuk == "persegi":
    sisi = float(input("Masukkan panjang sisi: "))
    luas = sisi ** 2
    keliling = 4 * sisi
    print(f"Luas persegi: {luas}")
    print(f"Keliling persegi: {keliling}")
    
elif bentuk == "persegi panjang":
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas persegi panjang: {luas}")
    print(f"Keliling persegi panjang: {keliling}")
    
elif bentuk == "lingkaran":
    jari_jari = float(input("Masukkan jari-jari: "))
    pi = 3.14
    luas = pi * (jari_jari ** 2)
    keliling = 2 * pi * jari_jari
    print(f"Luas lingkaran: {luas}")
    print(f"Keliling lingkaran: {keliling}")
    
else:
    print("Bentuk tidak valid!")