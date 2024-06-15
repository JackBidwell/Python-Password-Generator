import random 
import string 

password = input("Enter your password: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetposition = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

# Determing a letters position in the alphabet

i = 0
while i < len(password):
  j = 0
  while j < len(alphabet):
    if password[i] == alphabet[j]:
      print(alphabetposition[j])
    j += 1
  i += 1


# print(password)

# i = 0
# while i < len(password):
#   if password[i] < (alphabetposition)/2:
#     password[i] = random.choice(string.digits)
#   elif password[i] > (alphabetposition)/2:
#     password[i] = alphabetposition - i
#   i += 1 

# print(password)
