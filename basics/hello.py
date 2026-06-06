#portability
#simple syntax
#procedural + oop +functional

#print
print("Hello, World!")
print("Hello"); print("How are you?"); print("Bye bye!")
print("Hello World!", end=" ")
print("I will print on the same line.")
print("I am", 22, "years old.")

#comments 
"""
this is a multi
line 
commment
"""
#if statement
if 5 > 3:
    print("true")

#var
x=5
#python is case sensitive Age age are diff vars
"""
vars can't start with a number
cannot be any keyword
can only have underscore _ (place doesn't matter)
"""

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(x))

#multi var values 
x, y, z = "Orange", "Banana", "Cherry"

#one val mutiple vars
x = y = z = "Orange"

#unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits


#functions and global/local vars 
x = "awesome"

def myfunc():
  x = "fantastic"
  global y

  print("Python is " + x)

myfunc()

print("Python is " + x)

"""
data types 
Text Type:	str
Numeric Types:	int, float, complex 1j
Sequence Types:	list [], tuple () , range range(6)
Mapping Type:	dict x= {"name":"amira","age":22}  or x = dict(name="John", age=36)
Set Types:	set {}, frozenset frozenset({"apple", "banana", "cherry"})
Boolean Type:	bool
Binary Types:	bytes b"Hello", bytearray bytearray(5), memoryview memoryview(bytes(5))
None Type:	NoneType None

"""



#random
import random
print(random.randrange(1,10))


