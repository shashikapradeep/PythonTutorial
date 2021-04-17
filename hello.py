print("hello world!");

name = "shashika";
city = "Kiribathgoda";

print(name);

a =10;
b = 3;

print(a+b);
print(a-b);
print(a/b);
print(a//b);
print(a**b);
#print(name+a);  this is invalid. String can not be added to an int
print(name+str(a)); #this is the way to concat a number to a string
print(name+city);
print((name+' ')*a);


d= True;
f= False;

print(d and f);
print(not f);
print(d or f);
print(d ^ f);
print(f);


print(type(d))
print(type(a))
print(type(name))

print(f, type(f)); #priny type of the variable

x,y=12, 'hello';
print(x, y);

#casting
print(bool(f), int(d));

print('Input your age : ', end=''); #end param stop going to next line to print the next line
answer = input();
print("You are "+answer+' old.')


