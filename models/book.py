class Book:

    def __init__(self, name, author, year, available = False, id = None):
        self.name = name
        self.author = author
        self.year = year
        self.available = available
        self.id = id