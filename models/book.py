class Book:

    def __init__(self, title, author, year, available = False, id = None):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self.id = id