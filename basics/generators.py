#functions that can pause and resume their execution
#return a generator object 
#which is an iterator


def mygen():
    yield 1
    yield 2
    yield 3

for val in mygen():
    print(val)

#alow to iterate throught data without storing
#ecerything in the memory

"""
When yield is encountered
 the function's state is saved, t
 and the value is returned. 
 The next time the generator is called, 
 it continues from where it left off.
"""

def countto(n):
    count = 1
    while count<=n:
        yield count
        count+=1

for num in countto(5):
    print(num)

#unlike return yield doesn't terminate the function just pause it
#so instead of storing everything a generator generates data onthe fly



def large_seq(n):
    for i in range(n):
        yield i

gen = large_seq(10000000)#this doesn't create 1000000 num in memory
print(next(gen))#next is used to manualy iterate
print(next(gen))
print(next(gen))


def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
# print(next(gen)) # This will raise StopIteration


gen_exp = (x*x for x in range(5))#same as list compresion but list with [] and gen with ()
print(gen_exp)
print(next(gen_exp))
print(next(gen_exp))

total = sum(x*x for x in range(4))
print(total)


#generate a febonacci sequence
def febonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,b+a

gen = febonacci()

for _ in range(20):
    print(next(gen))



def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

#to stop the generator 
gen.close()

