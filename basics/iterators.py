#strings ,list ,tuples , dictionaries ,sets are iterables
#theyompemnt iter and next

mytuple = ("amira","zehour","gouigah")
myit= iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


#loopimg in an iterable
for x in mytuple:
    print(x)


"""
create an iterator object /class

    you have to implement  __iter__() and __next__() to your object 
    and all classes need a function called __init__() 
        which allow you to do some initialization when the object is being created
    __iter__() act similar but alway return an object iterator
    __next__() must return the next item in the sequence
    use StopIteration statement to stop next so it doesn't iterate forever
"""


class numbers:
    def __iter__(self):
        self.a =1
        return self
    def __next__(self):
        # if self.a>10:
        #     raise StopIteration (will raise an error)
        x = self.a
        self.a +=1 
        return x
    
mynums=numbers()
myiter=iter(mynums)
for i in range(11):
    print(next(myiter))

