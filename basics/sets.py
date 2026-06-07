
#unordred => no index or key
#unchangeable  =>  cannot change the items can only add or remove
#no duplicate => will store them as one ture is 1 false is 0 (duplicates)
myset={"amira" , "zehour","gouigah"}

myset.add("hello")

newset = {"abc",123}
mylist = [True,False]
myset.update(newset)
myset.update(mylist)
myset.remove(True)#raise an error if item doesn't exist
myset.discard(True)#doesn't raise an error
x= myset.pop()#remove randomly
print(myset ,x)
myset.clear()



"""
Join Sets
There are several ways to join two or more sets in Python.

The union() | and update() methods joins all items from both sets.

The intersection() & method keeps ONLY the duplicates.
intersection_update() will put intersection in 1st set

The difference() - method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() ^ method keeps all items EXCEPT the duplicates.

opperators like | & ^ - + only aplicable on 2 sets + the methodes can be used on diff structures/ datatypes

"""


#frozen sets 
#not able to add or remove 
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
#suports things like isdisjoint() ,issubset()<= | < , issuperset() >= | >
#it is imutable
