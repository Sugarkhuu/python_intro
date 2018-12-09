# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:15:19 2018

@author: Sugar2
"""

# https://www.tutorialspoint.com/python/python_strings.htm

# "" and '' are the same

my_str = "Hello World!"
str1 = ''

#Basics

my_str.replace('o','y')

my_str[4]
my_str[0]
my_str[0:1]
my_str[0:5]
my_str[2:5]
my_str[-1]
my_str[-2]
my_str[0:-2]
my_str[20]
my_str[-7]
my_str[-10]
my_str[-11]
my_str[9]

#Legnth and others

len(my_str)
max(my_str)
min(my_str)

# Strip

str = "0000000wow l daa!!!0000000";
print(str.strip( '0' ))

# Up down

my_str.upper()
my_str.lower()
my_str.capitalize()
my_str.title()


#Repeat
my_str * 5

# Reverse
#my_str[1:5:2]
my_str[::-1]

#Membership in or not in

my_str in (my_str, 'Chiher', 'Jims')

my_word = 'World'

my_str.find(my_word,0)
my_str.index(my_word,0)


# string format operator %

dog_1 = 'Асар'
dog_2 = 'Басар'
event = "амьдран суудаг байжээ."

print("%s, %s %d %s" %(dog_1, dog_2, 2, event))


# Split

str = "Бат-Эрдэнэ Баяр-Эрдэнэ Оюун-Эрдэнэ";
str.split()
str.split(' ')
str.split("-")


#Join

str3 = str1 + my_str
print(str3)
str3 = str1 + " " + my_str

seq = ("Бат", "Эрдэнэ")
s = "::"
s.join(seq)


#Conversion to string

pi = 22/7
print("Пи тоо нь ойролцоогоор " + str(pi) + "-тай тэнцүү.")








