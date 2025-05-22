'''
Quiz 6: Perulangan dengan While Loop
-----------------------------------
Tujuan: Memahami perulangan while di Python
'''

# Challenge 1: Hitung Mundur
# Buatlah program yang melakukan hitung mundur dari n hingga 1
# menggunakan while loop

# Kode Anda di sini:
print("=== Hitung Mundur ===")
n = int(input("Masukkan nilai awal hitung mundur: "))

print("Hitung mundur dimulai:")
while n > 0:
    print(n, end=" ")
    n -= 1
print("\nSelesai!")

# Challenge 2: Tebak Angka
# Buatlah permainan tebak angka sederhana:
# - Program memilih angka acak dari 1-100
# - Pemain menebak angka tersebut
# - Program memberikan petunjuk "terlalu besar" atau "terlalu kecil"
# - Program berhenti jika tebakan benar

# Kode Anda di sini:
import random
print("\n=== Permainan Tebak Angka ===")
print("Saya telah memilih angka dari 1-100. Coba tebak!")

angka_rahasia = random.randint(1, 100)
tebakan = 0
jumlah_tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebakan Anda: "))
    jumlah_tebakan += 1
    
    if tebakan < angka_rahasia:
        print("Terlalu kecil, coba lagi.")
    elif tebakan > angka_rahasia:
        print("Terlalu besar, coba lagi.")
    else:
        print(f"Selamat! Anda berhasil menebak angka {angka_rahasia}")
        print(f"Anda membutuhkan {jumlah_tebakan} kali tebakan")

# Challenge 3: Validasi Input
# Buatlah program yang meminta pengguna memasukkan angka positif
# Program terus meminta sampai pengguna memasukkan angka yang valid

# Kode Anda di sini:
print("\n=== Validasi Input ===")
angka_valid = False

while not angka_valid:
    try:
        angka = float(input("Masukkan angka positif: "))
        if angka > 0:
            angka_valid = True
            print(f"Terima kasih! Anda memasukkan angka positif: {angka}")
        else:
            print("Error: Angka harus positif.")
    except ValueError:
        print("Error: Input harus berupa angka.")

# Challenge 4: Kalkulator dengan Menu
# Buatlah kalkulator sederhana dengan menu:
# 1. Penjumlahan
# 2. Pengurangan
# 3. Perkalian
# 4. Pembagian
# 0. Keluar
# Program terus berjalan sampai pengguna memilih keluar

# Kode Anda di sini:
print("\n=== Kalkulator dengan Menu ===")
running = True

while running:
    print("\nMenu Kalkulator:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("0. Keluar")
    
    pilihan = input("Pilih operasi (0-4): ")
    
    if pilihan == "0":
        running = False
        print("Terima kasih telah menggunakan kalkulator ini!")
    elif pilihan in ["1", "2", "3", "4"]:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        
        if pilihan == "1":
            print(f"Hasil: {a} + {b} = {a + b}")
        elif pilihan == "2":
            print(f"Hasil: {a} - {b} = {a - b}")
        elif pilihan == "3":
            print(f"Hasil: {a} * {b} = {a * b}")
        elif pilihan == "4":
            if b != 0:
                print(f"Hasil: {a} / {b} = {a / b}")
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Bonus Challenge: Fibonacci dengan While
# Buatlah program yang menampilkan deret Fibonacci hingga suku ke-n
# menggunakan while loop (deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...)

# Kode Anda di sini:
print("\n=== Deret Fibonacci ===")
n = int(input("Masukkan jumlah suku Fibonacci yang diinginkan: "))

# Inisialisasi suku-suku awal
a, b = 0, 1
count = 0

print("Deret Fibonacci:")
while count < n:
    print(a, end=" ")
    # Update nilai untuk suku berikutnya
    temp = a + b
    a = b
    b = temp
    count += 1