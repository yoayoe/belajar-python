#Belajar list
# List adalah tipe data yang dapat menyimpan banyak data dalam satu variabel

nama = ["Yoyok", "Budi", "Siti", "Joko"]

print(nama)
# Mengakses elemen list
print(nama[0]) # Yoyok
print(nama[1]) # Budi
print(nama[2]) # Siti
print(nama[3]) # Joko

print(len(nama)) # 4


nama.append("Andi") # Menambahkan elemen baru ke list
print(nama) # ['Yoyok', 'Budi', 'Siti', 'Joko', 'Andi']
print(len(nama)) # 5

nama.remove("Yoyok") # Menghapus elemen dari list
print(nama) # ['Budi', 'Siti', 'Joko', 'Andi']
print(len(nama)) # 4

nama [0]= "Kadal" # Mengubah elemen list
print(nama) # ['Kadal', 'Siti', 'Joko', 'Andi']
print(len(nama)) # 4