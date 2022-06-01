import sqlite3
import pandas as pd

def create_table(conn):
    conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);''')
    print("Table created successfully")


def insert_table(conn):
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

    data = [
        [5, 'Sarah', 28, 'Oregon', 55000.00],
        [6, 'Bill', 31, 'Seattle', 95000.00]
    ]
    conn.executemany("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (?, ?, ?, ?, ?)", data)


def select_table(conn):
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")


def main():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    df_company = pd.read_sql_query('select * from company', conn)
    print(df_company)

    df_company.to_sql("company_pd", conn, index=False, if_exists='replace')

    # create_table(conn)
    # insert_table(conn)
    # select_table(conn)
    #
    # conn.execute("DELETE from COMPANY where ID = 2;")
    # conn.commit()
    #
    # select_table(conn)



    conn.close()


if __name__ == "__main__":
    main()
