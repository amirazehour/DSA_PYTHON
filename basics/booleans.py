print(bool("Hello"))
print(bool(15))
print(bool(""))

#class with __len__ that return 0/false evaluates to false
class myclass():
    def __len__(self):
        return 0 #or false

myobj = myclass()
print(bool(myobj))

x=100
print(isinstance(x,int))

#opperators
# % mod
# / div
# // floor division

#walrus opperatoe
print(x := 3) 
#same as 
x = 3
print(x)

num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)

x = 5

print(1 < x < 10)



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x


#they have to point at same object to be true while == same value
print(x is z)
print(x is y)
print(x == y)


fruits = ["apple", "banana", "cherry"]

#membership operator
print("banana" in fruits)
# XOR x ^ y Sets each bit to 1 if only one of two bits is 1
#~x NOT

#Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2



#Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2


#()> ** > +X -X ~X > *  /  //  % > +  - > >> << > & > ^ > (==  !=  >  >=  <  <=  is  is not  in  not in)  > NOT> AND > OR