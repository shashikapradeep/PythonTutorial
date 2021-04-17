class Dog:
 types = ['small', 'medium', 'large']

 def __init__(self, name):
  self.name = name

 @staticmethod                          # static methods can not access any class or instance methods
 def owner():                           # no parameter is passed by Python
   print(f"Owner is me")                # self.name can not be accessed

 @classmethod
 def getTypes(cls):                     # class methods receive class as first argument
  print(cls)                            #<class '__main__.Dog'>
  #cls.sleep()                           this can not be called as we need to pass the class object as first param
  cls.sleep(Dog('Casper'))              # this is the way we should call
  return cls.types

 def sleep(self):                       # these are class instance methods
  print(f"{self.name} is sleeping")


class Puppy(Dog):
 def eat(self):
   #print(f"His father({self._age}) feeds me")  can not access this as this is a private variable
   print(f"Puppy lives in ({self._city})")

dog = Dog("Casper")
print(dog.getTypes())

Dog.owner()                              #can access directly
dog.owner()                              #can access via object as well
