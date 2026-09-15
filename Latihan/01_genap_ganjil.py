print("==============================================")
print("      PROGRAM MENENTUKAN GENAP ATAU GANJIL    ")
print("==============================================")

# Input
bilangan = int(input("Masukkan sebuah bilangan bulat: "))

# Proses dan seleksi
if bilangan % 2 == 0:
    hasil = "genap"
else:
    hasil = "ganjil"

# Output
print("----------------------------------------------")
print(f"Bilangan {bilangan} merupakan bilangan {hasil}.")
print("==============================================")