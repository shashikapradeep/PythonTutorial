class Dog:
 pass

dog = Dog()
print(dog)       #<__main__.Dog object at 0x7fa33ffeafd0>

dog.name = 'Casper'
dog.breed = 'Labrador'

print(dog.name, dog.breed)


class Cat:
 def walk(self):         # since object is passed in to the method first argument accepts it and we define it as self
  print('inside', self)

cat = Cat()
cat.walk()              # by default python passes object to the class method
print('outside', cat)


#self attribute

class Bird:
 def setName(self, name):
  self.name = name
 def walk(self):         # since object is passed in to the method first argument accepts it and we define it as self
  print(f'It walks & name of it is {self.name}')

bird = Bird()
bird.setName("Peththa")
bird.walk()


#constructor

class Elephant:
 def __init__(self, name):
  self.name = name
  print("inside constructor")

 def walk(self):
   print(f'It walks & name of it is {self.name}')

elephant = Elephant('Kandula')
#elephant.name = "Pandula"
elephant.walk()
