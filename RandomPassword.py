import random 
import string 

password = []

i = 0
while i <= 10:
  password.append(random.choice(string.digits))
  i += 1

print(password)



