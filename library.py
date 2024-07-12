library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    title = input("What is the book's title?: ")
    author = input("Who is the book's author?: ")
    book = (title, author)
    for books in library:
        if book[0] == books[0] in library:
            print("We already gots that")
        else:
            library.append(book)
            print(library)
            break

add_book(library)