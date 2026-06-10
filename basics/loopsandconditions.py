a,b,c=False,True,False

if a:
    print("a is true")
elif b :
    print("b is true")
elif c:
    print("c is true")

d = "a" if a else "b" if b else "c"
print(d)


#combining multiple opp (not > and >or)

if a :
    pass #to not get an error incase logic still not implemented as place holder
    #or it's a case you want to isolate cuz no action needed
    #also used is functions ..ect





day = 4
match day:
    case 1|3|4:
        pass
    case 2 if a:
        pass
    case _:
        pass #default




while a :
    if b:
        b!=b
        continue
    break
else:
    pass #else will not execute if while stoped bt break statment



arr = ["a","b","c"]
for x in arr:
    print(x)
    if x == "b":
        break


for x in range(10):
    print(x)#from 0 to 9

for x in range(2,10):
    print(x)#from 2 to 9

for x in range (1,10,2):
    print(x)#increment by 2
else:
    print("finally finished")#no execution if loop stoped by break