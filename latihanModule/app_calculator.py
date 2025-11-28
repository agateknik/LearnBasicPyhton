from calculator import operasi as op

if __name__ == "__main__":
    while True:
        print("\n=== KALKULATOR SEDERHANA ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        
        pilihan = input("Pilih operasi (1-5): ")
        
        if pilihan == '1':
            op.penjumlahan()
        elif pilihan == '2':
            op.pengurangan()
        elif pilihan == '3':
           op. perkalian()
        elif pilihan == '4':
            op.pembagian()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")