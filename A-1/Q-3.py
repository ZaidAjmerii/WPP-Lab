# Write a program that asks the user to enter a length in feet. The program should then give
# the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
# meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
# enter a 2, then the program converts to yards, etc. While this can be done with if statements,
# it is much shorter with lists and it is also easier to add new conversions if you use lists.


userLength = int(input("Enter the length in feet "))
print("Enter 1 for inches, 2 for yards, 3 for miles, 4 for millimeters, 5 for centimeter, 6 for meter, 7 for kilometer")
userChoice = int(input())
conversionList = [userLength*12, userLength/3, userLength/5280, userLength*304.8, userLength*30.48, userLength/3.281, userLength/3281]
print(f"So, The converted value is {conversionList[userChoice - 1]}")