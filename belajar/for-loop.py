#Belajar For Loop
# For loop adalah perulangan yang digunakan untuk mengulang suatu blok kode

pelanggan = ["Yoyok", "Budi", "Siti", "Joko"]
# Menggunakan for loop untuk mengulang elemen list  
for nama in pelanggan:
    print(f"Nama Pelanggan: {nama}") # Yoyok Budi Siti Joko

# Menggunakan for loop untuk mengulang elemen list dengan index
for i in range(len(pelanggan)):
    print(f"Nama Pelanggan: {pelanggan[i]}") # Yoyok Budi Siti Joko