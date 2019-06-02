# Source
#https://www.w3schools.com/python/python_regex.asp
#https://www.tutorialspoint.com/python/python_reg_expressions.htm
#https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial
#https://www.rexegg.com/regex-lookarounds.html

word = 'geeks for geeks'
result = word.find('for') 

### WARM UP PART
import re

# 'search' - search in string (match)
x = re.search('in', 'The rain in Spain')
x.group()
# or simply
re.search('in', 'The rain in Spain').group() # show result
# you can define the string in an string object
str = 'The rain in Spain'
x = re.search('in', str)


re.search('in', 'The rain in Spain').start() # first index of match
re.search('in', 'The rain in Spain').end()   # last index of match
re.search('in', 'The rain in Spain').span()  # show indices

# 'findall' - print occurrences as a list
x=re.findall('a', 'The rain in Spain')

# 'sub' - replace in string
re.sub('n', 's', 'The rain in Spain')
re.sub('n', 's', 'The rain in Spain', 1) # only the first

# split - split string into pieces
re.split('i', 'The rain in Spain')

### Main part

# Metacharacters
#[] + * {} ? ! ^ $ | () .
# Special Sequences
# \ \A \b \B \d \D \s \S \w \W \Z
# Option Flags
#re.I re.M



# [] is a set. Search for any one of the characters in []
re.search('[0-9]', info).group()    # 0-9 <=> 0 1 2 3 4 5 6 7 8 9. Finding matching number from the string
# + means 1 or more match
re.search('[0-9]+', info).group()   # matches (first) up to a character which is not in the set
re.search('[a-z]+', info).group()   # matches (first) up to a character which is not in the set. from a to z
re.search('[a-zA-Z]+', info).group()   # matches (first) up to a character which is not in the set. from a to z and A to Z
re.findall('[0-9]+', info)          # all matches
re.search('[0-9-]+', info).group()  # including the dash '-'
# * means 0 or more match
re.search('[0-9-]+##*', info).group()  # Second "#" is not neccessary
re.search('[0-9-]+##+', info).group()  # Second "#" is not neccessary


# {} - how many times
re.search('[0-9]{3}', info).group()    # 3 times numbers between 0-9
re.search('[0-9]{3,5}', info).group()  # from 3 to 5 times numbers between 0-9
re.search('[0-9]{3,}', info).group()   # at least or more numbers between 0-9
# ? - character on the left at most one or no occurrence
re.search('[0-9]a?', info).span()      
re.findall('[0-9-]+a?', info)      

# ? - also can be used for lookbehind/lookahead
# lookbehind or look to the immediately preceding characters
re.search('(?<=-)[0-9]+', info).group()  # numbers which follow after '-'. 
re.search('(?<!-)[0-9]+', info).group()  # numbers which don't follow '-'  
re.split('(?<!-)[0-9]+', info)           # split at the numbers which don't follow '-'
# lookahead or look to the immediately following characters
re.search('[0-9]+(?=-)', info).group()  # numbers which followed by '-'. 
re.search('[0-9]+(?!-)', info).group()  # numbers which are not followed by '-'  
re.split('[0-9]+(?!-)', info)           # split at the numbers which are not followed by '-'
# ^ - in the beginning of string
re.search('^[0-9]+', info).group()      # numbers in the beginning of string
re.search('^[A-Za-z]+', info).group()      # numbers in the beginning of string

# ^ - also negates when inside []
re.search('[^0-9]+', info).group()      # not number

# $ -in the end of string
re.search('[^0-9]+$', info).group()      # not number in the end of string

info = '2004-959-559# This is Phone Number, my email is py4econ@gmail.com'
# | - or (one of many)
re.findall('i[s|l]', info)                # "i" followed by s or l
re.findall('m[b|y|a]', info)                # "m" followed by b, y or a
re.findall('m[^b|y]', info)                # "m" not followed by b or y

# () - group
x=re.search('([0-9]+)-([0-9-]+)', info)      # two number groups connected by "-"
print(x.group(1))
print(x.group(2))

x=re.search('([0-9a-zA-Z]+)@([0-9a-zA-Z.]+)', info2)      # not number in the end of string
print(x.group(1))
print(x.group(2))

# . - 
info2 = '2004-959-559# This is Phone Number, my email is py4econ@gmail.com'
x=re.search(r'([0-9a-zA-Z]+)@([0-9a-zA-Z.]+)', info2)      # not number in the end of string
print(x.group(1))
print(x.group(2))
