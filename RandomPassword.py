import random 
import string 

password = input("Enter your password: ")

i = 0
while i <= 10:
  password += (random.choice(string.digits))
  i += 1

print(password)

i = 0
while i < len(password):
  if password[i] == "s":
    print("This charecter is an s")
  else:
    print("This charecter is not an s")
  i += 1
