print("==================================================")
print("           ANALISIS PERSAMAAN KUADRAT             ")
print("==================================================")
print("Bentuk umum: ax² + bx + c = 0")
print("--------------------------------------------------")

# ============================================================
# INPUT
# ============================================================

a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

print("--------------------------------------------------")

# Menampilkan kembali koefisien yang dimasukkan
print("Koefisien persamaan:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("--------------------------------------------------")

# ============================================================
# PROSES SELEKSI
# ============================================================

# Jika a = 0, maka persamaan bukan persamaan kuadrat.
if a == 0:

    print("Bukan persamaan kuadrat.")

else:

    # Menghitung diskriminan
    diskriminan = b ** 2 - 4 * a * c

    print(f"Diskriminan = {diskriminan:.2f}")

    # ========================================================
    # MENENTUKAN JENIS AKAR
    # ========================================================

    # Kondisi pertama: diskriminan lebih besar dari 0
    if diskriminan > 0:

        # Menghitung dua akar real yang berbeda
        x1 = (-b + diskriminan ** 0.5) / (2 * a)
        x2 = (-b - diskriminan ** 0.5) / (2 * a)

        print("Dua akar real yang berbeda.")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")

    else:

        # Nested if untuk memeriksa apakah diskriminan = 0
        if diskriminan == 0:

            # Menghitung akar real kembar
            x = -b / (2 * a)

            print("Satu akar real kembar.")
            print(f"x = {x:.2f}")

        else:

            # Jika diskriminan kurang dari 0
            print("Tidak ada akar real.")

# ============================================================
# PROGRAM SELESAI
# ============================================================

print("--------------------------------------------------")
print("Analisis persamaan kuadrat selesai.")
print("==================================================")