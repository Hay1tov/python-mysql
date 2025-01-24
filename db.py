from mysql.connector.cursor import MySQLCursor


def create_books_table(cursor: MySQLCursor):
    """
    Create a 'books' table in the database if it doesn't exist.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(128) NOT NULL,
            author VARCHAR(64) NOT NULL,
            published_year INT,
            genre VARCHAR(32) NOT NULL,
            price FLOAT NOT NULL,
            available BOOLEAN NOT NULL
        );
    """)
    
def insert_book(cursor: MySQLCursor, title, author, published_year, genre, price, available):
    """
    Insert a new book into the 'books' table.
    """
    cursor.execute("""
        INSERT INTO books (title, author, published_year, genre, price, available)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, author, published_year, genre, price, available))

def show_all_books(cursor: MySQLCursor):
    """
    Retrieve and display all books from the 'books' table.
    """
    cursor.execute("""
        SELECT * FROM books
    """)
    books = cursor.fetchall()

    for book in books:
        print(book)