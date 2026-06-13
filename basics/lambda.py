#lambda args : expression

x = lambda a : a + 10
print(x(1))

"""
why lambda?
    anonymos function inside another function

lambda built in functions :
    map() : applies a function to every item in an iterable(list)
    filter(): 
    sorted():
"""

def myfunc(n):
  return lambda a : a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

#map()
nums =[1,4,3,2]
double = list(map(lambda x : x*2, nums))
print(double)


#filter
odd=list(filter(lambda x : x % 2 != 0 , nums))
print(odd)


#sorted()
ordred = sorted(nums,key= lambda x:x)
print(ordred)


