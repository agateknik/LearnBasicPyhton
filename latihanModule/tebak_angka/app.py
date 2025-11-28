import random

def app_tebak_angka():

    angka_acak = random.randint(1, 9)
    maksimal_percobaan = 3
    percobaan = 0
    
    while True:
        tebakan = input("Tebak angka antara 1 sampai 9 (atau ketik 'keluar' untuk kembali ke menu utama): ")
        if tebakan.lower() == 'keluar':
            print("Keluar dari permainan tebak angka.")
            break
        try:
            tebakan = int(tebakan)
            percobaan += 1
            if tebakan < angka_acak:
                print("Terlalu rendah! Coba lagi.")
            elif tebakan > angka_acak:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! Kamu berhasil menebak angka {angka_acak} dengan {percobaan} percobaan.")
                break
            if percobaan >= maksimal_percobaan:
                print(f"Maaf, kamu sudah mencapai batas percobaan. Angka yang benar adalah {angka_acak}.")
                break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka antara 1 sampai 10 atau 'keluar'.")
    print(input("Tekan Enter untuk kembali ke menu utama..."))
    