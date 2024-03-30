class Atm():
    name='SBI'
    cash=50000
    __account={
        'Sukhdeep':7832,
        'Shubham':1876,
        'Kushali':2345,
        'Savi':3456
    }
    def cashout(self,pin,money):
        if pin in self.__account.values():
            if self.cash>=money:
                self.cash=self.cash-money
                return money
        else:
            print("Out of Cash")
    def cashin(self,deposit_money):
        self.cash=self.cash+deposit_money
    def show_cash(self):
         print(self.cash)
         
class customer(Atm):
    def __init__(self,name,balance):
        self.name=name.upper()
        self.balance=balance
    def withdraw(self,pin,money):
            if self.balance>=money:
                status=self.cashout(pin,money)
                if status=="Out of cash" or status=="Invalid Pin":
                     return status
        
    
            else:
                Customer.balance-=money
                return status
    def deposit(self,deposit_money):
        self.balance=self.balance+deposit_money

ATM=Atm()
Customer=customer("Savi",20000)
ATM.show_cash()
Customer.withdraw(3456,5000)
# Customer.deposit(2000)
# Customer.withdraw(3456,500)
print(Customer.balance)