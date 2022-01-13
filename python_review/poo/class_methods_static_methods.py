# class ClassTest:
#
#     def instance_method(self):
#         print(f'called instance_method of {self}')
#
#     @classmethod
#     def class_method(cls):
#         print(f'called class_method of {cls}')
#
#     @staticmethod
#     def static_method():
#         print('called static method')
#
#
# # test = ClassTest()
# # test.instance_method()
# # ClassTest.instance_method(test)
# # ClassTest.class_method()
# ClassTest.static_method()

class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, {self.weight}g>'

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


# book = Book('A fuego lento', 'hardcover', 900)

book = Book.hardcover('A fuego lento', 1300)
light = Book.paperback('Apache Hadoop', 200)

print(book)
print(light)
