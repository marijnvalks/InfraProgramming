lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_characters = [' ', '!', '#', '$', '%', '&', '"', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                      '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', "'"]


def checkpass(password, firstname, lastname):

    length = int()
    length2 = int()
    lower = int()
    upper = int()
    special = int()
    number = int()
    f_name = int(1)
    s_name = int(1)
    """
Hieronder gaat die de waarde van 'password' vergelijken in een if contructie als die matchen past die de waarde van
'password_strength' aan. Aan de hand van die waarde geeft die aan of het een goed of slecht wachtwoord is. Ook wordt
de bijbehoorende int naar waarde 1 gezet als het overeenkomt. Dit gebruik ik voor het doorgeven van de reden 
waarom het goed of slecht is aan de user.
    """
    password_strength = 0
    if len(password) >= 8:
        length = 1
        length2 = 1
        password_strength += 1
    elif len(password) >= 4 and length != 1:
        length2 = 1
        password_strength -= 1
    else:
        password_strength -= 2
    for i in lower_alphabet:
        if i in password:
            while lower != 1:
                lower = 1
                password_strength += 1
    for i in upper_alphabet:
        if i in password:
            while upper != 1:
                upper = 1
                password_strength += 1
    for i in special_characters:
        if i in password:
            while special != 1:
                special = 1
                password_strength += 1
    for i in numbers:
        if i in password:
            while number != 1:
                number = 1
                password_strength += 1
    if firstname.lower() in password.lower():
        f_name = 0
        password_strength -= 2
    if lastname.lower() in password.lower():
        s_name = 0
        password_strength -= 2
    password_rank = str()

    if password_strength >= 5:
        password_rank = 'very strong!'
    elif password_strength == 4:
        password_rank = 'strong!'
    elif password_strength == 3:
        password_rank = 'ok!'
    elif password_strength == 2:
        password_rank = 'bad!'
    elif password_strength <= 1:
        password_rank = 'very bad!'
    print('\nYour password is ', password_rank)
    reasons = [length, length2, lower, upper, special, number, f_name, s_name]
    return reasons  # array met daarin de opgehoogde waardes per reden als het overeenkwam met statement.


def runprogram():

    password = input('\nPlease enter your password here: ')
    firstname = input('Please enter your first name: ')
    lastname = input('Please enter your last name: ')
    reasons = checkpass(password, firstname, lastname)
    if reasons[0] != 1:
        print("Because it's way too short.")
    if reasons[1] != 1:
        print("Because it's too short.")
    if reasons[2] != 1:
        print("Because it doesn't have a lower case character in it.")
    if reasons[3] != 1:
        print("Because it doesn't have an upper case character in it.")
    if reasons[4] != 1:
        print("Because it doesn't have a special character in it.")
    if reasons[5] != 1:
        print("Because it doesn't have a enough numbers in it.")
    if reasons[6] != 1:
        print("Because it's got your first name in it.")
    if reasons[7] != 1:
        print("Because it's got your last name in it.")
    if input("\nPress a key to try again or type 'stop' to exit. ") != 'stop':
        runprogram()


print("**Password strength tester (by Marijn Valks)**")
runprogram()
