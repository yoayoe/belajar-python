#Belajar while loop
# while loop
# while condition:

data=""

while data != "x":
    data = input("Masukkan data (x untuk keluar): ")
    print("Data yang dimasukkan adalah: ", data)
    if data == "x":
        print("Anda keluar dari loop")
    else:
        print("Anda masih dalam loop")
        print("Data yang dimasukkan adalah: ", data)
    print("Anda masih dalam loop")