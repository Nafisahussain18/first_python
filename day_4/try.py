def f(n, *args):
    print(n)
    for arg in args:
        print(arg)


def sayhello(*names):
    for name in names:
        print(f"Hello, {name}")


if __name__ == "__main__":
    a = '''zxcvbnm'''
    # print(a)
    # f(1, (2, 3), {4, 5, 6}, '&1')
    # sayhello('Ayushi', 'Leo', 'Megha')
    # f = open("firstfile.txt", "w+")
    f = open("firstfile.txt", "r")
    # for i in range(10):
    #     f.write("this is line " + str(i) + "\r\n")
    if f.mode == 'r':
        contents = f.read()
        print(contents)

    f.close()
