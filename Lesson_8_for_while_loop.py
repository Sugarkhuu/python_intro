# Source:
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.w3schools.com/python/python_while_loops.asp

# Simple
for x in range(6):
  print(x)

for x in range(3, 6):
  print(x)

## Through list
fruits = ["apple", "banana", "cherry"]

for x in range(len(fruits)):
  print(fruits[x])  

# faster way
for x in fruits:
  print(x)

# break
for x in fruits:
  print(x) 
  if x == "banana":
    print('Found a banana!')
    break

# continue
for x in fruits:
  if x == "banana":
    print('Found a banana!')
    continue
  print(x)

## Nested or double loop
adj = ["red", "big", "tasty"]

for x in adj:
  for y in fruits:
    print(x, y)

# nested with break
for x in adj:
  for y in fruits:
    if y == "banana":
        break
    print(x, y)

# nested with continue
for x in adj:
  for y in fruits:
    if y == "banana":
        continue
    print(x, y)

# While
i = 1
while i < 6:
  print(i)
#  if i == 3:
#    break
  i += 1

# continue and incrementing +=
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)

# just while with len
i = 0  
while i < len(fruits):
  print(fruits[i])
  i += 1

# nested while
i, j = 0, 0  
while i < len(adj):
  j = 0
  while j < len(fruits):
    print(adj[i], fruits[j])
    j += 1
  i += 1

# nested while with continue  
i, j = 0, 0  
while i < len(adj):
  j = 0
  while j < len(fruits):
    if j == 1:
        j += 1
        continue
    print(adj[i], fruits[j])
    j += 1
  i += 1

# just for fun
whoWeAre = 'Py4Econers'  
for i in range(len(whoWeAre)):
  print(whoWeAre[0:i+1])