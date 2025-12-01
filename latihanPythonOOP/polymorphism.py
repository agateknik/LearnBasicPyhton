class Hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def suara(self):
        Print("Hewan bersuara")

class Anjing(Hewan):
    def suara(self):  #method overriding
        print(f"{self.nama} mengeluarkan suara Guk Guk")

class Kucing(Hewan):
    def suara(self):  #method overriding
        print(f"{self.nama} mengeluarkan suara Meong Meong")    
    
class Sapi(Hewan):
    def suara(self):  #method overriding
        print (f"{self.nama} mengeluarkan suara Moo Moo")

#polymorphism in action
hewan_list = [
    Anjing("Doggy"),
    Kucing("Kitty"),
    Sapi("Lembu")
    ]

for hewan in hewan_list:
    hewan.suara()  #memanggil method suara yang sesuai dengan objeknya  

#Ducktyping

class Mobil:
    def start(self):
        return "Mesin mobil menyala"

class Motor:
    def start(self):
        return "Mesin motor menyala"
    
class Pesawat:
    def start(self):
        return "Mesin pesawat menyala"

#fungsi ducttyping
def operasikan_kendaraan(kendaraan):
    print(kendaraan.start())
    
kendaraan_list = [
                  Mobil(), 
                  Motor(),
                  Pesawat()
                  ]

for kendaraan in kendaraan_list:
    operasikan_kendaraan(kendaraan)


    
                