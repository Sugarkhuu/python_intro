# Source
# https://www.w3schools.com/python/python_conditions.asp


my_pet = "Dog";


# Plain IF

if my_pet == "Cat":
    print("You have a cat")

# else
 
if my_pet == "Cat":
    print("You have a cat")
else:
    print("You don't have a cat, but a " + my_pet + "!")


# if not equal    
    
if my_pet != "Cat":
    print("You don't have a cat!")
else:
    print("You have a cat!")
    
# else if 
    
a = 200
b = 33
c = 50

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
  print("a is greater than b")    

# if in one line
  
if a > b: print("a is greater than b")

# if else in one line

print("A") if a > b else print("B")

# if else if in one line

print("A") if a > b else print("=") if a == b else print("B")

# if not

if not a < 100:
    print("a is not a grade!")
else:
    print("a is a grade!")

# and or

if c > b and c > a:
  print("c is the largest")


if c > b or c > a:
  print("c is not the least")
  
if not c > b or c > a:
  print("c is not the least")
  
  
# More examples

# in list
my_friends = ["Bold", "Bat", "Bayar"]

a_person = "Gan"

if a_person in my_friends:
    print(a_person + " is your friend!")
else:
    print(a_person + " is not your friend!")
    
if a_person in my_friends:
    print(a_person + " is already your friend!")
else: 
    my_friends.append(a_person)
    print("New friend " + a_person + " was added!")


# operation
    
if a - b > 0:
    print("a is larger than b")
elif a-b < 0:
    print("b is larger than a")
else:
    print("a and b are equal")

# assign
    
if a > 60:
    grade = "pass"
else:
    grade = "fail"
    
print(grade)


# switch  case

def switch(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)

# function name to gift    
def gift(x):
    return {
        "boy": 'bike',
        "girl": 'barby',
         "woman": 'drone',
         "man": 'motorbike'
    }.get(x, "cake")
    
    




