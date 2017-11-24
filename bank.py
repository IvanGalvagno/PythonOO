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

#Herança
class Bank1Account(object):
    def __init__(self,number):
        self.__number = number
        self.__total = 0
    
    def deposit(self, value):
        self.__total += value
    
    def withdraw(self,Value):
        self.__total -= Value
        #Cobra Taxa
        self.__total -= 1
    
    def getTotal(self):
        return self.__total



#Herda tudo da classe Bank1Account sem re-escrever o codigo
class Bank2Account(Bank1Account):
    def __init__(self, number, cvv):
        super(Bank2Account,self).__init__(number)  #Acesso a classe pai e passando o valor assim podendo atribuir valor a cvv
        # lINHA ACIMA | EXECUTOU O METODO DO PAI PARA PODER SOBREESCREVER 
        self.cvv = cvv
    

    def withdraw(self,Value):
        self._Bank1Account__total -= Value
        #Cobra Taxa maior
        self._Bank1Account__total -= 2


class TesteCommitPush(object):
    print("Hello Commit")