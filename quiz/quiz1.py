# Terima input dari pengguna
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
x = int(input("Masukkan nilai x: "))

# Pastikan a <= b
if a > b:
    print("Error: Nilai a harus lebih kecil atau sama dengan b")
else:
    # Temukan kelipatan pertama
    if a % x != 0:
        a = (a // x + 1) * x
    
    # Cetak kelipatan dari a hingga b
    for i in range(a, b + 1, x):
        print(i, end=" ")