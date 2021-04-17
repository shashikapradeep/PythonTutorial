#non duplicate data set
#if we want to extract distinct values then use a set data structure
# case sensitive
# KULAKA

x = {'hello', 'world'}
x.add('world');
print(x);

x.add('World');           #hash function is used
print(x);

y={'A', 'B'};

#print(x['hello'], x[0]); # invalid TypeError: 'set' object is not subscriptable
#print(x+y);   #error TypeError: unsupported operand type(s) for +: 'set' and 'set'

print(x.union(y), x | y)        # this is how two sets are combined

print(x-y); #this can be used to remove one set from another set. ex: remove corona affected cities from all cities in SL.

print('hello' in x, 'world' not in y); #check existence of a key


