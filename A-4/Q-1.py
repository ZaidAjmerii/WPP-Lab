#  The Love-Letter Mystery

def LoveLetterMystery(arrayStrings):
  count = 0

  for x in range(T):

    charList = [char for char in arrayStrings[x]]
    length = len(charList)

    for l in range(length//2):
      if(ord(charList[l]) >= ord(charList[length-l-1])):
        count = count + (ord(charList[l]) - ord(charList[length-l-1]))
      else:
        count = count + (ord(charList[length - l - 1]) - ord(charList[l]))

    print(count)
    count = 0


# main function

T = int(input("Enter the value of T(0 <=T <=10): "))

arrayStrings = []

for i in range(T):
  arrayStrings.append(input())

LoveLetterMystery(arrayStrings)


