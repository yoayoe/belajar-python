'''
Quiz Algoritma: Array dan Struktur Data
-------------------------------------
Tujuan: Memahami penggunaan array (list di Python) dan manipulasi struktur data

Soal:
Buatlah program yang menerima input berupa daftar angka dan melakukan beberapa operasi:
1. Mencari nilai maksimum dan minimum dalam array
2. Menghitung rata-rata nilai dalam array
3. Menghitung berapa banyak nilai yang di atas rata-rata
4. Mengurutkan array secara ascending dan descending
'''

# Challenge 1: Analisis Array Dasar
# Buatlah program yang mencari nilai maksimum, minimum, dan rata-rata dalam array

# Kode Anda di sini:
print("=== Analisis Array Dasar ===")
input_str = input("Masukkan daftar angka (pisahkan dengan spasi): ")
# Konversi input string menjadi list of integers
numbers = [int(x) for x in input_str.split()]

if numbers:
    # Mencari nilai maksimum dan minimum
    nilai_max = max(numbers)
    nilai_min = min(numbers)
    
    # Menghitung rata-rata
    total = sum(numbers)
    rata_rata = total / len(numbers)
    
    # Output
    print(f"Array: {numbers}")
    print(f"Nilai maksimum: {nilai_max}")
    print(f"Nilai minimum: {nilai_min}")
    print(f"Rata-rata: {rata_rata}")
else:
    print("Array kosong")

# Challenge 2: Nilai di Atas Rata-rata
# Buatlah program yang menghitung berapa banyak nilai di atas rata-rata

# Kode Anda di sini:
print("\n=== Nilai di Atas Rata-rata ===")
input_str = input("Masukkan daftar angka (pisahkan dengan spasi): ")
numbers = [int(x) for x in input_str.split()]

if numbers:
    # Menghitung rata-rata
    rata_rata = sum(numbers) / len(numbers)
    
    # Menghitung nilai di atas rata-rata
    nilai_diatas_rata = [x for x in numbers if x > rata_rata]
    jumlah_diatas_rata = len(nilai_diatas_rata)
    
    # Output
    print(f"Array: {numbers}")
    print(f"Rata-rata: {rata_rata}")
    print(f"Jumlah nilai di atas rata-rata: {jumlah_diatas_rata}")
    print(f"Nilai-nilai di atas rata-rata: {nilai_diatas_rata}")
else:
    print("Array kosong")

# Challenge 3: Pengurutan Array
# Buatlah program yang mengurutkan array secara ascending dan descending

# Kode Anda di sini:
print("\n=== Pengurutan Array ===")
input_str = input("Masukkan daftar angka (pisahkan dengan spasi): ")
numbers = [int(x) for x in input_str.split()]

if numbers:
    # Pengurutan secara ascending
    ascending = sorted(numbers)
    
    # Pengurutan secara descending
    descending = sorted(numbers, reverse=True)
    
    # Output
    print(f"Array asli: {numbers}")
    print(f"Ascending: {ascending}")
    print(f"Descending: {descending}")
else:
    print("Array kosong")

# Challenge 4: Implementasi Manual
# Buatlah implementasi manual (tanpa menggunakan fungsi bawaan seperti min, max, sum)
# untuk mencari nilai maksimum, minimum, dan menghitung rata-rata

# Kode Anda di sini:
print("\n=== Implementasi Manual ===")
input_str = input("Masukkan daftar angka (pisahkan dengan spasi): ")
numbers = [int(x) for x in input_str.split()]

if numbers:
    # Implementasi manual untuk mencari nilai maksimum
    nilai_max = numbers[0]
    for num in numbers:
        if num > nilai_max:
            nilai_max = num
    
    # Implementasi manual untuk mencari nilai minimum
    nilai_min = numbers[0]
    for num in numbers:
        if num < nilai_min:
            nilai_min = num
    
    # Implementasi manual untuk menghitung total
    total = 0
    for num in numbers:
        total += num
    
    # Menghitung rata-rata
    rata_rata = total / len(numbers)
    
    # Output
    print(f"Array: {numbers}")
    print(f"Nilai maksimum (manual): {nilai_max}")
    print(f"Nilai minimum (manual): {nilai_min}")
    print(f"Total (manual): {total}")
    print(f"Rata-rata (manual): {rata_rata}")
else:
    print("Array kosong")

# Bonus Challenge: Pencarian Nilai
# Buatlah program yang mencari nilai tertentu dalam array dan mengembalikan posisinya
# Implementasikan algoritma pencarian linear dan binary search

# Kode Anda di sini:
print("\n=== Bonus: Algoritma Pencarian ===")
input_str = input("Masukkan daftar angka (pisahkan dengan spasi): ")
numbers = [int(x) for x in input_str.split()]

if numbers:
    # Input nilai yang dicari
    target = int(input("Masukkan nilai yang ingin dicari: "))
    
    # Pencarian linear
    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    
    # Pencarian binary (array harus terurut)
    def binary_search(arr, target):
        # Urutkan array terlebih dahulu
        sorted_arr = sorted(arr)
        
        # Pencarian binary
        left, right = 0, len(sorted_arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Jika nilai ditemukan
            if sorted_arr[mid] == target:
                return mid
            
            # Jika target lebih kecil, cari di bagian kiri
            elif sorted_arr[mid] > target:
                right = mid - 1
            
            # Jika target lebih besar, cari di bagian kanan
            else:
                left = mid + 1
        
        return -1
    
    # Lakukan pencarian
    linear_result = linear_search(numbers, target)
    
    # Sort array untuk binary search
    sorted_numbers = sorted(numbers)
    binary_result = binary_search(sorted_numbers, target)
    
    # Output
    print(f"Array: {numbers}")
    print(f"Nilai yang dicari: {target}")
    
    if linear_result != -1:
        print(f"Linear Search: Nilai ditemukan pada indeks {linear_result}")
    else:
        print(f"Linear Search: Nilai tidak ditemukan")
    
    if binary_result != -1:
        print(f"Binary Search: Nilai ditemukan pada indeks {binary_result} (dalam array terurut {sorted_numbers})")
    else:
        print(f"Binary Search: Nilai tidak ditemukan")
else:
    print("Array kosong")