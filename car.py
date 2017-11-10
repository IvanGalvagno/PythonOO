class Car():

    def __init__(self):
        self.name = 'A3'
        self.maker = 'audi'
        self.year = 2015
        self.color = 'green'

class Car1():
    x = 'abs'
    def __init__(self, name, maker, year):
        self.name = name
        self.maker = maker
        self.year = year

    def start(self):
        print(self.name + ' Started ' + self.name)
        
    #Metodo Estatico
    @staticmethod
    def hello():
        print('Hello from car')
    
    #Metodo com acesso ao atributos da classe mas nao com o da instancia
    @classmethod
    def show(cls):
        print(cls.x)
        #IF cls.name nao funciona

    