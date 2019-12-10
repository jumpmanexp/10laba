import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def select_notatku(conn):
    sql = 'SELECT * FROM notatku'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def create_notatku(conn, task):
    sql = ''' INSERT INTO notatku(nazva_notatku, data)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)


def update_notatku(conn, data):
    sql = ''' UPDATE notatku
              SET data = ?
              WHERE nazva_notatku = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def remove_notatku(conn, removed_task):
    sql = ''' DELETE FROM notatku WHERE nazva_notatku = ?'''
    cur = conn.cursor()
    cur.execute(sql, removed_task)
    conn.commit()


def main():

    database = r"zaharchyk.db" 
 
    conn = create_connection(database)

    with conn:
        print("\nВсі нотатки (текст, дата)")
        select_notatku(conn)
        print("\nВставка нового рядка...")
        create_notatku(conn, ('Зробити ДЗ', '20-12-2020'))
        print("\nВсі нотатки (текст, дата)")
        select_notatku(conn)
        print("\nЗміна рядка...")
        update_notatku(conn, ('Зробити ДЗ', '21-12-2020'))
        print("\nВсі нотатки (текст, дата)")
        select_notatku(conn)
        print("\nВидалення рядка")
        remove_notatku(conn, ('Зробити ДЗ',))
        print("\nВсі нотатки (текст, дата)")
        select_notatku(conn)
        
 
if __name__ == '__main__':
    main()
