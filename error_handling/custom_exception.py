#make custom exception class simple
class InvalidAgeException(Exception):
 def __init__(self, error):
  super(InvalidAgeException, self).__init__(error)
  self.error_code = 10

class Person:
 def __init__(self, name):
  self.name = name

 @staticmethod
 def getPerson(name):
  if not name:
   raise Exception('Invalid name')
  return Person(name)

 def calculateAge(self):
    if not age:
      raise InvalidAgeException("Invalid Age")

try:
 person = Person.getPerson('Shashika')
 print(person)

 person.calculateAge()

except InvalidAgeException as e:
 print("Error Age", e)
except Exception as e:
 print("Error Occurred => ", e)
