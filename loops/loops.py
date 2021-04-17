#for

x = [12,32,45,23]
for i in x:
 print(type(i), i)

'''
<class 'int'> 12
<class 'int'> 32
<class 'int'> 45
<class 'int'> 23
'''

for i in enumerate(x):         #enumerate function returns a tuple
  print(type(i), i, i[0], i[1])

'''
<class 'tuple'> (0, 12) 0 12
<class 'tuple'> (1, 32) 1 32
<class 'tuple'> (2, 45) 2 45
<class 'tuple'> (3, 23) 3 23
'''

for key, value in enumerate(x):         #enumerate function returns a tuple
  print(key, value)

'''
0 12
1 32
2 45
3 23
'''

r = range(0, len(x))
for i in r:
 print(type(r), r, x[i])

'''
<class 'range'> range(0, 4) 12
<class 'range'> range(0, 4) 32
<class 'range'> range(0, 4) 45
<class 'range'> range(0, 4) 23

'''

count = 0
while True:
 if(count >= len(x)):
   break
 i = x[count]
 if i %2 == 0:
  count += 1
  continue
 print(i)
 count += 1
