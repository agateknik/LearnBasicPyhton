print("Contoh penggunaan while loop")
i =1
while i <= 5:
    print(i)
    i += 1
print("sekarang kondisi cetak mundur")
i = 5
while i >= 1:
    print(i)
    i -= 1

print("=== loop dengan kondisi boolean ===")
jalan = True
while jalan:
    print("loop jalan")
    jalan = False
print("loop berhenti")

print("=== program selalu muncul text input sampai ketik stop ===")
kata =""
while kata.lower() != "stop":
    kata = input("Silahkan ketik apa saja (ketik 'stop' untuk berhenti): ")
    print("Anda mengetik:", kata)
print("Program selesai karena Anda mengetik 'stop'.")

print("=== program hanya menerima input jika angka valid ===")
while True:
    angka_input = input("masukakan input berupa angka : ")
    if angka_input.isdigit():
        print("Anda memasukkan angka valid:", angka_input)
        break
    print("Input tidak valid. Silakan coba lagi.")
print("Program selesai setelah menerima input angka valid.")

print("Latihan jumlahka angka selama tidak 0")
total = 0
angka = None
while angka != 0:
    angka = int(input("Masukkan angka (ketik 0 untuk berhenti): "))
    total += angka
print("Total penjumlahan angka yang dimasukkan adalah:", total)

print("=== Latihan case nyata====")
print("program passwrord retry")
password_benar = "1234"
percobaan = 0
maksimal_percobaan = 3
while percobaan < maksimal_percobaan:
    input_password = input("Silahkan input password: ")
    if input_password == password_benar:
        print("Password benar, akses diberikan.")
        break
    else:
        percobaan += 1
        print(f"Password salah. Anda memiliki {maksimal_percobaan - percobaan} percobaan tersisa.")
else:
    print("Anda telah mencapai batas percobaan. Akses ditolak.")

print("Sekarang coba buat validasi bertingkat")
while True:
    angka = input("masukkan angka 5-10: ")
    if angka.isdigit():
        angka = int(angka)
        if 5 <= angka <= 10:
            print(f"Angka yang anda input, {angka}, angka yang valid")
            break
    print("Input tidak valid. Silakan coba lagi.")

print("====Program tebak angka sederhana====")
import random
angka_acak = random.randint(1,9)
percobaan = 0
maksimal_percobaan = 5

while percobaan < maksimal_percobaan:
    tebakan = input("masukkan tebakan angka antara 1-9=>")
    
    if not tebakan.isdigit():
        print("Input tidak valid. Silakan masukkan angka antara 1-9.")
        continue
    
    tebakan = int(tebakan)
    percobaan += 1
    
    if tebakan == angka_acak:
        print("Selamat, tebakan anda benar!")
        break
    
    if tebakan < angka_acak:
        print(f"angka yang diinput terlalu rendah, sisa percobaan {maksimal_percobaan - percobaan}, silahkan input kembali")
    else:
        print(f"angka yang diinput terlalu tinggi, sisa percobaan {maksimal_percobaan - percobaan}, silahkan input kembali")
else:
    print(f"Maaf, Anda telah mencapai batas percobaan. Angka yang benar adalah {angka_acak}.")

    
    