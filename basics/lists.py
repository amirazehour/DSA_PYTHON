
#ordred
#changable
#allow duplicates
mylist = ["amira", "zehour" , "gouigah","amira"] # order won't change
difflist = ["abc",123,True]
print(mylist)
print(difflist)

listFromTuple = list(("abc",123,True))

print(len(mylist))
print(difflist == listFromTuple)


"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""


# to start from the end use negative indexing

print(mylist[1:3])
print(mylist[:3])
print(mylist[2:])

if "amira" in mylist :
    print("this is amira")

mylist[3] = "hello"
mylist[1:3]=["gouigah","zehour"]
print(mylist)
mylist[1:3]=["zehour"]
print(mylist)

#to add in a specific position else use append array lenght will inc by 1 (we're not replacing)
mylist.insert(2,"zip zip zop")
print(mylist)


#extend can also use append in a for loop or  just an addition +
difflist.extend(mylist)
print(difflist)

# can add a tuple to a list 

difflist.remove("amira")
print(difflist)

difflist.pop(5)
print(difflist)
del difflist[0]
print(difflist)
del difflist #this delets it comlpletly use clear() to clear only 
# print (difflist) will give undifined err


#loop
for e in mylist:
    print(e)

#loop on index
for i in range(len(mylist)):
    print(i)

i=0
while i<len(mylist):
    print("looping")
    i+=1

#list comprehension
[print(x) for x in mylist]
newlist = [x for x in mylist if x!="amira"] # condition can be omitted
print(newlist)

[print(x) for x in range(10) if x!=5]

mylist.sort(reverse=True) #without reverse is ascending
print(mylist)
mylist.sort(key=str.lower)#to make sort case insensitive(it is case sensitive by default)



#customised sort
def myfunc(n):
    return abs(n-50)


numlist = [10 , -50 , 100 ,-3 , 80]
numlist.sort(key =myfunc)
print(numlist)

numlist.reverse()

#to coppy list use copy() or list() or list[:] aka slicing to not copy pointer but values

#index() return the index of the first element with specific 