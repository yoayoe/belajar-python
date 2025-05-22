'''
Quiz 1: Variabel dan Tipe Data
----------------------------
Tujuan: Mempelajari tentang variabel dan tipe data dasar di Python
'''

# Challenge 1: Buat variabel untuk menyimpan informasi pribadi
# Buatlah variabel untuk menyimpan nama, umur, tinggi (dalam meter), dan status_mahasiswa (boolean)
# Kemudian cetak semua informasi dengan format yang rapi

# Kode Anda di sini:
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
tinggi = float(input("Masukkan tinggi Anda (meter): "))
status_str = input("Apakah Anda seorang mahasiswa? (ya/tidak): ")
status_mahasiswa = status_str.lower() == "ya"

# Output dengan format
print("\n--- Informasi Pribadi ---")
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Tinggi: {tinggi} meter")
print(f"Status Mahasiswa: {'Ya' if status_mahasiswa else 'Tidak'}")
print(f"Tipe data nama: {type(nama)}")
print(f"Tipe data umur: {type(umur)}")
print(f"Tipe data tinggi: {type(tinggi)}")
print(f"Tipe data status: {type(status_mahasiswa)}")

# Challenge 2: Konversi tipe data
# Konversikan string "10" menjadi integer dan string "3.14" menjadi float
# Kemudian jumlahkan kedua nilai tersebut dan cetak hasilnya

# Kode Anda di sini:
string_angka1 = "10"
string_angka2 = "3.14"

angka1 = int(string_angka1)
angka2 = float(string_angka2)

hasil = angka1 + angka2

print("\n--- Hasil Konversi dan Operasi ---")
print(f"String 1: {string_angka1}, Tipe: {type(string_angka1)}")
print(f"String 2: {string_angka2}, Tipe: {type(string_angka2)}")
print(f"Setelah konversi - Angka 1: {angka1}, Tipe: {type(angka1)}")
print(f"Setelah konversi - Angka 2: {angka2}, Tipe: {type(angka2)}")
print(f"Hasil penjumlahan: {hasil}, Tipe: {type(hasil)}")

# Bonus Challenge: Buatlah variabel untuk menyimpan alamat email
# Kemudian pisahkan nama pengguna dan domain dari email tersebut

# Kode Anda di sini:
email = input("\nMasukkan alamat email Anda: ")
parts = email.split('@')

if len(parts) == 2:
    username = parts[0]
    domain = parts[1]
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Format email tidak valid!")