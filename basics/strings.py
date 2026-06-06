#multiple line str
x="""
hello
my name is amire
i'm 22 yo
"""

print(x)

#like arrays
a = "Hello, World!"
print(a[1])

#looping throught strings
for x in "banana":
  print(x)

#lenght
print(len("amira"))

#check in
txt = "i'm doing a master in AI"
print("AI" in txt)
if "master" in txt :
  print("she is a master student")
if "bashelor" not in txt :
  print("she isn't a bashelor student")


#slicing
b="Hello, world ! "
print(b[2:5]) ## lo 5 not included
print(b[:5]) ## hello
print(b[2:]) ##llo world ! 
print(b[-5:-2]) #ld  (start from end)


#upper/lower case and remoce white space at the begining and end
print(b.upper())
print(b.lower())
print(b.strip()+"a")

#replace 
print(b.replace("H","J"))

#SPLIT
print(b.split(","))

#concatenate with + (can't concatenate string and int with +)
#f-string is a way to format strings a place holder can contain a math opp like +
age=22
txt=f"my age is {age:.2f}"#{} is a palce hoder for a var named age  .2f for floating values
print(txt)


#escape illigal chars in the string add \ ()
print("abc \" defg")
print("abc \\n efg")
print("abc \r efg")
print("abc \t efg")
print("abc \befg")
print("abc \f efg")
print("abc \124 efg")
print("abc \x23 efg")

