class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def info(self):
        return f"Merek {self.merek}, buatan tahun {self.tahun}"

    def nyalakan(self):
        print(f"Kendaraan {self.merek} dinyalakan.")        


class Mobil(Kendaraan): #class Mobil mewarisi class Kendaraan

    """menggunakan super() untuk mengakses method dari class induk"""
    
    def __init__(self, merek, tahun, warna):
        super().__init__(merek, tahun)  #menggunakan super() untuk mengakses konstruktor class induk
        self.warna = warna
    
    def klakson(self):
        print(f"Mobil {self.info()}, berwana {self.warna},  dan memiliki klakson")

class Motor(Kendaraan): #class Motor mewarisi class Kendaraan
    
    def klakson(self):
        print(f"Motor {self.info()} memiliki klakson")       
        
    def nyalakan(self):    #method overriding, yaitu method diparent di inisiasi ulang di child class  
        print(f"Motor {self.merek} dinyalakan otomatis!")
         
        
Obj_mobil = Mobil("Toyota", 2020, "Merah")
Obj_mobil.nyalakan()
Obj_mobil.klakson()

Obj_motor = Motor("Yamaha", 2019)
Obj_motor.nyalakan()
Obj_motor.klakson()




        
