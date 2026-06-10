#naming
"""
myFnction()
_private_function()
myfunction2()
"""


#arguments
def my_function(abc="zehour"):# default parameter
    print(abc)

my_function("amira")#argument
my_function()
my_function(abc="gouigah")#when mixing keywird and positional argument



import random
def tuple_func():
    return (random.randrange(0,10),random.randrange(10,20))

x,y = tuple_func()
print(x,y)

def only_positional(abc,/):
    print(abc)
only_positional("positional")


def keywordsOnly(*,abc):
    print(abc)
keywordsOnly(abc="keyword")

def combined(a,b,/,*,c,d):
    return a+b+c+d

print(combined(10,5,c=2,d=3))


"""
 *args **kwargs
 args becomes a tuple containing all the passed arguments
 kwargs becomes a dictionary containing all the keyword arguments
 he order must be:
    regular parameters
    *args
    **kwargs
"""

def my_function(greeting,*args):
  print(greeting)
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("hello","Emil", "Tobias", "Linus")

def info(**person):
    print(person["fname"])

info(fname="amira",fname2="zehour",lname="gouigah")


#unpacking a list into arguments
elems=[1,2,4,5]
def sumfunc(*args):
    s=0
    for x in args:
        s=s+x
    return s

print(sumfunc(*elems))
#same with dictionaries and kwargs


"""

#scope
    #if x is defined in a function it is not reachable outside 
    #but it is in any function defined inside the function
    #we can have same name var in local nad global scope
    #python treats them as seprate variables
    # we already saw the global keyword
    # nonlocal key word:
        vars inside nested functions
        makes them belong to the outer function


    LEGB RULE
    local > enclosing > global > built-in
"""

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)
outer()
print("Global:", x)



