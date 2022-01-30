import sqlite3
from random import randint

database_1 = sqlite3.connect("server.sqlite3")
sql = database_1.cursor()

sql.execute(
    """CREATE TABLE IF NOT EXISTS notebook (
    note TEXT,
    answer TEXT
    )
    """
)
database_1.commit()


def add_notes():
    global notebook_note, notebook_answer
    notebook_note = input('your note: ')

    sql.execute(f"SELECT note FROM notebook WHERE note = '{notebook_note}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO notebook VALUES (?, ?)", (notebook_note, 'no'))
        database_1.commit()
        print('User registered')
        for value in sql.execute("SELECT * FROM notebook"):
            print(value)
    else:
        print('this note already exists')
        for value in sql.execute("SELECT * FROM notebook"):
            print(value)


if __name__ == "__main__":
    add_notes()


def delete_note():
    for value in sql.execute("SELECT * FROM notebook"):
        print(value)
    choose = input('choose note: ')
    sql.execute(f"SELECT note FROM notebook WHERE note = '{choose}'")
    if sql.fetchone():
        ad = input('done? yes or  not : ')
        if ad == "yes":
            sql.execute(f"DELETE FROM notebook WHERE note = '{choose}'")
            database_1.commit()
            print('deleted')
        elif ad == 'not':
            print('note left')


delete_note()



