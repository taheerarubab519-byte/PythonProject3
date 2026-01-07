class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages= pages

    def print_information(self):
        print(f"Book name is: {self.name}, Author is: {self.author}, Pages are: {self.pages}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        print(f"Magazine name is: {self.name}, Chief Editor is: {self.editor}")

magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No.6", "Rosa Liksom", 192)

magazine.print_information()
book.print_information()