library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    title = input("What is the book's title?: ")
    author = input("Who is the book's author?: ")
    book = (title, author)
    for books in library:
        (titles, _) = books
        if title == titles:
            print("We already gots that")
            break
        else:
            library.append(book)
            print(library)
            break

add_book(library)