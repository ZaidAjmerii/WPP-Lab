# Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
# of the points in your 3-D space and store them in a list. The final output is a list with each
# consisting of a point and its nearest neighbour. [Hint: Use distance between two points
# formula]

VectorsList = []
points = []

for x in range(10):
  print(f"{x  + 1 } vector")
  for y in range(10):
    points.append(int(input(f"Enter coordinates of place {y+1}")))
  VectorsList.append(points)
  points = []
print(VectorsList)

max = 0
tempCal = 0
index = -1

'''

2 Loop

first will pick one vector 
and then take pick another and check their distance between them
and save it in max
Also save that positions index

'''

finalList = []

for x in range(10):
  print(f"{x  + 1 } vector")
  print(f"{VectorsList[x]}")
  for y in range(10):
    if(y != x):
     for z in range(3):
       tempCal += VectorsList[x][z]*VectorsList[y][z]
  
    if(tempCal > max):
      max = tempCal
      index = y
      tempCal = 0
  
  finalList.append([VectorsList[x], VectorsList[index]])

print(finalList)

  

