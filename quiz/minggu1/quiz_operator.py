'''
Quiz 3: Operator Perbandingan dan Logika
--------------------------------------
Tujuan: Memahami operator perbandingan dan logika di Python
'''

# Challenge 1: Operator Perbandingan
# Buatlah program yang membandingkan dua angka menggunakan semua operator perbandingan:
# ==, !=, >, <, >=, <=

# Kode Anda di sini:
print("=== Operator Perbandingan ===")
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

print(f"{a} == {b}: {a == b}")  # Sama dengan
print(f"{a} != {b}: {a != b}")  # Tidak sama dengan
print(f"{a} > {b}: {a > b}")    # Lebih besar dari
print(f"{a} < {b}: {a < b}")    # Lebih kecil dari
print(f"{a} >= {b}: {a >= b}")  # Lebih besar atau sama dengan
print(f"{a} <= {b}: {a <= b}")  # Lebih kecil atau sama dengan

# Challenge 2: Operator Logika (and, or, not)
# Buatlah program yang menggunakan operator logika untuk menentukan:
# - Apakah seseorang berhak mendapatkan diskon (jika umur < 12 atau umur > 65)
# - Apakah seseorang dapat masuk ke permainan (jika tinggi > 120 cm dan umur > 8)

# Kode Anda di sini:
print("\n=== Operator Logika ===")
umur = int(input("Masukkan umur Anda: "))
tinggi = float(input("Masukkan tinggi Anda (cm): "))

# Cek eligibilitas diskon
berhak_diskon = umur < 12 or umur > 65
print(f"Berhak mendapatkan diskon: {berhak_diskon}")

# Cek eligibilitas permainan
boleh_main = tinggi > 120 and umur > 8
print(f"Dapat masuk ke permainan: {boleh_main}")

# Gunakan operator not
tidak_berhak_diskon = not berhak_diskon
print(f"Tidak berhak mendapatkan diskon: {tidak_berhak_diskon}")

# Challenge 3: Kombinasi Operator
# Buatlah program yang mengkombinasikan operator perbandingan dan logika
# untuk menentukan apakah sebuah angka berada di dalam rentang tertentu

# Kode Anda di sini:
print("\n=== Rentang Nilai ===")
nilai = float(input("Masukkan nilai (0-100): "))

# Cek apakah nilai dalam rentang 0-100
valid = 0 <= nilai <= 100
print(f"Nilai valid (0-100): {valid}")

# Tentukan grade berdasarkan rentang nilai
if nilai >= 90 and nilai <= 100:
    grade = "A"
elif nilai >= 80 and nilai < 90:
    grade = "B"
elif nilai >= 70 and nilai < 80:
    grade = "C"
elif nilai >= 60 and nilai < 70:
    grade = "D"
elif nilai >= 0 and nilai < 60:
    grade = "E"
else:
    grade = "Nilai tidak valid"

print(f"Grade: {grade}")

# Bonus Challenge: Kalkulator Logika
# Buatlah program sederhana yang menghitung hasil dari operasi logika
# dari dua input boolean

# Kode Anda di sini:
print("\n=== Kalkulator Logika ===")
print("Masukkan True atau False")
bool1_str = input("Input boolean pertama: ").lower()
bool2_str = input("Input boolean kedua: ").lower()

# Konversi string ke boolean
bool1 = bool1_str == "true"
bool2 = bool2_str == "true"

print(f"{bool1} AND {bool2} = {bool1 and bool2}")
print(f"{bool1} OR {bool2} = {bool1 or bool2}")
print(f"NOT {bool1} = {not bool1}")
print(f"NOT {bool2} = {not bool2}")
print(f"{bool1} XOR {bool2} = {bool1 != bool2}")  # XOR implementation