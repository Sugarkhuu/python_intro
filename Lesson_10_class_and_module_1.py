#Source
#https://docs.python.org/3/tutorial/classes.html
#https://www.w3schools.com/python/python_classes.asp
#https://www.learnpython.org/en/Classes_and_Objects

class Budget:
    
    def __init__(self, name, income, expense):
        self.name     = name
        self.income   = income
        self.expense  = expense
    
    def balance(self):
        return self.income - self.expense
    
    def interest(self, int_rate):
        return self.balance()*(1+int_rate/100)


class newBudget:
    
    citizenship = 'Mongolian'
    
    def __init__(self, name, income, expense):
        self.name     = name
        self.income   = income
        self.expense  = expense
    
    def exp_to_inc(self):
        return self.expense/self.income
    
def greet_one(who):
    print("Hello " + who + "!")
    
    
### Examples and os, sys    

# Object construction

BatBudget     = Budget('Bat', 100, 70)

ChimegBudget  = Budget('Chimeg', 500, 300)

BatBudget     = newBudget('Bat', 100, 70)


# os
import os

os.getcwd()
os.chdir('C:\\Users\\Sugar2\\Documents\\py\\Python intro')

# sys
import sys
sys.path
sys.path.append('C:\\Users\\Sugar2\\Documents\\py\\Python intro')
sys.path.remove('C:\\Users\\Sugar2\\Documents\\py\\Python intro')


# import
import Lesson_10_class_and_module_1
from Lesson_10_class_and_module_1 import Budget
from Lesson_10_class_and_module_1 import *


import Lesson_10_class_and_module_1 as l10
