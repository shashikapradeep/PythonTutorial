#mix of all data types
# this is like a table row. various data types in a row

x=('shashika', 'mahindapala', 10, 1984);
print(x, type(x));
print(x[0], x.count('shashika'));

#items can not be removed. if want to remove this should be converted to a list.

name, last_name, age, year = x;  #number of variables should be equal to tuple items length

print(name, last_name, age);
