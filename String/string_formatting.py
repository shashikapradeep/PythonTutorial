name='shashika'
age=37
height=3.5

#basic (string concatenation)
print('Hello ' + name + ', you are ' + str(age) + ' years old')

#c type (percentage formatting)
print("Hello %s, you are %d years old" % (name, age))          #a tuple is used
print("Hello %s, you are %f height!" % (name, height))          # print as a float
print("Hello %s, you are %.2f height!" % (name, height))          #round to two decimals
print("Hello %s, you are %05d height!" % (name, height))          #fix length of numbers in decimals

#format
print("Hello {}, you are {} old!".format(name, age))          #fix length of numbers in decimals
print("Hello {0}, you are {1}({0}) old!".format(name, age))          #fix length of numbers in decimals
print("Hello {}, you are {:05d} old!".format(name, age))          #fix length of numbers in decimals
print("Hello {0}, you are {1:05d}({0}) old!".format(name, age))          #fix length of numbers in decimals

'''
Hello shashika, you are 37 years old
Hello shashika, you are 37 years old
Hello shashika, you are 3.500000 height!
Hello shashika, you are 3.50 height!
Hello shashika, you are 00003 height!
Hello shashika, you are 37 old!
Hello shashika, you are 37(shashika) old!
Hello shashika, you are 00037 old!
Hello shashika, you are 00037(shashika) old!
'''

#f string formatting
print(f"Hello {name}, you are {age:05d}({name}) old!") #Hello shashika, you are 00037(shashika) old!
print(f"Hello {len(name)}, you are {age:05d}({name}) old!") #Hello 8, you are 00037(shashika) old!
