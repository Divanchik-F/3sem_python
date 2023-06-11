import sqlite3

commands_list = """
Available commands:
books_list   - List books
readers_list - List readers
add_book    - Add book
add_reader  - Add reader
give_b2r    - Give book to reader
take_b4r    - Take book from reader
exit    - Exit app
""" 

def get_id(conn, name, author, title):
    return (conn.execute('select id from Readers where name = ?', (name,)).fetchone()[0],
            conn.execute('select id from Books where title = ? AND author = ?',(title, author)).fetchone()[0])

conn = sqlite3.connect("test.db")

while True:
    cmd = input("> ").lower()
    if cmd == "books_list":
        with conn:
            for row in conn.execute('select * from Books'):
                print(row)
    elif cmd == "readers_list":
        with conn:
            for row in conn.execute('select * from Readers'):
                print(row)
    elif cmd == "add_book":
        author = input("> Author: ")
        title = input("> Title: ")
        publish_year = int(input("> Publish year: "))
        with conn:
            conn.execute('insert into Books(author, title, publish_year) values (?, ?, ?)', (author, title, publish_year))
            print("OK")
    elif cmd == "add_reader":
        name = input("> Name: ")
        with conn:
            conn.execute('insert into Readers(name) values (?)', (name,))
            print("OK")
    elif cmd == "give_b2r":
        name = input("> To: ")
        author = input("> Book author: ")
        title = input("> Book title: ")
        with conn:
            reader_id, book_id = get_id(conn, name, author, title)
            conn.execute('insert into Records(reader_id, book_id, taking_date) values (?, ?, datetime("now", "localtime"))', (reader_id, book_id))
            print("OK")
        pass
    elif cmd == "take_b4r":
        name = input("> From: ")
        author = input("> Book author: ")
        title = input("> Book title: ")
        with conn:
            reader_id, book_id = get_id(conn, name, author, title)
            conn.execute('update Records set returning_date = datetime("now", "localtime") where reader_id = ? AND book_id = ?', (reader_id, book_id))
            print("OK")
    elif cmd == "exit":
        break
    else:
        print(commands_list)