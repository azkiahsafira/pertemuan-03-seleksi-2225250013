print("==============================================")
print("         PROGRAM KELULUSAN BERSYARAT          ")
print("==============================================")

# Input
nilai_akhir = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))

print("----------------------------------------------")

# Proses dan seleksi
if nilai_akhir >= 60 and kehadiran >= 80:
    print("Status: Lulus")
    print("Syarat nilai akhir dan kehadiran terpenuhi.")
else:
    print("Status: Belum lulus")
    print("Syarat kelulusan belum terpenuhi.")

print("==============================================")