def penjumlahan():
    while True:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            break
        except ValueError:
            print("Error: Masukkan angka yang valid.")
    while True:
        try:
            angka2 = float(input("Masukkan angka kedua: "))
            break
        except:
            print("Error: Masukkan angka yang valid.")
    hasil = angka1 + angka2
    print("Hasil penjumlahan:", hasil)
    print("---PROGRAM PENJUMLAHAN SELESAI---")
    print(input("Tekan Enter untuk kembali ke menu utama..."))
    
def pengurangan():
    print("---PROGRAM PENGURANGAN---")
    while True:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            break
        except ValueError:
            print("Error: Masukkan angka yang valid.")  
    while True:
        try:
            angka2 = float(input("Masukkan angka kedua: "))
            break
        except:
            print("Error: Masukkan angka yang valid.")
    hasil= angka1 - angka2
    print("Hasil pengurangan:", hasil)
    print("---PROGRAM PENGURANGAN SELESAI---")
    print(input("Tekan Enter untuk kembali ke menu utama..."))

def perkalian():   
    print("---PROGRAM PERKALIAN---")
    while True:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            break
        except ValueError:
            print("Error: Masukkan angka yang valid.")
    while True:
        try:
            angka2 = float(input("Masukkan angka kedua: "))
            break
        except:
            print("Error: Masukkan angka yang valid.")
    hasil= angka1 * angka2
    print("Hasil perkalian:", hasil)
    print("---PROGRAM PERKALIAN SELESAI---")
    print(input("Tekan Enter untuk kembali ke menu utama..."))
    
def pembagian():
    print("---PROGRAM PEMBAGIAN---")
    while True:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            break
        except ValueError:
            print("Error: Masukkan angka yang valid.")
    while True:
        try:
            angka2 = float(input("Masukkan angka kedua: "))
            if angka2 == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan. Input ulang.")
            else:
                break
        except:
            print("Error: Masukkan angka yang valid.")
    hasil= angka1 / angka2
    print("Hasil pembagian:", hasil)
    print("---PROGRAM PEMBAGIAN SELESAI---")
    print(input("Tekan Enter untuk kembali ke menu utama..."))
