import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='[redacted]',
        database='books'
    )
    return connection

def add_book(Book_Title, Book_Author, Year_Of_Publication, ISBN):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO books (Book_Title, Book_Author, Year_of_Publication, ISBN) VALUES (%s, %s, %s, %s)"
        values = (Book_Title, Book_Author, Year_Of_Publication, ISBN)

        cursor.execute(query, values)

        connection.commit()

        print("Book added successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def check_out_book(ISBN, Borrower_ID, Borrow_Date, Due_Date):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO transactions (ISBN, Borrower_ID, Borrow_Date, Due_Date) VALUES (%s, %s, %s, %s)"
        values = (ISBN, Borrower_ID, Borrow_Date, Due_Date)

        cursor.execute(query, values)

        connection.commit()

        print("Book checked out successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def check_in_book(ISBN, Borrower_ID, Borrow_Date, Due_Date):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "INSERT INTO transactions (ISBN, Borrower_ID, Borrow_Date, Due_Date) VALUES (%s, %s, %s, %s)"
        values = (ISBN, Borrower_ID, Borrow_Date, Due_Date)

        cursor.execute(query, values)

        connection.commit()

        print("Book checked out successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def check_in_book(Transaction_ID, Return_Date):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE transactions SET Return_Date = %s WHERE Transaction_ID = %s"
    values = (Return_Date, Transaction_ID)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def search_books(search_term):
    results = []
    connection = None
    cursor = None

    try:
        connection = create_connection()

        cursor = connection.cursor()

        print(f"Searching for books with title containing: {search_term}")

        query = "SELECT * FROM books WHERE Book_Title LIKE %s"
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

def main():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. Check Out Book")
        print("3. Check In Book")
        print("4. Search Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            Book_Title = input("Enter book title: ")
            Book_Author = input("Enter book author: ")
            ISBN = int(input("Enter ISBN: "))
            Year_Of_Publication = int(input("Enter year published: "))
            add_book( Book_Title, Book_Author, Year_Of_Publication, ISBN)

        elif choice == '2':
            ISBN = int(input("Enter ISBN: "))
            Borrower_ID = int(input("Enter borrower ID: "))
            Borrow_Date = input("Enter borrow date (YYYY-MM-DD): ")
            Due_Date = input("Enter due date (YYYY-MM-DD): ")
            check_out_book(ISBN, Borrower_ID, Borrow_Date, Due_Date)

        elif choice == '3':
            Transaction_ID = int(input("Enter transaction ID: "))
            Return_Date = input("Enter return date (YYYY-MM-DD): ")
            check_in_book(Transaction_ID, Return_Date)

        elif choice == '4':
            search_term = input("Enter search term: ")
            books = search_books(search_term)
            for book in books:
                print(book)
            search_books(search_term)

        elif choice == '5':
            break


if __name__ == "__main__":
    main()