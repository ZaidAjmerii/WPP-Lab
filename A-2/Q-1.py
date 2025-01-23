'''
Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.

getAstring

forloop

add next as add

then next as lower
'''

userString = input("Enter your string: ")
programString = ""
x = 1

for char in userString:
  if x%2==1:
    programString += char.lower()
    x+=1
  else:
    programString += char.upper()
    x+=1


print(f"previous string: {userString} \n New string: {programString}")