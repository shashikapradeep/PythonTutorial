#this file should be run being in the folder itself

file = open('./../String/string_formatting.py')
#content = file.read()                           # read all lines
firstChars = file.read(1)
print(firstChars)

line = file.readline()
print(line)

for line, text in enumerate(file):
  print('Line: ', line, text)

file.close()                       # this is a must although it doesn't give any error but for security'.

#file write

'''
file opening modes

r = read only
w = write with truncate
x = open for exclusive creation
a = append
b = binary
t = text mode
+ = updating

'''

file = open('sample.txt', 'w')
for i in range(0,100):
 file.write(str(i))

file = open('sample.txt')
line = file.readline()
print(line)

file.close()

# join method to add , between two numbers
x = [str(i) for i in range(0, 100)]
msg = ', '.join(x)
file = open('sample.txt', 'w')
file.write(msg)

file = open('sample.txt')
line = file.readline()
print(line)

file.close()


# append
# join method to add , between two numbers
x = [str(i) for i in range(0, 100)]
msg = ', '.join(x)
file = open('sample.txt', 'a')
file.write(msg)

file = open('sample.txt')
line = file.readline()
print(line)

file.close()
