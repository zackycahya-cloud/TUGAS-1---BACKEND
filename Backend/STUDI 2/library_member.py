from typing import List
from library_item import LibraryItem

class LibraryMember:
    """
    Representasi anggota perpustakaan.
    """
    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_items: List[LibraryItem] = []

    def borrow_item(self, item: LibraryItem):
        """Meminjam item."""
        self.borrowed_items.append(item)
        print(f"{self.name} borrowed {item.title}")

    def return_item(self, item: LibraryItem):
        """Mengembalikan item."""
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            print(f"{self.name} returned {item.title}")
