import sqlite3 as sql


def createTableIfNotExist():
    sqlConnection = sql.connect(r"SQLiteDb\userData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS users (
                            id integer primary key autoincrement,
                            username text not null,
                            password text not null
                        );
                    """)


# cursor = sqlConnection.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
# print(cursor.fetchall())


# CompanyID = input("Please enter company id")
# CompanyName = input("Please enter company name")
# CEO = input("Please enter company CEO")
# Address = input("Please enter company address")
# Country = input("Please enter company country")


def insertUser(username, password):
    con = sql.connect("SQLiteDb\\userData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username, password))
    con.commit()
    con.close()


def retrieveUsers():
    con = sql.connect("SQLiteDb\\userData.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users
