import sqlite3


class MyConnection:

    def myconnect(self):
        self.conn = sqlite3.connect('mydb.db')
        return self.conn

    # def closeMyConnection(self):
    #     self.conn.close()


def WriteDetails(fname, lname, emailid):
    try:
        conn = MyConnection().myconnect()
        cursor = conn.cursor()

        insert_query = "INSERT INTO users(firstname,lastname,emailid) VALUES(?,?,?)"
        # tuple
        param = (fname, lname, emailid)

        cursor.execute(insert_query, param)

        print('Data Inserted successfully')
        conn.commit()
        # conn.close()
    except sqlite3.Error as er:
        print(f'Warning : {er}')
        # conn.close()
    finally:
        if(conn):
            conn.close()


def read_Details():
    try:
        conn = MyConnection().myconnect()
        cursor = conn.cursor()
        select_qurey = 'SELECT * FROM users'
        cursor.execute(select_qurey)

        # Catch result
        rows = cursor.fetchall()
        print('Id\t\t\tfirstname\t\tlastname\t\tEmailId')
        for row in rows:
            print(f"{row[0]}\t\t\t{row[1]}\t\t\t{row[2]}\t\t\t{row[3]}")

    except sqlite3.Error as er:
        print(f'Warning : {er}')

    finally:
        if(conn):
            conn.close()


if __name__ == "__main__":
    # fname = input("Enter the Firstname:\n")
    # lname = input("Enter the lastname:\n")
    # emailid = input("Enter the emailid:\n")
    #WriteDetails(fname, lname, emailid)
    read_Details()
