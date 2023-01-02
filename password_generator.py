import random

rawsymbol    = "@#$%"
raw          = "A, B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, X, Z, W, Y, E, I, O, U"
rawambiguous = "{ } [ ] ( ) / \ ' \" ` ~ , ; : . < >"


def passwordGenerator(len, symbol_yes=False, ambigious_yes=False):
    """ Create a password of the user's desired length and complexity, 
        randomly generated from a raw string of characters.

        len: int
        symbol_yes: bool
        ambigious_yes: bool
    """
    password, sym, ambi, num, cap = [], [], [], [], []

    # list of 10 numbers
    numbers      = list(range(10))
    
    # split the raw string into a list of capitalized and lower case letters
    capitalized  = raw.split(sep=', ')
    lower        = list(map(lambda x: x.lower(), capitalized))
    
    # slice the raw symbol string into a list of symbols
    symbols      = list(rawsymbol)
    
    # split the raw ambiguous string into a list of ambiguous characters
    ambiguous    = rawambiguous.split(sep=' ')
    
    # We gonna give them a number and a capital letter
    password_len = len - 2
    all_options  = capitalized + lower + numbers

    # If they do ask symbol
    if symbol_yes:
        sym.append(random.choice(symbols))
        password_len -= 1

    # If they do ask ambiguous
    if ambigious_yes:
        ambi.append(random.choice(ambiguous))
        password_len -= 1

    # Give them a number
    # Give them a capital letter
    num.append(random.choice(numbers))
    cap.append(random.choice(capitalized))
    
    print("\nYour password num:  ", num)
    print("\nYour password cap:  ", cap)
    print("\nYour password sym:  ", sym)
    print("\nYour password ambi: ", ambi)
    
    # Now choose the rest of the password from all the options
    processed = random.sample(all_options, k=password_len)

    # Combine all the lists
    password  = processed + num + cap + sym + ambi
    
    print("\nYour password currently look like this: ", password, "\n")
    return ''.join([str(item) for item in random.sample(password, k=password_len)])

def main():
    while True:
        # If they do ask
        symbol_flag    = False
        ambiguous_flag = False
        
        """ Ask the user for the desired password length and complexity """
        len       = int(input('Your password length: '))
        symbol    = input(f'Include symbols like (@ # $ %)? (y/n) ')
        ambiguous = input("Include ambiguous characters like { } [ ] ( ) / \ ' \" ` ~ , ; : . < >? (y/n) ")
        
        if symbol == 'y':
            symbol_flag = True

        if ambiguous == 'y':
            ambiguous_flag = True

        """ Generate the password """
        result = passwordGenerator(len, symbol_flag, ambiguous_flag)
        print("--------Your password: " + result +"--------")

        """ Copy the password to the clipboard """
        print('Your password is ready to be pasted. Thank you for using our service.')
        
        """ End game condition """
        cont = input('Continue using? (y/n) ')
        
        if cont != 'y':
            print("Thank you for using our service.")
            print('----------------------------------------')
            break

if __name__ == '__main__':
    main()