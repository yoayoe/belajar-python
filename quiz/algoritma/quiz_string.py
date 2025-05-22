'''
Quiz Algoritma: Pengolahan String
--------------------------------
Tujuan: Memahami manipulasi string dan penggunaan struktur kendali

Soal:
Buatlah program yang mengolah string dengan berbagai cara:
1. Membalik string tanpa menggunakan fungsi bawaan
2. Menghitung frekuensi kemunculan setiap karakter
3. Memeriksa apakah string merupakan palindrome
4. Mengubah kasus huruf (uppercase, lowercase, atau title case)
'''

# Challenge 1: Membalik String
# Buatlah fungsi untuk membalik string tanpa menggunakan fungsi bawaan seperti reverse

# Kode Anda di sini:
print("=== Membalik String ===")
teks = input("Masukkan string yang ingin dibalik: ")

# Metode 1: Menggunakan slicing
reversed_teks1 = teks[::-1]
print(f"Hasil dengan slicing: {reversed_teks1}")

# Metode 2: Implementasi manual (tanpa slicing)
reversed_teks2 = ""
for i in range(len(teks) - 1, -1, -1):
    reversed_teks2 += teks[i]
print(f"Hasil implementasi manual: {reversed_teks2}")

# Challenge 2: Menghitung Frekuensi Karakter
# Buatlah program yang menghitung frekuensi kemunculan setiap karakter dalam string

# Kode Anda di sini:
print("\n=== Frekuensi Karakter ===")
teks = input("Masukkan string untuk dihitung frekuensinya: ")

# Menggunakan dictionary untuk menyimpan frekuensi
frekuensi = {}
for karakter in teks:
    if karakter in frekuensi:
        frekuensi[karakter] += 1
    else:
        frekuensi[karakter] = 1

# Menampilkan hasil
print(f"String: {teks}")
print("Frekuensi karakter:")
for karakter, jumlah in sorted(frekuensi.items()):
    print(f"'{karakter}': {jumlah}")

# Challenge 3: Palindrome Checker
# Buatlah program untuk memeriksa apakah string merupakan palindrome
# (sama jika dibaca dari depan maupun belakang)

# Kode Anda di sini:
print("\n=== Palindrome Checker ===")
teks = input("Masukkan string untuk diperiksa: ")

# Menghapus spasi dan mengubah ke huruf kecil
teks_clean = ''.join(teks.lower().split())

# Memeriksa palindrome
is_palindrome = teks_clean == teks_clean[::-1]

# Menampilkan hasil
print(f"String original: {teks}")
print(f"String setelah dihapus spasi dan huruf kecil: {teks_clean}")
if is_palindrome:
    print("Ini adalah palindrome!")
else:
    print("Ini bukan palindrome.")

# Challenge 4: Manipulasi Kasus Huruf
# Buatlah program untuk mengubah kasus huruf sesuai pilihan pengguna

# Kode Anda di sini:
print("\n=== Manipulasi Kasus Huruf ===")
teks = input("Masukkan string: ")
pilihan = input("Pilih konversi (upper/lower/title): ").lower()

if pilihan == "upper":
    hasil = teks.upper()
    print(f"Uppercase: {hasil}")
elif pilihan == "lower":
    hasil = teks.lower()
    print(f"Lowercase: {hasil}")
elif pilihan == "title":
    hasil = teks.title()
    print(f"Title case: {hasil}")
else:
    print("Pilihan tidak valid. Gunakan 'upper', 'lower', atau 'title'.")

# Bonus Challenge: Caesar Cipher
# Implementasikan algoritma Caesar Cipher sederhana
# Caesar Cipher menggeser setiap karakter dalam teks sejumlah posisi tertentu

# Kode Anda di sini:
print("\n=== Bonus: Caesar Cipher ===")
teks = input("Masukkan plaintext: ")
shift = int(input("Masukkan nilai pergeseran (1-25): "))

encrypted = ""
for char in teks:
    # Memproses hanya karakter alfabet
    if char.isalpha():
        # Mendapatkan kode ASCII
        ascii_offset = ord('A') if char.isupper() else ord('a')
        # Rumus enkripsi Caesar: (x + shift) % 26
        encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        encrypted += encrypted_char
    else:
        # Menggunakan karakter asli jika bukan alfabet
        encrypted += char

print(f"Plaintext: {teks}")
print(f"Ciphertext (shift {shift}): {encrypted}")

# Implementasikan juga fungsi dekripsi
decrypted = ""
for char in encrypted:
    if char.isalpha():
        ascii_offset = ord('A') if char.isupper() else ord('a')
        # Rumus dekripsi: (x - shift) % 26
        decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        decrypted += decrypted_char
    else:
        decrypted += char

print(f"Decrypted: {decrypted}")