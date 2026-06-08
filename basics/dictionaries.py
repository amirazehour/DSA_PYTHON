
#ordred from py 3.7 and up
#changeable
# no duplicate allowed (will overwrite) in key name
thisdict={
    "name" : "amira zehour",
    "birthYear" : 2004,
    "lastname" : "gouigah",
    "university" : "USTHB "
}

print(thisdict)
x=thisdict["name"]
x=thisdict.get("name")#same results
print(thisdict["name"])

x=thisdict.keys()
print(x)

thisdict["birthMonth"]=6
print(x)

x=thisdict.values()
print(x)

x=thisdict.items() #each item as a tuple
print(x)

if "name" in thisdict:
    print(thisdict["name"])

thisdict.update({"name2":'apple'})

thisdict.pop("name2")
thisdict.popitem()#remove last added item\


for x in thisdict:
    print(x)

for x in thisdict.values():
    print(x)

for x in thisdict.items():
    print(x)

thisdict.clear()
del thisdict #thisdict nolonger exists


#neste dictionaries

DictClass = {
    "student1":{
        "name":"amira",
        "age":22  
    },
    "student2":{
        "name":"maria",
        "age":21 
    }
}
print(DictClass)
print(DictClass["student1"]["name"])

for x, obj in DictClass.items():
    print(x)
    for y in obj:
        print(obj[y])



#Create a dictionary with 3 keys, all with the value 0:

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)



#defdault values 
car = {
  "brand": "Ford",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)