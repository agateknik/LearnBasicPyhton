class BankAccount:
    #buat attribut diencaplsulation dengan menambahkan __ diawal nama attribut
    __no = ""
    __balance = 0
    
    def __init__(self, no):
        self.__no = no
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def no(self):
        return self.__no
    
    def topup(self, topoup_amount):
        self.__balance += topoup_amount
        
    def cashout(self, cashout_amount):
        if cashout_amount > self.__balance:
            print("Saldo tidak cukup untuk melakukan cashout")
        else:
            self.__balance -= cashout_amount

account1 = BankAccount("12346789")   #bua
print(f"Nomor Rekening: {account1.no}")

account1.topup(5000)
print(f"Saldo setelah topup: Rp.{account1.balance}")

account1.cashout(2000)
print(f"Saldo setelah cashout: Rp.{account1.balance}")  

account1.cashout(4000)  #mencoba cashout melebihi saldo yang ada
print(f"Saldo setelah cashout: Rp.{account1.balance}")

