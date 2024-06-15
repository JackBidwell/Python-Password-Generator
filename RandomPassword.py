import random 
import string 

password = input("Enter your password: ")

i = 0
while i <= 10:
  password += (random.choice(string.digits))
  i += 1

print(password)



