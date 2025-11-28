from post_comment import post

if __name__ == "__main__":
    while True:    
        print("Selamat data diaplikasi Post dan Comment")
        print("Silahkan pilih opsi berikut:")
        print("1. Daftar Post")
        print("2. Untuk keluar dari aplikasi")
        
        pilihan = int(input("Masukkan pilihan Anda (1/2): "))    
        if pilihan == 1:
            post.menu_post()
        elif pilihan == 2:
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")
        