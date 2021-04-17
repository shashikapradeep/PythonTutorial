class Mammal:
 def feed(self):
  print('feeding..')

class Animal:
 def __init__(self, breed):
  print('Animal Constructor')
  self.breed = breed

 def walk(self):
  print('Animal walks')

 def talk(self):
  print('Animal talks')



class Dog(Animal, Mammal):
 def eat(self):
  print('Dog eat')

class Cat(Animal):
 def walk(self):         # overriding
  print('Cat walks')



dog = Dog('Dog')
print('Dog Walk => ', dog.walk())
print('Dog Talk => ', dog.talk())


cat = Cat('Cat')
print('Cat Walk => ', cat.walk())              # by default python passes object to the class method
print('Cat Talk => ', cat.talk())              # by default python passes object to the class method
print('outside')
