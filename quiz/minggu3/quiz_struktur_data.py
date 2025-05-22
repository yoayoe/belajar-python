'''
Quiz 8: Struktur Data Lanjutan
----------------------------
Tujuan: Memahami list, dictionary, tuple, dan set di Python
'''

# Challenge 1: Manipulasi List
# Buatlah program yang melakukan berbagai operasi pada list:
# - Menambah elemen
# - Menghapus elemen
# - Mengurutkan list
# - Membalik urutan list
# - Mencari nilai tertentu

# Kode Anda di sini:
print("=== Manipulasi List ===")
buah = ["apel", "jeruk", "mangga", "pisang"]
print(f"List awal: {buah}")

# Menambah elemen
buah.append("anggur")
print(f"Setelah append: {buah}")

buah.insert(2, "melon")
print(f"Setelah insert pada indeks 2: {buah}")

# Menghapus elemen
buah_dihapus = buah.pop()
print(f"Elemen yang di-pop: {buah_dihapus}")
print(f"List setelah pop: {buah}")

buah.remove("jeruk")
print(f"List setelah remove 'jeruk': {buah}")

# Mengurutkan list
buah.sort()
print(f"List setelah sort: {buah}")

# Membalik urutan list
buah.reverse()
print(f"List setelah reverse: {buah}")

# Mencari nilai
cari = input("\nMasukkan nama buah yang ingin dicari: ")
if cari in buah:
    indeks = buah.index(cari)
    print(f"'{cari}' ditemukan pada indeks {indeks}")
else:
    print(f"'{cari}' tidak ditemukan dalam list")

# Challenge 2: Dictionary
# Buatlah program yang menggunakan dictionary untuk menyimpan
# data mahasiswa (NIM sebagai key, dan dictionary dengan nama & nilai sebagai value)

# Kode Anda di sini:
print("\n=== Data Mahasiswa dengan Dictionary ===")
mahasiswa = {
    "123456": {"nama": "Budi", "nilai": 85},
    "654321": {"nama": "Ani", "nilai": 90},
    "789012": {"nama": "Cindy", "nilai": 78}
}

print("Data mahasiswa awal:")
for nim, data in mahasiswa.items():
    print(f"NIM: {nim}, Nama: {data['nama']}, Nilai: {data['nilai']}")

# Menambah data mahasiswa baru
print("\nMenambah data mahasiswa baru:")
nim_baru = input("Masukkan NIM: ")
nama_baru = input("Masukkan Nama: ")
nilai_baru = int(input("Masukkan Nilai: "))

mahasiswa[nim_baru] = {"nama": nama_baru, "nilai": nilai_baru}

# Mencari data mahasiswa
print("\nMencari data mahasiswa:")
cari_nim = input("Masukkan NIM yang ingin dicari: ")

if cari_nim in mahasiswa:
    data = mahasiswa[cari_nim]
    print(f"Data ditemukan - Nama: {data['nama']}, Nilai: {data['nilai']}")
else:
    print(f"NIM {cari_nim} tidak ditemukan")

# Menghapus data mahasiswa
print("\nMenghapus data mahasiswa:")
hapus_nim = input("Masukkan NIM yang ingin dihapus: ")

if hapus_nim in mahasiswa:
    del mahasiswa[hapus_nim]
    print(f"Data mahasiswa dengan NIM {hapus_nim} telah dihapus")
else:
    print(f"NIM {hapus_nim} tidak ditemukan")

# Tampilkan data mahasiswa akhir
print("\nData mahasiswa akhir:")
for nim, data in mahasiswa.items():
    print(f"NIM: {nim}, Nama: {data['nama']}, Nilai: {data['nilai']}")

# Challenge 3: List Comprehension
# Buatlah program yang menggunakan list comprehension untuk:
# - Membuat list bilangan kuadrat dari 1-10
# - Membuat list yang hanya berisi bilangan genap dari list awal
# - Membuat list yang berisi panjang setiap string dari list string

# Kode Anda di sini:
print("\n=== List Comprehension ===")

# List bilangan kuadrat dari 1-10
kuadrat = [x**2 for x in range(1, 11)]
print(f"List kuadrat dari 1-10: {kuadrat}")

# List bilangan awal
bilangan = list(range(1, 21))
print(f"List bilangan awal: {bilangan}")

# List yang hanya berisi bilangan genap
genap = [x for x in bilangan if x % 2 == 0]
print(f"List bilangan genap: {genap}")

# List string
kata = ["Python", "adalah", "bahasa", "pemrograman", "yang", "menyenangkan"]
print(f"List kata: {kata}")

# List panjang setiap string
panjang_kata = [len(s) for s in kata]
print(f"Panjang setiap kata: {panjang_kata}")

# Challenge 4: Tuple dan Set
# Buatlah program yang mendemonstrasikan penggunaan tuple dan set

# Kode Anda di sini:
print("\n=== Tuple dan Set ===")

# Tuple
print(">> Tuple <<")
kordinat = (3, 4)
print(f"Kordinat: {kordinat}")
print(f"X: {kordinat[0]}")
print(f"Y: {kordinat[1]}")

# Unpacking tuple
x, y = kordinat
print(f"X (dari unpacking): {x}")
print(f"Y (dari unpacking): {y}")

# Tuple tidak bisa diubah (immutable)
print("Tuple bersifat immutable (tidak bisa diubah)")
try:
    kordinat[0] = 10
except TypeError as e:
    print(f"Error: {e}")

# Set
print("\n>> Set <<")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Operasi set
print(f"Union (A ∪ B): {set_a | set_b}")
print(f"Intersection (A ∩ B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")
print(f"Symmetric Difference (A △ B): {set_a ^ set_b}")

# Set tidak memiliki duplikat
set_c = {1, 1, 2, 2, 3, 3}
print(f"Set dengan nilai duplikat: {set_c}")

# Bonus Challenge: Nested Data Structures
# Buatlah program yang menggunakan struktur data bersarang
# (misalnya dictionary yang berisi list, atau list yang berisi dictionary)

# Kode Anda di sini:
print("\n=== Struktur Data Bersarang ===")

# Dictionary of lists
sekolah = {
    "SD": ["Matematika", "IPA", "Bahasa Indonesia"],
    "SMP": ["Matematika", "IPA", "Bahasa Indonesia", "Bahasa Inggris"],
    "SMA": ["Matematika", "Fisika", "Kimia", "Biologi", "Bahasa Indonesia", "Bahasa Inggris"]
}

print("Mata pelajaran berdasarkan tingkat sekolah:")
for tingkat, mapel in sekolah.items():
    print(f"{tingkat}: {', '.join(mapel)}")

# List of dictionaries
siswa = [
    {"nama": "Andi", "nilai": {"Matematika": 85, "IPA": 90, "Bahasa": 78}},
    {"nama": "Budi", "nilai": {"Matematika": 75, "IPA": 80, "Bahasa": 85}},
    {"nama": "Citra", "nilai": {"Matematika": 90, "IPA": 85, "Bahasa": 92}}
]

print("\nData nilai siswa:")
for s in siswa:
    print(f"Nama: {s['nama']}")
    print("  Nilai:")
    rata_rata = sum(s['nilai'].values()) / len(s['nilai'])
    for mapel, nilai in s['nilai'].items():
        print(f"    {mapel}: {nilai}")
    print(f"  Rata-rata: {rata_rata:.2f}")
    print()