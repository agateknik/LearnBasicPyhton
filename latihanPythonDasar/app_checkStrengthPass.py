import re

def cek_password(password):
    skor = 0
    catatan = []
    
    # panjang password
    if len(password) >= 12:
        skor += 40
        catatan.append("Password sangat kuat.")
    elif len(password) >= 8:
        skor += 25
        catatan.append("Password cukup kuat.")
    elif len(password) >= 4:
        skor += 10
        catatan.append("Password kurang kuat.")
    else:
        skor += 5
        catatan.append("Password lemah.")
    
    # huruf besar
    if re.search(r"[A-Z]", password):
        skor += 15
        catatan.append("Terdapat huruf besar.")
    else:
        catatan.append("Tidak mengandung huruf besar.")
    
    # huruf kecil
    if re.search(r"[a-z]", password):
        skor += 15
        catatan.append("Ada huruf kecil.")
    else:
        catatan.append("Tidak ada huruf kecil.")
    
    # angka
    if re.search(r"[0-9]", password):
        skor += 15
        catatan.append("Mengandung angka.")
    else:
        catatan.append("Tidak mengandung angka.")   
    
    # karakter spesial
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        skor += 15
        catatan.append("Ada karakter spesial.")
    else:
        catatan.append("Tidak ada karakter spesial.")
    
    # penilaian skor
    if skor >= 80:
        status = "STRONG"
    elif skor >= 50:
        status = "MEDIUM"
    else:
        status = "WEAK"
    
    return status, skor, catatan


#main program   
def app_main():
    print("=== PROGRAM CEK KEKUATAN PASSWORD ===")    
    
    while True:  
        password = input("Masukkan password yang ingin dicek: ")
        try:
            if not password:
                raise ValueError("Password tidak boleh kosong. Silakan masukkan password yang valid.")
        except ValueError as ve:
            print(ve)
            continue
        
        status, skor, catatan = cek_password(password)
        print("\nHasil pengecekan password:")
        print("Skor Kekuatan Password:", skor)
        print("Status Kekuatan Password:", status)
        print("Catatan:")
        for item in catatan:
            print("-", item)
     
        ulang = input("\nApakah Anda ingin mengecek password lain? (ketik y , jika ingin mengulang, enter jika ingin keluar dari program): ")
        if ulang != 'y':
            print("Terima kasih telah menggunakan program cek kekuatan password.")
            break   
        
if __name__ == "__main__":
    app_main()