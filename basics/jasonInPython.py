import json

#some json
x=' { "name" : "amira" , "age" : 22 , "city" : "algiers" } '

print(x)
#parse  make it into a dictionary

y=json.loads(x)

print(y)

#from python to json

x = json.dumps(y,indent=4,separators=(".","="),sort_keys=True)#indent and separators not nessesary but to make it readable

print(x)

"""
all these can be converte to json
dict becomes object 
list --> array
tuple --> array
str --> sring
int --> number
float --> number
True -->true
False --> false
None --> null
"""