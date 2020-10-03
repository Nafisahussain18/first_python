import sys


def mychoices(ch):
    mydict = {1: 'Addition',
              2: 'Subtraction',
              3: 'Exit'}

    return mydict.get(ch, 'Invalid Option')


if __name__ == "__main__":
    retart = 'yes'
    while retart[0] == 'y' or retart[0] == 'Y':
        print('1. Addition \n 2. Subtraction \n 3. Exit \n Select the option')
        c = eval(input("select the option "))
        options = mychoices(c)
        if options == 'Addition':
            a, b = eval(input('Enter the value of a,b \n'))
            print(f'{a} + {b} = {a+b}')
            retart = input('Do you want to continue, yes or no?')
        elif options == 'Subtraction':
            a, b = eval(input('Enter the value of a,b \n'))
            print(f'{a} - {b} = {a+b}')
            retart = input('Do you want to continue, yes or no?')
        elif options == 'Exit':
            sys.exit()
        else:
            print(options)
            retart = input('Do you want to continue, yes or no?')
