class Dog:
 def __init__(self, name):
  self.name = name
  self.__age = 50          # private is made with __
  self._city = "Kiribathgoda"
  print(name)

 def sleep(self):
  print(f"{self.name} is sleeping")

 # when a private modifier is added this is the way to set and get a private variable
 def getAge(self):
   return self.__age

 def setAge(self, age):
   self.__age = age

class Puppy(Dog):
 def eat(self):
   #print(f"His father({self._age}) feeds me")  can not access this as this is a private variable
   print(f"Puppy lives in ({self._city})")

dog = Dog('Casper')
dog.sleep()
#dog.__age = 50 # this is not a private variable but a new variable. to make a variable Private it should be in a class
__legs = 4 # this has no meaning of private modifier
#print(f"dog is {dog.__age} years old") # since this is a private variable unable to get value
print(f"dog has {__legs} legs")

dog.setAge(6)
print(f"dog is {dog.getAge()} years old")

puppy = Puppy('Pepper')
puppy.eat()

print(f"Dog lives in {dog._city}") # this is a loop hole in Python. Normally protected modifiers should not be accessible from outside but inherited classes.
print(f"Puppy lives in {puppy._city}") # this is a loop hole in Python. Normally protected modifiers should not be accessible from outside but inherited classes.
