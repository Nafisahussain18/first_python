def login_func(u, p):
    try:
        objectfile = open('login.txt', 'r')
        Lines = objectfile.readlines()
        for line in Lines:
        print(line.strip())

        # if Lines[0] == u:
        #     if Lines[1] == p:
        #         print(f'login successful')
        #     else:
        #         print(f'password is wrong')
        # else:
        #     print(f'username is wrong')
    except Exception as er:
        print(f'waring :{er}')


if __name__ == '__main__':
    user = input('enter your user name \n')
    password = input('Enter password\n')
    login_func(user, password)
