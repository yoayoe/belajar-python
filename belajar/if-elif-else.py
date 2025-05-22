# Belajar Pernyataan Kondisional (if) di Python

# 1. Pernyataan if sederhana
print("=== Contoh if sederhana ===")
umur = 18
if umur >= 17:
    print("Anda sudah dapat membuat KTP")

# 2. Pernyataan if-else
print("\n=== Contoh if-else ===")
nilai = 75
if nilai >= 60:
    print(f"Nilai {nilai}: Lulus")
else:
    print(f"Nilai {nilai}: Tidak Lulus")

# 3. Pernyataan if-elif-else
print("\n=== Contoh if-elif-else ===")
nilai = 85
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"
print(f"Nilai {nilai}, Grade: {grade}")

# 4. Kondisi bersarang (nested if)
print("\n=== Kondisi bersarang (nested if) ===")
nilai = 75
kehadiran = 80

if nilai >= 70:
    if kehadiran >= 75:
        status = "Lulus"
    else:
        status = "Tidak Lulus (Kehadiran Kurang)"
else:
    status = "Tidak Lulus (Nilai Kurang)"
print(f"Nilai: {nilai}, Kehadiran: {kehadiran}%, Status: {status}")

# 5. Kondisi menggunakan operator logika (and, or, not)
print("\n=== Kondisi dengan operator logika ===")
nilai_teori = 80
nilai_praktek = 70

if nilai_teori >= 70 and nilai_praktek >= 70:
    status = "Lulus Keduanya"
elif nilai_teori >= 70 or nilai_praktek >= 70:
    status = "Lulus Salah Satu"
else:
    status = "Tidak Lulus Keduanya"
print(f"Nilai Teori: {nilai_teori}, Nilai Praktek: {nilai_praktek}, Status: {status}")

# 6. Ternary Operator (cara singkat menulis if-else)
print("\n=== Ternary Operator ===")
umur = 20
status = "Dewasa" if umur >= 18 else "Anak-anak"
print(f"Umur: {umur}, Status: {status}")

# 7. Mengecek nilai dalam range
print("\n=== Mengecek nilai dalam range ===")
suhu = 37
if 36.5 <= suhu <= 37.5:
    kondisi = "Normal"
elif suhu < 36.5:
    kondisi = "Hipotermia"
else:
    kondisi = "Demam"
print(f"Suhu tubuh: {suhu}°C, Kondisi: {kondisi}")