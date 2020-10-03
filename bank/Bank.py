import sys


class Bank():
    def __init__(self, amount, uname, upass):
        self.amount = amount
        self.uname = uname
        self.upass = upass

    def login(self, uname, upass):
        if((self.uname == 'Bank') and (self.upass == 'Bank@123')):
            print("successfuly login ")
            return 1
        else:
            print("unsuccessful login")
            return 2

    def transaction(self, ch):
        bankoption = {1: 'Deposit',
                      2: 'Withdrawal',
                      3: 'Balance Enquiry',
                      4: 'Exit'}

        return bankoption.get(ch, 'Invalid option')

    def Deposit(self, credited_amount):
        self.amount = self.amount + credited_amount
        print(f'Your current Account Balance : $ {self.amount}')

    def Withdrawal(self, credited_amount):
        self.amount = self.amount - credited_amount
        print(f'Your current Account Balance : $ {self.amount}')

    def Balance_Enquiry(self):
        print(f'Your current Account Balance : $ {self.amount}')


if __name__ == "__main__":
    username = input('Enter username \n')
    password = input('Enter your password \n')
    log = Bank(10000, username, password)
    if(log.login(username, password) == 2):
        sys.exit()
    else:
        print(f'Enter 1 for Deposit \nEnter 2 for Withdrawal \nEnter 3 for Balance Enquiry \nEnter 4 for Exit \n')
        retart = 'yes'
        while retart[0] == 'y' or retart[0] == 'Y':
            ch = eval(input('select option '))
            trans = log.transaction(ch)
            if (trans == 'Deposit'):
                x = eval(input('How much do you want to deposit? \t'))
                log.Deposit(x)
                retart = input('Do you want to continue, yes or no? \t')
            elif(trans == 'Withdrawal'):
                y = eval(input('How much do you want to withdraw \t'))
                log.Withdrawal(y)
                retart = input('Do you want to continue, yes or no?\t')
            elif(trans == 'Balance Enquiry'):
                log.Balance_Enquiry()
                retart = input('Do you want to continue, yes or no? \t')
            elif(trans == 'Exit'):
                sys.exit()
            else:
                print(trans)
                retart = input('Do you want to continue, yes or no? \t ')
