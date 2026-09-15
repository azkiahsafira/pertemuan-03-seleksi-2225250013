print("==============================================")
print("       PROGRAM MEMBANDINGKAN DUA BILANGAN     ")
print("==============================================")

# Input
bilangan_pertama = float(input("Masukkan bilangan pertama: "))
bilangan_kedua = float(input("Masukkan bilangan kedua: "))

print("----------------------------------------------")

# Proses menggunakan nested if
if bilangan_pertama > bilangan_kedua:
    print("Bilangan pertama lebih besar daripada bilangan kedua.")
else:
    if bilangan_pertama < bilangan_kedua:
        print("Bilangan pertama lebih kecil daripada bilangan kedua.")
    else:
        print("Bilangan pertama sama dengan bilangan kedua.")

print("==============================================")