from typing import List, Tuple, Set, Dict


# def list_avg(sequence: List) -> float:
#     return sum(sequence) / len(sequence)
#
#
# list_avg(123)


# class Book:
#     def __init__(self, name: str, page_count: int):
#         self.name = name
#         self.page_count = page_count
class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f'<Book {self.name}, {self.book_type}, {self.weight}g>'

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f'BookShelf with {len(self.books)} books.'
