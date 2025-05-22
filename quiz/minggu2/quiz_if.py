'''
Quiz 4: Percabangan (if-elif-else)
---------------------------------
Tujuan: Memahami percabangan kondisional di Python
'''

# Challenge 1: Menentukan Bilangan
# Buatlah program yang menerima input bilangan dan menentukan apakah
# bilangan tersebut positif, negatif, atau nol

# Kode Anda di sini:
print("=== Cek Jenis Bilangan ===")
bilangan = float(input("Masukkan sebuah bilangan: "))

if bilangan > 0:
    print(f"{bilangan} adalah bilangan positif")
elif bilangan < 0:
    print(f"{bilangan} adalah bilangan negatif")
else:
    print(f"{bilangan} adalah nol")

# Challenge 2: Kalkulator Sederhana
# Buatlah kalkulator sederhana yang dapat melakukan operasi
# penjumlahan, pengurangan, perkalian, dan pembagian berdasarkan pilihan pengguna

# Kode Anda di sini:
print("\n=== Kalkulator Sederhana ===")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operasi = input("Pilih operasi (+, -, *, /): ")

if operasi == "+":
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
elif operasi == "-":
    hasil = angka1 - angka2
    print(f"{angka1} - {angka2} = {hasil}")
elif operasi == "*":
    hasil = angka1 * angka2
    print(f"{angka1} * {angka2} = {hasil}")
elif operasi == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"{angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan")
else:
    print("Operasi tidak valid!")

# Challenge 3: Menentukan Tahun Kabisat
# Buatlah program untuk menentukan apakah sebuah tahun adalah tahun kabisat
# Tahun kabisat adalah:
# - Habis dibagi 4 tetapi tidak habis dibagi 100, ATAU
# - Habis dibagi 400

# Kode Anda di sini:
print("\n=== Cek Tahun Kabisat ===")
tahun = int(input("Masukkan tahun: "))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")

# Bonus Challenge: Penentu Hari dalam Bulan
# Buatlah program yang menerima input bulan dan tahun,
# lalu menampilkan jumlah hari dalam bulan tersebut
# (Perhatikan tahun kabisat untuk bulan Februari)

# Kode Anda di sini:
print("\n=== Jumlah Hari dalam Bulan ===")
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

if bulan < 1 or bulan > 12:
    print("Bulan tidak valid!")
else:
    # Cek tahun kabisat
    is_kabisat = (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)
    
    # Tentukan jumlah hari berdasarkan bulan
    if bulan == 2:  # Februari
        if is_kabisat:
            hari = 29
        else:
            hari = 28
    elif bulan in [4, 6, 9, 11]:  # April, Juni, September, November
        hari = 30
    else:  # Januari, Maret, Mei, Juli, Agustus, Oktober, Desember
        hari = 31
    
    nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                  "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    print(f"{nama_bulan[bulan-1]} {tahun} memiliki {hari} hari")