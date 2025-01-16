# Write a program that generates 100 random integers that are either 0 or 1. Then find the
# longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
# zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random

genList = [random.randint(0,1) for x in range(1,101)]

max = 0
count = 0

for x in range(100):
  if(genList[x] == 0):
    if x == 99:
     count += 1
     max = count
    else:
     count += 1
  else:
    if(max < count):
      max = count
      count = 0
    else:
      count = 0


print(genList)
print(max)
      
