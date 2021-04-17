# this is single line comment
"""
multipl line comments
"""

#doc string - this is to describe a function. There are many doc strings and identifying plugins for IDE
def comment(x, y, z):
 '''
  this is a function does something
  @param x: first number
  @param y: second number
  @param z: third number
 '''
 return x + y + z

comment(10,20,30)


#type hinting & return type
def commentTypeHint(x:int, z:str, a:dict, y:float=0.5) -> dict:  # default arguments must come at the end
 return a

x = {'name': ['Shashika'], 'age':37}
z = commentTypeHint(1,"hello", x, 2)
print(z)
