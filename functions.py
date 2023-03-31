import random
from data import letters as let, symbols as sym, numbers as num

def check_the_input(user_input):
     """
    Function is checking if user prompt a numerical value.
    :param user_input: is taking the value from the keyboard prompt by user.
    :return: value as int
     """
     while True:
        try:
            value = int(input(user_input))
        except ValueError:
            print('You typed a non-numerical value. Please try again!')
            continue
        else:
            break
     return value

def password_generator(letters, symbols, numbers):
    """
    Basing on the user choices generates the random password which length = sum of the respective values inputed
    by the user.
    :param letters: takes the number of the letters from user input
    :param symbols: takes the number of the symbols from user input
    :param numbers: takes the number of the numbers from user input
    :return: randomly generated password
    """
    password_list = []

    for char in range(1, letters + 1):
        password_list.append(random.choice(let))

    for char in range(1, symbols + 1):
        password_list += random.choice(sym)

    for char in range(1, numbers + 1):
        password_list += random.choice(num)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")

def another_pass():
    """
    Checks if the user would like to generate another password.
    :return: user's choice
    """
    user_choice = input('Would You like to generate another password? Type "Yes" or "No".')
    if user_choice.lower() == 'yes':
        return True
    elif user_choice.lower() == 'no':
        return False
    else:
        print('Incorrect answer. Please try again')
        another_pass()