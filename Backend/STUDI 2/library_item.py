class LibraryItem:
    """
    Class dasar untuk item perpustakaan.
    """
    def __init__(self, item_id: int, title: str):
        self.item_id = item_id
        self.title = title

    def display_info(self):
        """Menampilkan informasi item."""
        print(f"ID: {self.item_id}, Title: {self.title}")

    def calculate_late_fee(self, days_late: int) -> float:
        """Menghitung denda keterlambatan."""
        return days_late * 1.0
