from tebak_angka import app

while True:
    print("\n=== PROGRAM TEBAK ANGKA SEDERHANA ===")
    print("1. Tebak Angka")
    print("2. Keluar")
        
    pilihan = input("Pilih aplikasi (1-2): ")  
         
    if pilihan == '1':
        app.app_tebak_angka()
    elif pilihan == '2':
        print("Terima kasih telah menggunakan game tebak angka sederhana.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")