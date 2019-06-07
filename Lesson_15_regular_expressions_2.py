# Source
#https://www.w3schools.com/python/python_regex.asp
#https://www.tutorialspoint.com/python/python_reg_expressions.htm
#https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial
#https://www.rexegg.com/regex-lookarounds.html
#others


# Content
# Special Sequences
# \ \s \S \A \b \B \w \W \d \D
# Option Flags
#re.I re.M

import re

# Special Sequences

info = '2004-959-559# This is Phone Number, my email is py4econ@gmail.com'
info2 = '2004-959-559# This is'

re.findall('s',  info2)                 # the letter "s" 
re.findall('\s', info2)                 # not the letter "s" but a space, equivalent to [ \t\n\r\f\v]
re.findall('\S', info2)                 # "m" not followed by b or y

re.findall('\A[a-z]', info2)                # Match only at beginning of string
re.findall('is', info2)                # is
re.findall(r'\bis\b', info2)           # Match a word boundary
re.findall(r'\Bis', info2)             # Match except at a word boundary
re.findall(r'[\w]*\Bis', info2)        # Match except at a word boundary

re.findall(r'\w', info2)             # Characters in [a-zA-Z0-9_]
re.findall(r'\W', info2)             # Characters NOT in [a-zA-Z0-9_]

re.findall(r'\d*', info2)             # Digits [0-9]
re.findall(r'\D', info2)              # NOT digits ^[0-9]

re.findall(r'\d*', info2)             # Digits [0-9]
re.findall(r'\D', info2)              # NOT digits ^[0-9]

# Option Flags
# re.I, re.M, re.S,re.X

# re.I = re.IGNORECASE 
re.findall(r'p', info, flags=re.I)

# re.M = re.MULTILINE
ss = '''abc
def
ghi'''

re.findall(r'^\w', ss)
re.findall(r'^\w', ss, flags = re.MULTILINE)

# re.S = re.DOTALL
ss = """once upon a time,
there lived a king"""

re.findall(r'.+', ss)
re.findall(r'.+', ss, re.S)

#re.X = re.VERBOSE

pattern = """[a-z]+ 

#this is the pattern we want to catch"""
pattern1 = '[a-z]+'

re.findall(pattern1, info, re.VERBOSE)




