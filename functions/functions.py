def getGreeting():
 print('Hello')
getGreeting()

def getGrade(marks):
 if marks>75:
  print('Grade A')
 else:
  print('Grade B')
getGrade(70)


def getGradeWithSubject(marks, subject='Unknown'):
 print('You have got '+str(marks)+' for '+subject)
getGradeWithSubject(50)


#named arguments
def getFoodList(food, price):
 print(food+":"+str(price))

getFoodList(food="banana", price=50)
getFoodList("Mango", price=80)
#getFoodList(food="banana", 50)   if started from named argument then next one also must be a named argument
getFoodList(price=80, food="banana")

def marks(*marks):
 print(marks)              #makes a tuple of marks
marks(30,45,64,23,100)

def myForm(**formData):
 if 'city' not in formData:
  print("Error! City is required")
 print(formData)
myForm(name='Shashika', age='37', city='Kiribathgoda')        #makes a dictionary
myForm(name='Shashika', city='Kiribathgoda')
myForm(name='Shashika', age='37')

def myMarksForm(*marks, **formData):
 if 'city' not in formData:
  print("Error! City is required")
 print(marks, formData)

myMarksForm(23, 60, 80, name='Shashika', age='37')    #positional argument always come first before the named arguments.


#dictionary to named arguments
def myFormData(name, city, age, country='Sri Lanka'):
 print(name, city, age, country)

data = {'name': "Shashika", 'city': "Kiribathgoda", 'age':37}
myFormData(**data)

#return
def gradeValue(marks, subject=None):
 if not subject:
  return
 print(marks, subject)

gradeValue(80)
gradeValue(80, 'Science')

#return and assign
def familyMember(name, age, familyMember='Unknown'):
   return name, age, familyMember                         # returns a tuple
member = {"name":"Shashika", "age":37}
name, age, person = familyMember(**member)
print(name, age, person)
