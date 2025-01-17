import sqlite3

def main():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def test_select():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Create table
    c.execute('''select * from stocks''')

    print(c.fetchall())



if __name__ == "__main__":
    #main()
    test_select()