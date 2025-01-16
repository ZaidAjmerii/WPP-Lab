# Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.



# (a)

listA = [x for x in range(50)]
print(listA)

# (b)

listB = [x*x for x in range(1, 51)]
print(listB)

# (b)

listC = [[chr(x) for y in range(x-96)] for x in range(97, 123)]
print(listC)