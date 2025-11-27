#buat fungsi penjumlahan, pengurangan, perkalian, dan pembagian
def penjumlahan():
    print("---PROGRAM PENJUMLAHAN---")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil= angka1 + angka2
    print("Hasil penjumlahan:", hasil)
    print("---PROGRAM PENJUMLAHAN SELESAI---")
    print(input("Tekan Enter untuk kembali ke menu utama..."))
    
def pengurangan():
    print("---PROGRAM PENGURANGAN---")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil= angka1 - angka2
    print("Hasil pengurangan:", hasil)
    print("---PROGRAM PENGURANGAN SELESAI---")
    print(input("Tekan Enter untuk kembali ke menu utama..."))

def perkalian():   
    print("---PROGRAM PERKALIAN---")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil= angka1 * angka2
    print("Hasil perkalian:", hasil)
    print("---PROGRAM PERKALIAN SELESAI---")
    print(input("Tekan Enter untuk kembali ke menu utama..."))
    
def pembagian():
    print("---PROGRAM PEMBAGIAN---")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    if angka2 != 0:
        hasil= angka1 / angka2
        print("Hasil pembagian:", hasil)
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
    print("---PROGRAM PEMBAGIAN SELESAI---")
    print(input("Tekan Enter untuk kembali ke menu utama..."))

def app_menu():
    while True:
        print("\n=== KALKULATOR SEDERHANA ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        
        pilihan = input("Pilih operasi (1-5): ")
        
        if pilihan == '1':
            penjumlahan()
        elif pilihan == '2':
            pengurangan()
        elif pilihan == '3':
            perkalian()
        elif pilihan == '4':
            pembagian()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    app_menu()
    
