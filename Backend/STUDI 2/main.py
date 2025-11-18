from author import Author
from book import Book
from library_member import LibraryMember

def main():
    author = Author("Tere Liye", 1979)
    book = Book("123-XYZ", "Bumi", author, 1)

    member = LibraryMember(101, "Andi")
    member.borrow_item(book)

    book.display_info()

    late_fee = book.calculate_late_fee(3)
    print("Late Fee:", late_fee)

    member.return_item(book)

if __name__ == "__main__":
    main()
