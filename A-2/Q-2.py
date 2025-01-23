# Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a
# product name and print the corresponding price or a message if the product is not in the
# dictionary

thisdict = {
  
}


x = 1
y = 1
productNo = 0

while x != 0:
  productNo += 1
  productName = input(f"Enter the {productNo} product Name: ")
  productPrice = input(f"Enter the {productName} product price: ")
  thisdict.update({productName: productPrice})
  x = int(input(f"Enter 0 to quit and 1 to continue: "))

while y != 0:
  productName = input(f"Enter the product Name to find its price: ")
  print(f"{productName}\'s price is {thisdict[productName]} ")
  y = int(input(f"Enter 0 to quit and 1 to continue: "))
