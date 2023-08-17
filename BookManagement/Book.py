class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Publication Year:', self.publication_year)

book = Book('Alice in Wonderland', 'Charles Lutwidge Dodgson', 2010)

book.display_info()