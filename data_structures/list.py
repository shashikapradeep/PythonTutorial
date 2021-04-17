a = [12,332,5432,15];

print(a, a[3]);
#print(a[10]);      IndexError: list index out of range

a[3] = 333;
print(a, a[3]);

a.append(400); #add a value to end of list

#a[10] = 555; this gives error as the list has np 10 items

a.insert(4, 450);
print(a);
a.remove(12); #element. not index
print(a);
a.pop(3);
print(a);

#lists can be added together
b=['Hello', 'world'];
print(a +b);

#print(a-b) invalid. impossible

#in always gives a boolean value
z=a+b;
is_12_in_z= 12 in z;
is_12_not_in_z= 12 not in z;

print(is_12_in_z, is_12_not_in_z);
