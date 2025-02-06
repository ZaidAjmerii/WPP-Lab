# Check if a sentence is a pangram

def is_pangram(s):
  s = s.lower()  # Convert to lowercase
  alphabet = set("abcdefghijklmnopqrstuvwxyz")  # All letters in the alphabet

  
  if set(s) >= alphabet:
    print("pangram")
  else:
    print("not pangram")



s = input("Enter a sentence: ")
is_pangram(s)
