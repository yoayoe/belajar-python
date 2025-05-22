'''
Quiz Algoritma: Kelipatan Bilangan
---------------------------------
Tujuan: Memahami penggunaan struktur kendali (if, for, while) dan algoritma dasar

Soal:
Tuliskan program yang menerima masukan 3 (tiga) buah integer, misalnya a, b, dan x,
dan menuliskan ke layar bilangan pertama antara a dan b (a dan b termasuk) yang
merupakan kelipatan (habis dibagi) x. Asumsikan a <= b.

Contoh masukan: a = 10, b = 20, x = 4
Tertulis di layar = 12
'''

# Challenge 1: Mencari Kelipatan dengan For Loop
# Buatlah program yang mencari bilangan pertama dalam rentang a hingga b yang habis dibagi x

# Kode Anda di sini:
print("=== Mencari Kelipatan (For Loop) ===")
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
x = int(input("Masukkan nilai x: "))

# Pastikan a <= b
if a > b:
    print("Error: Nilai a harus lebih kecil atau sama dengan b")
else:
    # Menggunakan for loop
    result = None
    for i in range(a, b + 1):
        if i % x == 0:
            result = i
            break
    
    if result is not None:
        print(f"Bilangan pertama antara {a} dan {b} yang habis dibagi {x} adalah: {result}")
    else:
        print(f"Tidak ada bilangan antara {a} dan {b} yang habis dibagi {x}")

# Challenge 2: Mengoptimalkan Pencarian Kelipatan
# Buatlah versi yang lebih efisien dengan menggunakan properti matematika kelipatan

# Kode Anda di sini:
print("\n=== Mencari Kelipatan (Optimized) ===")
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
x = int(input("Masukkan nilai x: "))

# Pastikan a <= b
if a > b:
    print("Error: Nilai a harus lebih kecil atau sama dengan b")
else:
    # Temukan kelipatan pertama dari x yang >= a
    # Jika a sudah habis dibagi x, maka hasilnya a
    # Jika tidak, kita cari kelipatan x terkecil yang >= a
    if a % x == 0:
        first_multiple = a
    else:
        # Menghitung kelipatan x terkecil yang >= a
        first_multiple = a + (x - a % x)
    
    # Cek apakah kelipatan berada dalam rentang
    if first_multiple <= b:
        print(f"Bilangan pertama antara {a} dan {b} yang habis dibagi {x} adalah: {first_multiple}")
    else:
        print(f"Tidak ada bilangan antara {a} dan {b} yang habis dibagi {x}")

# Challenge 3: Mencari Kelipatan dengan While Loop
# Buatlah versi alternatif menggunakan while loop

# Kode Anda di sini:
print("\n=== Mencari Kelipatan (While Loop) ===")
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
x = int(input("Masukkan nilai x: "))

# Pastikan a <= b
if a > b:
    print("Error: Nilai a harus lebih kecil atau sama dengan b")
else:
    # Menggunakan while loop
    current = a
    result = None
    
    while current <= b:
        if current % x == 0:
            result = current
            break
        current += 1
    
    if result is not None:
        print(f"Bilangan pertama antara {a} dan {b} yang habis dibagi {x} adalah: {result}")
    else:
        print(f"Tidak ada bilangan antara {a} dan {b} yang habis dibagi {x}")

# Bonus Challenge: Algoritma yang Lebih Kompleks
# Buatlah program yang mencari kelipatan bilangan yang memenuhi kondisi tambahan
# Misalnya, kelipatan x yang juga merupakan bilangan ganjil atau bilangan prima

# Kode Anda di sini:
print("\n=== Bonus: Kelipatan dengan Kondisi Tambahan ===")
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
x = int(input("Masukkan nilai x: "))
kondisi = input("Pilih kondisi tambahan (ganjil/genap): ").lower()

# Pastikan a <= b
if a > b:
    print("Error: Nilai a harus lebih kecil atau sama dengan b")
else:
    # Temukan kelipatan x yang memenuhi kondisi tambahan
    result = None
    
    for i in range(a, b + 1):
        # Cek apakah i kelipatan x
        if i % x == 0:
            # Cek kondisi tambahan
            if kondisi == "ganjil" and i % 2 != 0:
                result = i
                break
            elif kondisi == "genap" and i % 2 == 0:
                result = i
                break
            # Jika tidak ada kondisi tambahan atau kondisi tidak valid
            elif kondisi not in ["ganjil", "genap"]:
                result = i
                break
    
    if result is not None:
        if kondisi in ["ganjil", "genap"]:
            print(f"Bilangan pertama antara {a} dan {b} yang habis dibagi {x} dan {kondisi} adalah: {result}")
        else:
            print(f"Bilangan pertama antara {a} dan {b} yang habis dibagi {x} adalah: {result}")
    else:
        if kondisi in ["ganjil", "genap"]:
            print(f"Tidak ada bilangan antara {a} dan {b} yang habis dibagi {x} dan {kondisi}")
        else:
            print(f"Tidak ada bilangan antara {a} dan {b} yang habis dibagi {x}")