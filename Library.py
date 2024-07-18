import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='groudonnoir5',
        database='books'
    )
    return connection


def search_books(search_term):
    results = []
    connection = None
    cursor = None

    try:
        connection = create_connection()

        cursor = connection.cursor()

        print(f"Searching for books with title containing: {search_term}")

        query = "SELECT Book_Title FROM books WHERE Year_Of_Publication LIKE %s"
        values = ("%" + search_term + "%",)

        cursor.execute(query, values)

        results = cursor.fetchall()

        print(f"Number of results found: {len(results)}")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return results

if __name__ == "__main__":
    search_term = "1998"
    books = search_books(search_term)
    for book in books:
        print(book)