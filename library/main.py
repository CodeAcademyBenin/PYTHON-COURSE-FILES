import sqlite3 as sql

books = [
    {
        'title': 'Rich Dad Poor Dad',
        'author': 'Robert Kiyosaki',
        'category': 'Finance',
        'leased': True
    },
    {
        'title': 'The GodFather',
        'author': 'Mario Puzo',
        'category': 'Crime',
        'leased': False
    },
    {
        'title': 'Robinson Crusoe',
        'author': 'Daniel Defoa',
        'category': 'Adventure',
        'leased': False
    },
    {
        'title': 'In The Heart Of The Sea',
        'author': 'Johnny Depp',
        'category': 'Adventure',
        'leased': True
    },
    {
        'title': 'Romeo And Juliet',
        'author': 'Austin Pearl',
        'category': 'Romance',
        'leased': False
    }
]

try:
    conn = sql.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE IF EXISTS book""")

    table = """CREATE TABLE book (
            title VARCHAR(255) NOT NULL,
            author CHAR(25) NOT NULL,
            category CHAR(25)
        )
    """ 
    cursor.execute(table)
    for data in books:
        insert_query = f"""INSERT INTO book VALUES ('{data['title']}','{data['author']}','{data['category']}');"""
        # insert books into the book table.
        cursor.execute(insert_query)
    print("Shelve is ready!!!\n")

    while True:
        print("""Choose a task to perform: 
            A. Add a book           B. Search for a book
            C. Update a book        D. Remove a book  
            E. View all book        F. Exit    
        """)
        option = input().upper()

        if option == 'A':
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            category = input("Enter Book Category: ")

            query = """INSERT INTO book VALUES(?, ?, ?)"""
            cursor.execute(query, (title, author, category))

            print("\n[+] Book Has Been Added To Shelf!!!")

        elif option == 'B':
            search_value = input("Enter Search String: ")

            query = """SELECT * FROM book WHERE title like ? """
            result = cursor.execute(query, (f"{search_value}%",))
            print(result.fetchall())
            num_of_result = len(result.fetchall())

            if num_of_result >= 1:
                print(f"[+] Found {num_of_result} Books!!!")
                print("[+]", result.fetchall())
            else:
                print("[-] Could Not Find Any Book!!!")

        elif option == 'D':
            book_title = input("Enter Book Title: ")
            query = """DELETE FROM book WHERE title=?"""
            cursor.execute(query, (book_title,))
            conn.commit()
            print(f"[+] Book {book_title} has been removed from shelf!!!",)

        elif option == 'E':
            query = """SELECT * FROM book"""
            result = cursor.execute(query)
            print("[+]", result.fetchall())

        elif option == 'F':
            print("Shelf Closed!!!")
            break
except sql.Error as error:
    print(f"[-]: {error}")
finally:
    conn.close()