#Source 
#https://docs.python.org/3/tutorial/classes.html


class person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def getPerson(self):
        return self.firstname + " " + self.lastname

aPerson = person("Balgan", "Horloo")


# Simple inheritance

class employee(person):

    def __init__(self, first, last, staffnum):
# person or super()       
        person.__init__(first, last)
        self.staffnumber = staffnum

    def getEmployee(self):
        return self.getPerson() + ", " +  self.staffnumber

bEmployee = employee("Yunden", "Nansalmaa", "1007")


# Multiple inheritance

class credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class private(person, credentials):
    def __init__(self, first, last, username, password):
        person.__init__(self,first, last)
        credentials.__init__(self,username, password)
    
    def getPrivate(self):
        pin = input('Enter PIN: ') 
        if pin == 'huvsgul':
            print(self.username + " " + str(self.password))
        else:
            print("Wrong PIN!")

myPerson = private('Sanj', 'Bayar', 'sanjka', '1234')

# New attribute

myPerson.fColor = "Green"

def toUpper(word):
    print(word.upper())

def toCap(word):
    print(word.capitalize())    

    