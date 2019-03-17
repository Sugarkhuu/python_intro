# Source:  

# https://www.datacamp.com/community/tutorials/functions-python-tutorial#args
# https://treyhunner.com/2018/04/keyword-arguments-in-python/
# https://www.youtube.com/watch?v=9Os0o3wzS_I

# Simple
def greet():
    print("Hello Py4Econers!")


# run function before using


# 1 required argument
def greet_one(who):
    print("Hello " + who + "!")

greet_one('Tomor')


# 2 required arguments
def greet_two(who1, who2):
    print("Hello " + who1 + " and " + who2 +"!")

greet_two("Tomor", "Erdene")    

        # keyword arguments
        
greet_two(who2="Erdene", who1="Tomor")


# 3 required arguments
    
def greet_two_number(who1, who2, times):
    print("Hello " + str(times) + " times " + who1 + " and " + who2 +"!")

greet_two_number("Tomor", "Erdene", 100)    

    
# Default argument    
def greet_two_number_default(who1="Bat", who2="Damdin", times=1000):
    print("Hello " + str(times) + " times " + who1 + " and " + who2 +"!")

greet_two_number_default()
greet_two_number_default('Bayar')
greet_two_number_default(who2 = 'Bayar')


# Arbitrary number of arguments (positional and keyword)

# Arbitrary positional arguments and return
def mysum(*args):
    return sum(args)

mysum(13,12,11)

def myprint(*toprint):
    for a in toprint:
        print(a)

myprint(13,'heyhey',11, 'hihi')


# Arbitrary keyword arguments
def mypet(**kwargs):
    print("My pet is a {pet} and I call it {name}".format(name=kwargs['name'], pet=kwargs['pet']))

items = {'name': "Alag", 'pet': "horse"}
mypet(**items)

mypet(name='Khongor', pet='horse')

# Arbitrary arguments

def myargs(*args, **kwargs):
    print(kwargs)
    return sum(args)
    
    
    
    
# Output arguments

def mystat(a, b):
    return a*b, a+b

mystat(3,2)
prod, sum = mystat(3,2)

