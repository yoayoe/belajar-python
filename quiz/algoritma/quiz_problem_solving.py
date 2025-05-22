'''
Quiz Algoritma: Pemecahan Masalah Dasar
--------------------------------------
Tujuan: Menerapkan algoritma pemecahan masalah dengan menggunakan struktur kendali dan fungsi

Soal-soal berikut merupakan contoh permasalahan untuk melatih kemampuan pemecahan masalah
dengan algoritma.
'''

# Challenge 1: Bilangan Prima
# Buatlah program untuk memeriksa apakah sebuah bilangan adalah bilangan prima,
# dan temukan semua bilangan prima dalam rentang tertentu.

# Kode Anda di sini:
print("=== Bilangan Prima ===")

# Fungsi untuk memeriksa apakah bilangan adalah prima
def is_prime(n):
    """
    Memeriksa apakah suatu bilangan merupakan bilangan prima
    
    Parameter:
    n (int): Bilangan yang akan diperiksa
    
    Return:
    bool: True jika bilangan prima, False jika bukan
    """
    # Bilangan kurang dari 2 bukan bilangan prima
    if n < 2:
        return False
    
    # Cek dari 2 hingga akar dari n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Program untuk memeriksa bilangan prima
angka = int(input("Masukkan bilangan untuk diperiksa: "))

if is_prime(angka):
    print(f"{angka} adalah bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")

# Program untuk mencari bilangan prima dalam rentang tertentu
print("\nMencari bilangan prima dalam rentang:")
awal = int(input("Masukkan nilai awal: "))
akhir = int(input("Masukkan nilai akhir: "))

print(f"Bilangan prima antara {awal} dan {akhir}:")
count = 0
for num in range(max(2, awal), akhir + 1):
    if is_prime(num):
        print(num, end=" ")
        count += 1

if count == 0:
    print("Tidak ada bilangan prima dalam rentang tersebut")
else:
    print(f"\nTotal: {count} bilangan prima")

# Challenge 2: Konversi Angka ke Teks
# Buatlah program yang mengkonversi angka ke kata-kata dalam Bahasa Indonesia

# Kode Anda di sini:
print("\n\n=== Konversi Angka ke Teks ===")

def angka_ke_teks(angka):
    """
    Mengkonversi angka ke teks dalam Bahasa Indonesia (0-999)
    
    Parameter:
    angka (int): Angka yang akan dikonversi (0-999)
    
    Return:
    str: Representasi teks dari angka
    """
    if angka == 0:
        return "nol"
    
    # Definisikan kata-kata untuk angka dasar
    satuan = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
    belasan = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
    puluhan = ["", "sepuluh", "dua puluh", "tiga puluh", "empat puluh", "lima puluh",
              "enam puluh", "tujuh puluh", "delapan puluh", "sembilan puluh"]
    
    # Konversi berdasarkan nilai angka
    if angka < 10:
        return satuan[angka]
    elif angka < 20:
        return belasan[angka - 10]
    elif angka < 100:
        return puluhan[angka // 10] + (" " + satuan[angka % 10] if angka % 10 != 0 else "")
    else:  # angka 100-999
        if angka == 100:
            return "seratus"
        elif angka < 200:
            return "seratus " + angka_ke_teks(angka % 100)
        else:
            return satuan[angka // 100] + " ratus" + (" " + angka_ke_teks(angka % 100) if angka % 100 != 0 else "")

# Program utama
try:
    angka = int(input("Masukkan angka (0-999): "))
    
    if 0 <= angka <= 999:
        hasil = angka_ke_teks(angka)
        print(f"{angka} dalam kata: {hasil}")
    else:
        print("Angka harus dalam rentang 0-999")
except ValueError:
    print("Input harus berupa angka")

# Challenge 3: Perhitungan Fibonacci dengan Memoization
# Buatlah program untuk menghitung bilangan Fibonacci dengan teknik memoization
# untuk meningkatkan performa pada nilai input yang besar

# Kode Anda di sini:
print("\n=== Fibonacci dengan Memoization ===")

# Pendekatan rekursif biasa (kurang efisien untuk nilai besar)
def fibonacci_rekursif(n):
    """
    Menghitung bilangan Fibonacci dengan rekursi sederhana
    
    Parameter:
    n (int): Indeks bilangan Fibonacci yang dicari
    
    Return:
    int: Bilangan Fibonacci ke-n
    """
    if n <= 1:
        return n
    return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)

# Pendekatan dengan memoization
def fibonacci_memo(n, memo={}):
    """
    Menghitung bilangan Fibonacci dengan memoization
    
    Parameter:
    n (int): Indeks bilangan Fibonacci yang dicari
    memo (dict): Dictionary untuk menyimpan hasil perhitungan yang sudah dilakukan
    
    Return:
    int: Bilangan Fibonacci ke-n
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Pendekatan iteratif (paling efisien)
def fibonacci_iteratif(n):
    """
    Menghitung bilangan Fibonacci dengan metode iteratif
    
    Parameter:
    n (int): Indeks bilangan Fibonacci yang dicari
    
    Return:
    int: Bilangan Fibonacci ke-n
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Program utama
n = int(input("Masukkan nilai n untuk Fibonacci: "))

if n < 0:
    print("Input harus berupa bilangan non-negatif")
else:
    # Bandingkan hasil dari berbagai metode
    print(f"Fibonacci ke-{n}:")
    
    # Untuk nilai kecil, kita bisa menggunakan rekursif biasa
    if n < 30:
        result_rekursif = fibonacci_rekursif(n)
        print(f"Metode rekursif: {result_rekursif}")
    else:
        print("Metode rekursif tidak dijalankan (terlalu lambat untuk n >= 30)")
    
    # Metode memoization dan iteratif untuk semua nilai
    result_memo = fibonacci_memo(n)
    result_iteratif = fibonacci_iteratif(n)
    
    print(f"Metode memoization: {result_memo}")
    print(f"Metode iteratif: {result_iteratif}")

# Challenge 4: Game Tebak Angka dengan AI Sederhana
# Buatlah permainan tebak angka dimana komputer mencoba menebak
# angka yang dipikirkan oleh pengguna menggunakan binary search

# Kode Anda di sini:
print("\n=== Game Tebak Angka dengan AI Sederhana ===")
print("Pikirkan sebuah angka dari 1-100, dan komputer akan menebaknya.")
print("Beritahu komputer apakah tebakannya benar, terlalu besar, atau terlalu kecil.")

low = 1
high = 100
tebakan_ke = 0
selesai = False

print("Gunakan: 'c' untuk benar, 'l' untuk terlalu kecil, 'h' untuk terlalu besar")

while not selesai and low <= high:
    # Komputer menebak dengan binary search
    tebakan = (low + high) // 2
    tebakan_ke += 1
    
    respons = input(f"Tebakan ke-{tebakan_ke}: Apakah angkanya {tebakan}? (c/l/h): ").lower()
    
    if respons == 'c':
        print(f"Komputer berhasil menebak angka Anda ({tebakan}) dalam {tebakan_ke} kali tebakan!")
        selesai = True
    elif respons == 'l':
        # Jika tebakan terlalu kecil, cari di sebelah kanan
        low = tebakan + 1
    elif respons == 'h':
        # Jika tebakan terlalu besar, cari di sebelah kiri
        high = tebakan - 1
    else:
        print("Input tidak valid. Gunakan 'c', 'l', atau 'h'.")
        tebakan_ke -= 1  # Tidak menghitung tebakan ini

if not selesai:
    print("Hmm, sepertinya ada kesalahan. Pastikan Anda memberikan respons yang konsisten.")