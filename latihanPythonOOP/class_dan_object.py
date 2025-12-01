class Kampus:
    """buat attribut untuk kelas Kampus"""
    nama= ""
    alamat= ""

class Mahasiswa:
    """buat attribut untuk class Mahasiswa"""
    nama= ""
    nim= 0
    
    #buat method untuk class Mahasiswa
    def perkenalan(self):
        print(f"Hello nama saya adalah {self.nama} dengan NIM {self.nim}")
    
    def menyapa(self,pesan):
        print(f"{pesan}, nama saya {self.nama}")
        
        
kampus1 = Kampus()
kampus2 = Kampus()

print(type(kampus1))
print(type(kampus2))
print(kampus1.nama)   #hasilnya  string kosong karena belum diisi
print(kampus1.alamat) #hasilnya  string kosong karena belum diisi


mahasiswa1 = Mahasiswa()  
"""menambahkan attribut nama dan nim pada objek mahasiswa1"""  
mahasiswa1.nim="10112345"
mahasiswa1.nama="Andi"


mahasiswa2 = Mahasiswa()
mahasiswa2.nim="10167890"
mahasiswa2.nama="Budi"

print(type(mahasiswa1))
print(type(mahasiswa2))

#tampilkan atribut pada object
print("tampilkan atribut pada object mahasiswa:")
print("Nama Mahasiswa 1:", mahasiswa1.nama) 
print("NIM Mahasiswa 1:", mahasiswa1.nim)   
print("Nama Mahasiswa 2:", mahasiswa2.nama) 
print("NIM Mahasiswa 2:", mahasiswa2.nim)

#tampilkan method pada object
mahasiswa1.perkenalan()  #memanggil method perkenalan pada objek mahasiswa1
mahasiswa2.perkenalan()  #memanggil method perkenalan pada objek mahasiswa2

mahasiswa1.menyapa('Selamat pagi')  #memanggil method menyapa pada objek mahasiswa1
mahasiswa2.menyapa('Senang bertemu dengan Anda')          #memanggil method menyapa pada objek mahasiswa2