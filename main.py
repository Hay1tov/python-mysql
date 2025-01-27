import mysql.connector
import setting


if __name__ == "__main__":
    connection = mysql.connector.connect(
        host=setting.host,
        user=setting.user,
        password=setting.password,
        port=setting.port
    )

    cursor = connection.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {setting.db_name}")
    cursor.execute(f"USE {setting.db_name}")

    # create table
    create_books_table(cursor)
    connection.commit()

    # insert books
    insert_book(
        cursor=cursor,
        title="Hamsa",
        author="Alisher Navoiy",
        published_year=1485,
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