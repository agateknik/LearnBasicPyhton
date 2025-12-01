class Matematika:
    
    #class method biasa
    def tambah(self, a, b):
        return a + b

    @staticmethod #class method engan decorator staticmethod
    def tambah(a,b):
        return a + b
    
print("============CONTOH CLASS METHOD======================")
#cara biasa
Matematika_obj = Matematika()
hasil = Matematika_obj.tambah(5, 7)
print("Hasil penjumlahan:", hasil)  # Output: Hasil penjum

#cara menggunakan staticmethod
hasil_static_method = Matematika.tambah(5, 7)
print("Hasil penjumlahan menggunakan staticmethod:", hasil_static_method)  # Output: Hasil penjumlahan menggunakan staticmethod

print("============CONTOH CLASS METHOD======================")
class BankAccount:
    active = True
    no = ""
    balance = 0
    
    #cara biasa
    def __init__(self, no, balance):
        self.no = no
        self.balance = balance
        
        if self.active == True:
            self.active = "Aktif"   
        else:
            self.active = "Non Aktif"    
        
    @classmethod #new class method dengan decorator classmethod
    def nonActived(cls, no, balance):
        result = cls(no, balance)
        result.active = False
        
        if result.active == True:
            result.active = "Aktif"
        else:
            result.active = "Non Aktif"

        return result
    
BankAccount_obj = BankAccount("123456789", 100000)    
print(f"Nomor Rekening {BankAccount_obj.no} memiliki saldo sebesar Rp.{BankAccount_obj.balance} dan rekeningnnya {BankAccount_obj.active}")

BankAccount_nonActive = BankAccount.nonActived("987654321", 500)
print(f"Nomor Rekening {BankAccount_nonActive.no} memiliki saldo sebesar Rp.{BankAccount_nonActive.balance} dan rekeningnnya {BankAccount_nonActive.active}")


print("============CONTOH PROPERTY METHOD======================")

class Category:
    _name = ""

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Nama Kategori tidak boleh kosong")
        self._name = name
        
categoryObject = Category()
categoryObject.name = "Gadget"  #memanggil setter   
print(categoryObject.name)              #memanggil getter   
