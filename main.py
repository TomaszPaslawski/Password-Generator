# Password Generator Project
"""
The main feature of this application is to generate the random password. The number of the respective password
components is basing on the number provided by the user. All the components are randomly organised.
"""

import random
from letters import letters as let
from numbers import numbers as num
from symbols import symbols as sym

print("Welcome to the PyPassword Generator!")

while True:
  try:
    nr_letters = int(input("How many letters would you like to have in your password?\n"))
  except ValueError:
    print('You typed a non-numerical value. Please try again!')
    continue
  else:
    break

while True:
  try:
    nr_symbols = int(input(f"How many symbols would you like to have in your password?\n"))
  except ValueError:
    print('You typed a non-numerical value. Please try again!')
    continue
  else:
    break

while True:
  try:
    nr_numbers = int(input(f"How many numbers would you like to have in your password?\n"))
  except ValueError:
    print('You typed a non-numerical value. Please try again!')
    continue
  else:
    break

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(let))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(sym)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(num)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")