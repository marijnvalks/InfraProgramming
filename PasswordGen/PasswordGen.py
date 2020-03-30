import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
specialcharacters = ['!', '#', '$', '%', '&', '*', '<', '=', '>', '?', '@', '[', ']', '^', '_', '~']


def runprogram():
    while True:  # Wacht op input user moet int zijn anders breakt die uit de loop en geeft error.
        try:
            passwordlength = int(input('\nHow long should the password be: '))
            break
        except ValueError:
            print('Please Enter a Number')

    while True:  # Aan de hand van user keuze generate die een password met de lengte die eerder is aangegeven.
        try:
            print('1 - Text Only \n2 - Numbers Only '
                  '\n3 - Text and numbers \n4 - Text and numbers with special characters')
            userchoice = int(input('\n\nPlease make a choice: '))
            if userchoice == 1:
                pw = ''.join(random.choice(alphabet) for _ in range(passwordlength))
                """
                
 .join zorgt voor toevoeging van data aan de string, gebruik maken van random.choice om een random 
 combinatie te kiezen van het gene tussen (). In dit geval pakt die dus random karakters uit mijn arrays.
 Dit doet zovaak als de waarde van integer passwordlenght. Dit principe geld ook van andere userchoices.
                
                """
                break
            elif userchoice == 2:
                pw = ''.join(random.choice(numbers) for _ in range(passwordlength))
                break
            elif userchoice == 3:
                pw = ''.join(random.choice(alphabet + numbers) for _ in range(passwordlength))
                break
            elif userchoice == 4:
                pw = ''.join(random.choice(alphabet + numbers + specialcharacters) for _ in range(passwordlength))
                break
            else:
                print('\nWrong Selection. Please select a number from the list \n')
        except ValueError:
            print('\nPlease Enter a Number\n')
    print('Here is a password for you: ', pw)
    print("\nPress a key to generate another password or type 'stop' to exit. ")
    print("Waiting for enter...")
    if input() != 'stop':
        runprogram()


print("**Password generator by Marijn Valks**")
runprogram()
