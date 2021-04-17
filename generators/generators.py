#list and data structures are iterable
# generators are used to make that kind of iterables

#folliwing is inefficient when deal with millions of numbers. It slows things down.
def getOddNumbers(number):
 odds = []
 for i in range(0, number):
  if i % 2 == 1:
   odds.append(i)
 return odds

x = getOddNumbers(30)
print(x)

#efficient way is new method called yield()
def getOddNumbersYield(number):
 for i in range(0, number):
  if i % 2 == 1:
   print("odd => ", i)
   yield i

x = getOddNumbersYield(30)
print(x)                #returns a generator

for i in x:
 print(i)

'''
 real-world example is that reading a log file or huge file line by line. Then when need to print all the lines we dont need to keep everything in memory and
 this makes the most efficient way to handle that in memory. memory uses when iterating the generator and once one iteration is done memory wipes.
'''

print(x)
for i in x:
 print(i)          #print nothing. reason is that once you generate a generator and iterate it then it destroys. So you have to regenerate it or reset it.


