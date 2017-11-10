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


#Modificador de Acesso
class Account1:
    def __init__(self,number,total):
        self.__number = number
        self.__total = total
    
    def deposit(self, value):
        self.__total += value
    
    def withdraw(self,Value):
        self.__total -= Value
    
    def getTotal(self):
        return self.__total

    def getNumber(self):
        return self.__number