class Book:
    def __init__(self, title, author, year):
        """Initializes a Book instance with title, author, and year."""
        self.title =  title
        self.author = author
        self.year = year

    def __del__(self):
        """Prints "Deleting (title of the book)" upon object deletion"""

        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a string in the format "(title) by (author), published in (year)"."""

        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
