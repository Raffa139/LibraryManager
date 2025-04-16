# Library Manager

**Project Goal**:
To develop a command-line interface (CLI) application in Python for managing a
small library of books. This application will allow users to interact with a library database
stored in a simple CSV file, enabling them to add, view, search, borrow, and return books.

## Functionality

- **Adding Books**:
  Allow users to input the author, title, publication year, and keywords
  for a new book, which will then be added as a new entry in the CSV file.
  The initial borrowing status for a newly added book will be "available".
- **Viewing All Books**:
  Display a formatted list of all books currently in the library, including their author, title,
  publication year, borrowing status, and keywords.
- **Searching Books**:
  Implement functionality to search for books based on Title (partial or exact match),
  Author (partial or exact match), Keywords (any matching keyword).
- **Borrowing Books**:
  Allow users to mark a book as "borrowed" based on its title.
  The application will check if the book is currently available before allowing the borrowing
  action.
- **Returning Books**:
  Allow users to mark a borrowed book as "available" based on its title.
- **Data Storage**:
  The library data (books) will be persistently stored in a simple CSV (Comma Separated Values)
  file.
  Each row in the CSV will represent a book, and the columns will correspond to the book attributes.

## How to run

To start the Library Manager just run the ``src/main.py`` file.

After exiting the first time, a ``library.txt`` file will be created next to ``main.py``, if books
have been created.\
The file contains all created books. Each line is one book with its values being comma separated.

The next time the Library Manager is started, it will load all books from the ``library.txt`` file.