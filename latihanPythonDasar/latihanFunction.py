##fungsi tes##
# def nama_function():
#     print("Ini adalah contoh fungsi tanpa parameter.")
    
# nama_function()

##Fungsi dengan parameter##
def sapa(nama):
    print(f"Halo {nama}, Selamat datang.")    
    print("Semoga hari mu menyenangkan ya", nama)
sapa("Andi")

def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    print("Luas persegi dengan sisi 10 adalah:",luas)
hitung_luas_persegi(10)

##function dengan return##
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas
hasil_luas = hitung_luas_persegi_panjang(5, 10)
print("Luas persegi panjang adalah:",hasil_luas)

##function dengan nilai default parameter##
def sapa_dengan_default(sapaan, umur, nama="Pengguna"):
    print(f"{sapaan},{umur}, {nama}!")
sapa_dengan_default("Selamat pagi", 6, "Angga")
sapa_dengan_default(6, "angga","selamat pagi")

