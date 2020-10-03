def write_details():
    filename = input('Enter file name with extension:\n')
    try:
        fileobject = open(filename, 'a')
        m = input("Enter your message\n")
        print(m, file=fileobject)
        print('data insert to file\n')
    except Exception as er:
        print(f'waring :{er}')


def read_details():
    filename = input('Enter file name with extension:\n')
    try:
        fileobject = open(filename, 'r')
        for line in fileobject.readline():
            print(line)
    except Exception as er:
        print(f'waring :{er}')


if __name__ == '__main__':
    # write_details()
    read_details()
