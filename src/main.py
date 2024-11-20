import repository as repo

from menu import Menu
from add_action import AddAction
from list_action import ListAction
from search_action import SearchAction
from book import Book, PublicationYear, Title, Author
from close_menu_action import CloseMenuAction

# print("=== Library Manager ===")
# print("1. Add book")
# print("2. List all books")
# print("3. Search books")
# print("4. Borrow/Return book")
# print("5. Save and exit")

book_repo = repo.instance((
    Book(Title("Musterbuch"), Author("Max Muster"), PublicationYear("2000")),
    Book(Title("Das Buch"), Author("Artur Author"), PublicationYear("2020")),
    Book(Title("Physik für Einsteiger"), Author("Albert Einstein"), PublicationYear("1975")),
))

menu = Menu("=== Library Manager ===")

menu.register_cmd("1", "Add book", AddAction())
menu.register_cmd("2", "List all books", ListAction())
menu.register_cmd("3", "Search books", SearchAction())
menu.register_cmd("5", "Save and exit", CloseMenuAction())

while not menu.close_requested:
    menu.take_cmd()

# cmd = input()
#
# while cmd not in ["1", "2", "3", "4", "5"]:
#     cmd = input()
#
# if cmd == "1":
#     print("Add book:")
#
#     title = input("Title: ")
#     author = input("Author: ")
#     year = input("Year: ")
#
#     book = Book(title, author, year)
#     book_repo.add(book)
# elif cmd == "2":
#     print("List all books:")
#
#     all_books = book_repo.get_all()
#     for book in all_books:
#         print(book)
# elif cmd == "3":
#     print("Search books")
# elif cmd == "4":
#     print("Borrow/Return book")
# elif cmd == "5":
#     print("Save and exit")
