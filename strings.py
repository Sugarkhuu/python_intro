# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:15:19 2018

@author: Sugar2
"""

# https://www.tutorialspoint.com/python/python_strings.htm


str1 = "Hello World!"
str2 = 'Hi Mongol!'

str1.replace('o','y');
str2.replace('l', 'lians')

print(str1, "\n",str2)

str2[4]
str2[0]
str2[0:1]
str2[0:5]
str2[2:5]
str2[-1]
str2[-2]
str2[0:-2]
str2[20]
str2[-7]
str2[-10]
str2[-11]
str2[9]

#Attach
str3 = str1 + str2
print(str3)
str3 = str1 + " " + str2

#Repeat
str2 * 5

# Reverse
str2[1:5:2]
str2[::-1]

#Membership not in
str2 in (str2, str1)


# string format operator %
# make 2 in string
dog_1 = 'Асар'
dog_2 = 'Басар'
event = "амьдран суудаг байжээ."

print("%s, %s %d %s" %(dog_1, dog_2, 2, event))


pi = 22/7

print("Пи тоо нь ойролцоогоор " + str(pi) + "-тай тэнцүү.")


len(str2)
count(str2,1,5)
max(str2)
min(str1)

hi = 'Hi'

str2.find(hi,0)
str2.index(hi,0)

seq = ("Бат", "Эрдэнэ")
s = "-"
s.join(seq)

str = "Бат-Эрдэнэ \nБаяр-Эрдэнэ \nОюун-Эрдэнэ";
str.split()
str.split(' ', 1 )
str.split("-")

str = "0000000this is string example....wow!!!0000000";
print(str.strip( '0' ))

str.upper()
str.lower()

str = "batbayar from Golomt Bank"
str.capitalize()
str.title()

from string import maketrans   # Required to call maketrans function.

input = "aeiou"
output = "12345"
tran = maketrans(intab, outtab)

str = "this is string example....wow!!!";
str.translate(trantab)




#!/usr/bin/python

from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
str.translate(trantab, 'xm')








