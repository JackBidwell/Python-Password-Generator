import random 
import string 

password = input("Enter your password: ")
arrayPassword = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetposition = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

# Determing a letters position in the alphabet


# Change password to array to handle assignment

i = 0
while i < len(password):
  arrayPassword.append(password[i])
  i += 1


i = 0
while i < len(password):
  j = 0
  while j < len(alphabet):
    if password[i] == alphabet[j]:
      charecter = alphabetposition[j]
      if charecter < len(alphabet)/2:
        password[i] = "a"
    j += 1
  i += 1

print(password)
