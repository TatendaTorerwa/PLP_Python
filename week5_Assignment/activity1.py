class Book:
    # Constructor to initialize a book
    def __init__(self, title, author, pages, cover_type):
        self.title = title
        self.author = author
        self.pages = pages
        self.cover_type = cover_type

    # Method to describe the book
    def describe(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages, {self.cover_type} cover."

    # Method to simulate reading
    def read(self):
        print(f"You are reading '{self.title}'. Enjoy!")

# Counterbook class inherits from Book
class Counterbook(Book):
    def __init__(self, title, author, pages, cover_type, is_graded):
        super().__init__(title, author, pages, cover_type)
        self.is_graded = is_graded  # Additional attribute specific to Counterbook

    # Override the describe method to include grading status
    def describe(self):
        graded_status = "graded" if self.is_graded else "not graded"
        return super().describe() + f" This is a {graded_status} counterbook."

    # Additional method specific to Counterbook
    def mark(self):
        if self.is_graded:
            print(f"The counterbook '{self.title}' is being marked.")
        else:
            print(f"The counterbook '{self.title}' does not require grading.")

# Example usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, "hardcover")
counterbook = Counterbook("Math Workbook", "Mr. Johnson", 120, "paperback", True)

print(book.describe())
book.read()

print(counterbook.describe())
counterbook.mark()
