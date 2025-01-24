import mysql.connector
import settings
from db import (
    create_books_table,
    insert_book,
    show_all_books,
)


if __name__ == "__main__":
    connection = mysql.connector.connect(
        host=settings.host,
        user=settings.user,
        password=settings.password,
        port=settings.port
    )

    cursor = connection.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.db_name}")
    cursor.execute(f"USE {settings.db_name}")

    # create table
    create_books_table(cursor)
    connection.commit()

    # insert books
    insert_book(
        cursor=cursor,
        title="Hamsa",
        author="Alisher Navoiy",
        published_year=1470,
        genre='Roman',
        price=20,
        available=True
    )
    connection.commit()

    # show books
    show_all_books(cursor)

    # close
    cursor.close()
    connection.close()