import sqlite3

con = sqlite3.connect("booksbase.sql")
cur = con.cursor()
while True:
    picturepath = input("Путь: ")
    title = input("Название: ")
    author = input("Автор: ")
    year = int(input("Год выпуска: "))
    genre = input("Жанр: ")
    if not picturepath:
        cur.execute("""INSERT INTO books (picturepath, title, author, year, genre) VALUES(NULL, ?, ?, ?, ?)""",
                (title, author, year, genre))
    else:
        cur.execute("""INSERT INTO books (picturepath, title, author, year, genre) VALUES(?, ?, ?, ?, ?)""",
                    (picturepath, title, author, year, genre))
    con.commit()
    print()
