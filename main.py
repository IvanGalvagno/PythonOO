# from pythonOOexample.math.calc import calc_sum
# from pythonOOexample.string.str import hello

# calc_sum(2,2)
# hello()

from car import Car

carro1 = Car()
print(carro1.name)
print(carro1.color)
carro2 = Car()
carro2.name = 'A200'
carro2.color = 'Gray'
print(carro2.name)
print(carro2.color)
print(carro1.maker)
print(carro2.maker)
carro2.maker = 'Mercedez-Benz'
print(carro2.maker)
