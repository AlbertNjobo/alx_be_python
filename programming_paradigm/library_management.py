class Book:
    """Represents a book in a library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books in the library."""

    def __init__(self):
        self._books = []  # Private list to store book objects

    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and checks it out if available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Finds a book by title and returns it to the library."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books available at the moment.")


