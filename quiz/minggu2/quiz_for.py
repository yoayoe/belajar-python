'''
Quiz 5: Perulangan dengan For Loop
---------------------------------
Tujuan: Memahami perulangan for dan range di Python
'''

# Challenge 1: Cetak Angka
# Buatlah program yang mencetak angka dari 1 hingga n (input pengguna)
# menggunakan for loop dan range

# Kode Anda di sini:
print("=== Cetak Angka 1 sampai n ===")
n = int(input("Masukkan nilai n: "))

print("Hasil:")
for i in range(1, n + 1):
    print(i, end=" ")
print()  # Baris baru

# Challenge 2: Hitung Jumlah dan Rata-rata
# Buatlah program yang menerima n angka dari pengguna,
# lalu menghitung jumlah dan rata-rata angka tersebut

# Kode Anda di sini:
print("\n=== Hitung Jumlah dan Rata-rata ===")
n = int(input("Berapa banyak angka yang ingin diinput? "))

jumlah = 0
for i in range(n):
    angka = float(input(f"Masukkan angka ke-{i+1}: "))
    jumlah += angka

if n > 0:
    rata_rata = jumlah / n
    print(f"Jumlah: {jumlah}")
    print(f"Rata-rata: {rata_rata}")
else:
    print("Tidak ada angka yang diinput")

# Challenge 3: Pola Bintang
# Buatlah program yang menampilkan pola bintang segitiga
# dengan tinggi sesuai input pengguna

# Kode Anda di sini:
print("\n=== Pola Bintang ===")
tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    print("*" * i)

# Challenge 4: Iterasi String
# Buatlah program yang menerima sebuah string,
# lalu mencetak setiap karakter dalam string tersebut
# beserta indeksnya

# Kode Anda di sini:
print("\n=== Iterasi String ===")
teks = input("Masukkan sebuah teks: ")

print("Karakter dalam teks:")
for i in range(len(teks)):
    print(f"Indeks {i}: '{teks[i]}'")

# Cara alternatif menggunakan enumerate
print("\nCara alternatif dengan enumerate:")
for i, karakter in enumerate(teks):
    print(f"Indeks {i}: '{karakter}'")

# Bonus Challenge: Tabel Perkalian
# Buatlah program yang menampilkan tabel perkalian
# dari 1 hingga n (input pengguna)

# Kode Anda di sini:
print("\n=== Tabel Perkalian ===")
n = int(input("Masukkan n untuk tabel perkalian (1-n): "))

# Cetak header
print("\n      ", end="")
for i in range(1, n + 1):
    print(f"{i:4}", end="")
print("\n" + "-" * (6 + 4 * n))

# Cetak tabel perkalian
for i in range(1, n + 1):
    print(f"{i:4} | ", end="")
    for j in range(1, n + 1):
        print(f"{i*j:4}", end="")
    print()