#key value pairs

x = {'name': 'Shashika', 'age':37};
print(x);

x['name'] = 'Shashika Pradeep';
print(x);

print(x.keys(), x.values()); #gives keys and values of a dictionary

x['name'] = {'first_name': 'Shashika', 'last_name': 'Mahindapala'};
x['marks'] = [88, 90, 45, 60];
print(x);

#print(x[0]); gives error as this is not a list.

print(x.get('name').get('first_name')); # this is how a key value is found

del(x['age']);   # delete one pair
print(x);

x.clear(); # clear all
print(x);

x = {'name': ['Shashika'], 'age':37};
y=x['name'];
z=x['age'];             # this is pass by value as this is a primary/basic data type. So although the variable is changed original value stays same.
y.append('Pradeep');    # this is pass by reference as this is not a primary/basic data type. So when assigned variable is modified the referenced value will be affected.
print(x);

z = 38;
print(x);

#dict එකක් list එකකට convert කල විට එහි keys පමණක් ලැබේ.
my_dict = {
    "Colombo": 'කොළඹ',
    "Kandy": 'නුවර',
    "Galle": 'ගාල්ල',
    "Negombo": 'මීගමුව'
}

output = list(my_dict)
print(output)
