class BalanceNotEnough(Exception):
    def __init__(self, message):
        self.mesaage = message
        
    def __str__(self):
        return self.mesaage
    
class BankAccount:
    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance
    
    def cashoutAmount(self, amount):
        if amount > self.balance:
            raise BalanceNotEnough("Saldo tidak cukup untuk melakukan transfer")
        else:
            self.balance -= amount
    
try:
    bank_account1 = BankAccount("123456789", 10000)
    bank_account1.cashoutAmount(15000)  #mencoba cashout melebihi saldo yang ada  
except BalanceNotEnough as e:
    print(e)
    
print(f"Saldo setelah cashout: Rp.{bank_account1.balance}")
    
    