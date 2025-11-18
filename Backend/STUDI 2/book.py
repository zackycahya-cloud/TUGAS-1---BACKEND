from library_item import LibraryItem
from author import Author

class Book(LibraryItem):
    """
    Representasi buku sebagai item perpustakaan.
    """
    def __init__(self, isbn: str, title: str, author: Author, item_id: int):
        super().__init__(item_id, title)
        self.isbn = isbn
        self.author = author

    def display_info(self):
        """Override: tampilkan info buku lengkap."""
        print(f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author.name}")

    def calculate_late_fee(self, days_late: int) -> float:
        """Denda buku."""
        return days_late * 2.0
