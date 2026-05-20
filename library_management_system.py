class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True  # From flowchart 1: "with available = True"


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email


class LibraryService:
    def __init__(self):
        # Dictionaries mentioned in the storage process steps
        self._books = {}
        self._members = {}

    def add_book(self):
        """Implements Flowchart 1: Add Book"""
        print("\n--- Add Book ---")
        # Input steps
        book_id = input("Input: Book ID: ")
        title = input("Input: Book Title: ")
        author = input("Input: Book Author: ")
        
        # Create Book object
        new_book = Book(book_id, title, author)
        
        # Store book in _books dictionary (key = book.book_id)
        self._books[new_book.book_id] = new_book
        
        # Output confirmation
        print(f"Output: \"Book added: {title}\"")

    def register_member(self):
        """Implements Flowchart 2: Register Member"""
        print("\n--- Register Member ---")
        # Input steps
        member_id = input("Input: Member ID: ")
        name = input("Input: Member Name: ")
        email = input("Input: Member Email: ")
        
        # Create Member object
        new_member = Member(member_id, name, email)
        
        # Store member in _members dictionary (key = member.member_id)
        self._members[new_member.member_id] = new_member
        
        # Output confirmation
        print(f"Output: \"Member registered: {name}\"")


def main():
    """Main application loop tying choices to the LibraryService"""
    library_service = LibraryService()
    
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Exit")
        
        # Display menu and read user choice
        choice = input("Enter choice: ")
        
        if choice == "1":
            library_service.add_book()
        elif choice == "2":
            library_service.register_member()
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")


if __name__ == "__main__":
    main()