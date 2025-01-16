# Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of
# numbers. Check the validity of your equivalence classes. [Hint: the union of all equivalence
# classes should be the original set/list.]

# The equivalence classes for modulo 5 are,,,, and. These classes are made up of integers that have the same remainder when divided by 5.

# 0, 1, 2 , 3 , 4 , 5

setAll = {x for x in range(1,10001)}

set0 = set()         
set1 = set()         
set2 = set()         
set3 = set()         
set4 = set()         

for x in range(1,10001):
  if(x%5 == 0):
    set0.add(x)
  elif(x%5 == 1):
    set1.add(x)
  elif(x%5 == 2):
    set2.add(x)
  elif(x%5 == 3):
    set3.add(x)
  elif(x%5 == 4):
    set4.add(x)

result = set0 | set1 | set2 | set3 | set4

if(result == setAll):
  print("All the classes are valid")