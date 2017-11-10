# from pythonOOexample.math.calc import calc_sum
# from pythonOOexample.string.str import hello

# calc_sum(2,2)
# hello()

# from car import Car

# carro1 = Car()
# print(carro1.name)
# print(carro1.color)
# carro2 = Car()
# carro2.name = 'A200'
# carro2.color = 'Gray'
# print(carro2.name)
# print(carro2.color)
# print(carro1.maker)
# print(carro2.maker)
# carro2.maker = 'Mercedez-Benz'
# print(carro2.maker)

# from car import Car1

# carro1 = Car1('GTR','Nissan',2019)
# print(carro1.name)
# print(carro1.maker)
# print(carro1.year)
# print(carro1.name, carro1.year)
# carro1.start()
# carro1.hello()
# carro1.show()

# from bank import Account

# acc = Account('2345-5',300)
# print('Account number: ', acc.number)
# print('$', acc.total)
# acc.deposit(50)
# print(acc.total)
# acc.withdraw(50)
# print(acc.getTotal())

# from bank import Account1

# acc1 = Account1('854-9',500)
# print(acc1.getTotal())

# acc = Account1(222)
# acc.__class__
# type(acc)

from bank import *

# acc.__class__
# type(acc)

acc1 = Bank1Account('123-0',0)
acc2 = Bank2Account('456-0',0)
acc1.deposit(100)
acc2.deposit(100)
acc1.withdraw(50)
acc2.withdraw(50)
print(acc1.getTotal())
print(acc2.getTotal())


