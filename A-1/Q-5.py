# You are a student in a class of 10. Your class teacher assigns you a task of entering the
# names of all the students in the class. You finally want to display the names given the
# condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
# names and display them. [Hint: Slicing works when you are selecting maximum characters]

numOfStudents = int(input("Enter the number of students "))

Names = []

for x in range(numOfStudents):
  Names.append(input(f"Enter the name of student {x + 1} "))
  while len(Names[x]) > 15:
    print("Error, condition that the maximum allowed characters in a name is 15")
    Names[x] = ""
    print("Re-enter the name")
    Names[x] = input(f"Enter the name of student {x + 1} ")

for x in range(numOfStudents):
  print(f"The reverse name of student {x+1} is {Names[x][::-1]}")
    
