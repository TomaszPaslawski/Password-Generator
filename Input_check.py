def check_the_input(user_input):
    while True:
        try:
            value = int(input(user_input))
        except ValueError:
            print('You typed a non-numerical value. Please try again!')
            continue
        else:
            break
    return value
