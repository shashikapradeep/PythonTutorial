a = [20,54,66,82,100,23]
b=a
c=list(a)          #make a copy of a, pass by value
b.append(500)
print(a,b,c)       #[20, 54, 66, 82, 100, 23, 500] [20, 54, 66, 82, 100, 23, 500] [20, 54, 66, 82, 100, 23]

#make a same copy of a list and assign to x in primary way
x = []
for i in a:
 x.append(i)
print(x)                 #output [20, 54, 66, 82, 100, 23, 500]

#one line of code above code
y=[i for i in x if i > 50]
print(y)                 #output [54, 66, 82, 100, 500]

#one line of code above code
y=[i*2 for i in x if i > 50]
print(y)                 #output [108, 132, 164, 200, 1000]


def changeVal(x):
 return x+50
#one line of code above code
y=[changeVal(i) for i in x if i > 50]
print(y)                 #output [104, 116, 132, 150, 550]

#make dictionary list with comprehension
def isOdd(number):
 return "Odd" if number % 2 == 1 else 'Even'

z = [ {value:isOdd(value)} for i,value in enumerate(x) if i % 2 == 0]
print(z)

#make dictionary with comprehension
z = { value:isOdd(value) for i,value in enumerate(x) if i % 2 == 0 }
print(z)

#make a set
z = {value for i,value in enumerate(x) if i % 2 == 0}
print(z)

#make a tuple
z = (value for i,value in enumerate(x) if i % 2 == 0)
print(z)                    #<generator object <genexpr> at 0x7fcf34325ac0>

for i in z:
  print(i)
'''
20
66
100
500
'''
