# Introduction to Python, Lesson #3. Lists, tuples, matrix and a glimpse into dataframe

# Strings, lists and tuples all are types of sequences.
# Ctrl + Shift + E (I) switch between editor and iphython console

# References
# For sequences: https://www.tutorialspoint.com/python/
# Matrix operations: https://www.python-course.eu/matrix_arithmetic.php
# Dataframe: http://pbpython.com/pandas-list-dict.html


# Lists

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

# Slice and concatenate 

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print(list1 + list2)

# Update 

list1[2] = 2001

# Append 

list1.append(2019)

# Delete 

del list1[2]

# Count

list1.count('physics')

# Index (lowest)

list1.index(2019)

# Insert

list1.insert(0,15)

# Pop

list1.pop(2)

# Reverse

list1.reverse()

# Sort

list1.sort()

lista = [20, 18, 14]
lista.sort()

# Len

len([1, 2, 3])

# Repetition

['Hi!'] * 4

# Membership

3 in [1, 2, 3]

# Tuples

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

# Empty tuple

tup1 = ()

tup1 = (50,)

# Following action is not valid for tuples

tup1[0] = 100

# Len

len((1, 2, 3))

# Concatenate

(1, 2, 3) + (4, 5, 6)

# Repetition

('Hi!',) * 4

# Membership

3 in (1, 2, 3)

# Any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples, as indicated in these short examples

 # Matrix 
 
# from numpy import * 
 
import numpy as np
 
 a = np.array([['Mon',18,20,22,17],['Tue',11,18,21,18],
 		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
 		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
 		   ['Sun',13,15,19,16]])
     
 m = np.reshape(a,(7,5))
 
 # Print data for Wednesday

print(m[2])
 
# Print data for friday evening

print(m[4][3])
      
# Insert a new row
 
m_r = np.append(m,[['Avg',12,15,13,11]],0)
 
# Insert a new column
    
m_c = np.insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
 
 
# Delete a row     

 m = np.delete(m,[2],0)

# Delete a column

 m = np.delete(m,[4],1)    
 
# Update a row
     
m[2] = ['Thu',0,0,0]

# Matrix operations

 x = np.array([1,5,2])
 y = np.array([7,4,1])
 x + y
 x * y
 x - y
 x / y
 x % y
 
 np.dot(x,y)
 
 x = np.array( ((2,3), (3, 5)) )
 y = np.array( ((1,2), (5, -1)) )
 x * y

 x = np.matrix( ((2,3), (3, 5)) )
 y = np.matrix( ((1,2), (5, -1)) )
 x * y
       
 # Inverse
     
 from numpy.linalg import inv
 a = np.array([[1., 2.], [3., 4.]])
 ainv = inv(a)
 
 # Determinant 
 
 a = np.array([ [[1, 2], [3, 4]], [[1, 2], [2, 1]], [[1, 3], [3, 1]] ])
 a.shape
 np.linalg.det(a)
 
 #Glimpse into Dataframe
 
 d = {'col1': [1, 2], 'col2': [3, 4]}
 
 import pandas as pd
 
 df = pd.DataFrame(data=d)
 
 df.dtypes
 
  df2 = pd.DataFrame(np.random.randint(low=0, high=10, size=(20, 5)),
                     columns=['a', 'b', 'c', 'd', 'e'])
  
  



