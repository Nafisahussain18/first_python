
import datetime
from datetime import date
import sys


class reservation:
    # def (self, name, passport_no, destination):

    # def __init__(self, name, age, sex, destination, transport, way):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    #     self.destination = destination
    #     self.transport = transport
    #     self.way = way
    #     self.price = 100

    def transport_func(self, transport):

        mytransport = {1: 'Bus',
                       2: 'train',
                       3: 'airplane'}

        return mytransport.get(transport, 'Invalid option')

    def ways(self, way):
        way_1_2 = {1: 'one way',
                   2: 'two ways'}

        return way_1_2.get(way, 'invalid option')

    def destination_list(self, destination):
        destination_dict = {1: 'doha',
                            2: 'dubui',
                            3: 'khartoum',
                            4: 'kuwait',
                            5: 'muscat',
                            6: 'Abu Dhabi'
                            }
        return destination_dict.get(destination, 'Invalid option')


class price(reservation):

    def __init__(self, name, age, sex, destination, transport, way):
        self.name = name
        self.age = age
        self.sex = sex
        self.destination = destination
        self.transport = transport
        self.way = way
        self.price = 100

    def ticketprice(self):
        if (self.age > 0 and self.age < 11):
            if (self.way == 'Bus'):
                return 100
            elif(self.way == 'train'):
                return 200
            else:
                return 1000
        elif (self.age > 10 and self.age < 19):
            if (self.way == 'Bus'):
                return 200
            elif(self.way == 'train'):
                return 400
            else:
                return 2000
        else:
            if (self.way == 'Bus'):
                return 300
            elif(self.way == 'train'):
                return 500
            else:
                return 3000

    # def destination():


if __name__ == '__main__':
    name = input('Enter your name\n')
    sex = input('Enter your sex\n')
    destination = int(input(
        'Enter your destionation\n1: doha\n2: dubui\n3: khartoum\n4: kuwait\n5: muscat\n6: Abu Dhabi\n'))
    age = int(input('Enter your age\n'))
    transport = int(input('select \n1 for bus\n2 for train\n3 for airplane\n'))
    way = int(input('select\n1 for one way\n2 for two way\n'))
    ob = price(name, age, sex, destination, transport, way)
    x = ob.ways(way)
    ob.transport_func(transport)
    ob.destination_list(destination)
    if x == 'one way':
        year, mon, day = eval(input('Enter the date(yyyy,mm,dd) : \n'))
        date1 = datetime.date(year, mon, day)
        if(date1 < date.today()):
            print(f'the date is gone')
            sys.exit()
    elif x == 'two ways':
        year1, mon1, day1 = eval(input('From(yyyy,mm,dd) : \n'))
        date1 = datetime.date(year1, mon1, day1)
        year2, mon2, day2 = eval(input('To(yyyy,mm,dd) : \n'))
        date2 = datetime.date(year2, mon2, day2)
        if(date1 < date.today()):
            print(f'the date is gone')
            sys.exit()
        if(date1 > date2):
            print('not possible')
            sys.exit()
        else:
            print(f'how long {date2-date1}')

    print(ob.ticketprice())
