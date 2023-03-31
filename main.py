# Password Generator Project
"""
The main feature of this application is to generate the random password. The number of the respective password
components is basing on the number provided by the user. All the components are randomly organised.
"""

from functions import check_the_input as checker, password_generator as pasgen, another_pass as ap
create_pass = True

while create_pass:
  print("Welcome to the PyPassword Generator!")

  nr_letters = checker("How many letters would you like to have in your password?\n")
  nr_symbols = checker(f"How many symbols would you like to have in your password?\n")
  nr_numbers = checker(f"How many numbers would you like to have in your password?\n")

  pasgen(letters=nr_letters, symbols=nr_symbols, numbers=nr_numbers)
  to_continue = ap()
  if to_continue == False:
    print ('Thank You for using this application. Hope to see You again!')
    create_pass = False
