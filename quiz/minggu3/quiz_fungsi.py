'''
Quiz 7: Fungsi di Python
----------------------
Tujuan: Memahami fungsi, parameter, dan nilai kembali di Python
'''

# Challenge 1: Fungsi Sederhana
# Buatlah fungsi untuk menghitung luas dan keliling persegi panjang

# Kode Anda di sini:
def hitung_luas_persegi_panjang(panjang, lebar):
    """
    Menghitung luas persegi panjang
    
    Parameter:
    panjang (float): Panjang persegi panjang
    lebar (float): Lebar persegi panjang
    
    Return:
    float: Luas persegi panjang
    """
    return panjang * lebar

def hitung_keliling_persegi_panjang(panjang, lebar):
    """
    Menghitung keliling persegi panjang
    
    Parameter:
    panjang (float): Panjang persegi panjang
    lebar (float): Lebar persegi panjang
    
    Return:
    float: Keliling persegi panjang
    """
    return 2 * (panjang + lebar)

# Penggunaan fungsi
print("=== Hitung Luas dan Keliling Persegi Panjang ===")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = hitung_luas_persegi_panjang(panjang, lebar)
keliling = hitung_keliling_persegi_panjang(panjang, lebar)

print(f"Luas persegi panjang: {luas}")
print(f"Keliling persegi panjang: {keliling}")

# Challenge 2: Fungsi dengan Nilai Default
# Buatlah fungsi untuk menghitung volume balok dengan nilai default

# Kode Anda di sini:
def hitung_volume_balok(panjang, lebar, tinggi=1):
    """
    Menghitung volume balok
    
    Parameter:
    panjang (float): Panjang balok
    lebar (float): Lebar balok
    tinggi (float, optional): Tinggi balok. Default adalah 1
    
    Return:
    float: Volume balok
    """
    return panjang * lebar * tinggi

# Penggunaan fungsi dengan nilai default
print("\n=== Hitung Volume Balok ===")
p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))
t_input = input("Masukkan tinggi (kosongkan untuk nilai default): ")

if t_input:
    t = float(t_input)
    volume = hitung_volume_balok(p, l, t)
    print(f"Volume balok dengan tinggi {t}: {volume}")
else:
    volume = hitung_volume_balok(p, l)
    print(f"Volume balok dengan tinggi default: {volume}")

# Challenge 3: Fungsi dengan Multiple Return Values
# Buatlah fungsi yang mengembalikan statistik dari sebuah list angka
# (min, max, jumlah, rata-rata)

# Kode Anda di sini:
def hitung_statistik(angka_list):
    """
    Menghitung statistik dasar dari list angka
    
    Parameter:
    angka_list (list): List berisi angka
    
    Return:
    tuple: (minimum, maximum, jumlah, rata-rata)
    """
    minimum = min(angka_list)
    maximum = max(angka_list)
    jumlah = sum(angka_list)
    rata_rata = jumlah / len(angka_list) if len(angka_list) > 0 else 0
    
    return minimum, maximum, jumlah, rata_rata

# Penggunaan fungsi dengan multiple return values
print("\n=== Statistik Angka ===")
input_angka = input("Masukkan beberapa angka dipisahkan spasi: ")
angka_list = [float(x) for x in input_angka.split()]

if angka_list:
    min_val, max_val, jumlah, rata_rata = hitung_statistik(angka_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    print(f"Jumlah: {jumlah}")
    print(f"Rata-rata: {rata_rata}")
else:
    print("Tidak ada angka yang dimasukkan.")

# Challenge 4: Fungsi Rekursif
# Buatlah fungsi faktorial menggunakan rekursi

# Kode Anda di sini:
def faktorial(n):
    """
    Menghitung faktorial dari n menggunakan rekursi
    
    Parameter:
    n (int): Bilangan non-negatif
    
    Return:
    int: Hasil faktorial n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Penggunaan fungsi rekursif
print("\n=== Faktorial Rekursif ===")
n = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))

if n < 0:
    print("Faktorial tidak didefinisikan untuk bilangan negatif.")
else:
    hasil = faktorial(n)
    print(f"{n}! = {hasil}")

# Bonus Challenge: Kalkulator dengan Fungsi dan Lambda
# Buatlah kalkulator yang menggunakan fungsi dan ekspresi lambda

# Kode Anda di sini:
print("\n=== Kalkulator dengan Fungsi ===")

# Definisikan operasi dengan fungsi dan lambda
operasi = {
    'tambah': lambda x, y: x + y,
    'kurang': lambda x, y: x - y,
    'kali': lambda x, y: x * y,
    'bagi': lambda x, y: x / y if y != 0 else "Error: Pembagian dengan nol"
}

def kalkulator(x, y, op):
    """
    Melakukan perhitungan berdasarkan operasi yang dipilih
    
    Parameter:
    x (float): Operand pertama
    y (float): Operand kedua
    op (str): Jenis operasi ('tambah', 'kurang', 'kali', 'bagi')
    
    Return:
    float/str: Hasil perhitungan
    """
    return operasi.get(op, lambda x, y: "Operasi tidak valid")(x, y)

# UI kalkulator
while True:
    print("\nPilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("0. Keluar")
    
    pilihan = input("Masukkan pilihan (0-4): ")
    
    if pilihan == '0':
        print("Terima kasih telah menggunakan kalkulator.")
        break
    
    if pilihan in ['1', '2', '3', '4']:
        x = float(input("Masukkan angka pertama: "))
        y = float(input("Masukkan angka kedua: "))
        
        if pilihan == '1':
            hasil = kalkulator(x, y, 'tambah')
            print(f"{x} + {y} = {hasil}")
        elif pilihan == '2':
            hasil = kalkulator(x, y, 'kurang')
            print(f"{x} - {y} = {hasil}")
        elif pilihan == '3':
            hasil = kalkulator(x, y, 'kali')
            print(f"{x} * {y} = {hasil}")
        elif pilihan == '4':
            hasil = kalkulator(x, y, 'bagi')
            print(f"{x} / {y} = {hasil}")
    else:
        print("Input tidak valid. Silakan coba lagi.")