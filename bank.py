class Account:
    def __init__(self,number,total):
        self.number = number
        self.total = total
    
    def deposit(self, value):
        self.total += value
    
    def withdraw(self,Value):
        self.total -= Value
    
    def getTotal(self):
        return self.total