class Sample_Class:
    def __init__(self, a):
        self.a = a

    def view(self):
        print(f'I\'m inside the function')

    def run(self):
        print(f'A : {self.a}')


if __name__ == "__main__":
    ob = Sample_Class(5)
    ob.view()
    ob.run()
