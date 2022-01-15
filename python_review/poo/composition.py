class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f'BookShelf with {len(self.books)} books.'


class Book(BookShelf):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book: {self.name}'


book = Book('A fuego lento')
book2 = Book('La melancolia de los feos')
shelf = BookShelf(book, book2)
print(shelf)
