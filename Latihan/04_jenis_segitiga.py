print("==============================================")
print("        PROGRAM MENENTUKAN JENIS SEGITIGA     ")
print("==============================================")

# Input
sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))
sisi_c = float(input("Masukkan panjang sisi c: "))

print("----------------------------------------------")

# Memeriksa apakah semua sisi positif
if sisi_a <= 0 or sisi_b <= 0 or sisi_c <= 0:
    print("Ketiga panjang sisi harus bernilai positif.")
else:
    # Memeriksa apakah ketiga sisi dapat membentuk segitiga
    if (
        sisi_a + sisi_b > sisi_c
        and sisi_a + sisi_c > sisi_b
        and sisi_b + sisi_c > sisi_a
    ):
        # Nested if untuk menentukan jenis segitiga
        if sisi_a == sisi_b:
            if sisi_b == sisi_c:
                print("Jenis segitiga: Segitiga sama sisi.")
            else:
                print("Jenis segitiga: Segitiga sama kaki.")
        else:
            if sisi_a == sisi_c:
                print("Jenis segitiga: Segitiga sama kaki.")
            else:
                if sisi_b == sisi_c:
                    print("Jenis segitiga: Segitiga sama kaki.")
                else:
                    print("Jenis segitiga: Segitiga sembarang.")
    else:
        print("Ketiga sisi tersebut tidak dapat membentuk segitiga.")

print("==============================================")