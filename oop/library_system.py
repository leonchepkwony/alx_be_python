# ============================
# library_system.py
# ============================

# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)   # Call Book constructor
        self.file_size = file_size        # Unique attribute

    def __str__(self):
        return f"EBook: {self.title} by {self.author} - File size: {self.file_size}KB"


# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)   # Call Book constructor
        self.page_count = page_count      # Unique attribute

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author} - Page Count: {self.page_count}"


# Composition: Library class
class Library:
    def __init__(self):
        self.books = []  # A collection of Book/EBook/PrintBook instances

    def add_book(self, book):
        """Add any book type to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all stored books."""
        if not self.books:
            print("The library has no books.")
            return
        
        for book in self.books:
            print(book)
