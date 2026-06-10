#pythoon decorators
def changecase(func):
   def inner(*args, **kwarg):
      return func(*args, **kwarg).upper()
   return inner #notice we return a function

@changecase
def myfunc(x):
   return x

print(myfunc("amira"))



#decorrators can have arguments
def changecases(x):#OUTER HAS ARGUMENT
   def changecase(func):#INER HAS THE FUNCTION
    if x==1:
        def inner(*args,**kwargs):
            return func(*args,**kwargs).upper()
    else:
       def inner(*args,**kwargs):
            return func(*args,**kwargs).lower()
       
    return inner
   return changecase



#WE CAN HAVE MULTIPLE DECORATORS
def greeting(func):
   def inner(*args,**kwargs):
      return "hello "+ func(*args,**kwargs)
   return inner
        
@changecases(1)
@greeting
def myfunc(x):
   return x

print(myfunc("Amira"))




#function meta data
"""
    useally we can get function name using myfunction.__name__
    but ot with decorators it will get inner instead of the acctial function name

"""

import functools

#decorrators can have arguments
def changecases(x):#OUTER HAS ARGUMENT
   def changecase(func):#INER HAS THE FUNCTION
   
    if x==1: 
        @functools.wraps(func)
        def inner(*args,**kwargs):
            return func(*args,**kwargs).upper()
    else:
       @functools.wraps(func)
       def inner(*args,**kwargs):
            return func(*args,**kwargs).lower()
       
    return inner
   return changecase



#WE CAN HAVE MULTIPLE DECORATORS
def greeting(func):
   @functools.wraps(func)
   def inner(*args,**kwargs):
      return "hello "+ func(*args,**kwargs)
   return inner
        
@changecases(1)
@greeting
def myfunc(x):
   return x

print(myfunc.__name__)

