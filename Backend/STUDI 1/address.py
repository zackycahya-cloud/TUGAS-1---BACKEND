class Address:
    """
    Representasi alamat tempat tinggal seseorang.
    """
    def __init__(self, street: str, city: str, state: str, postalCode: int, country: str):
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

    def validate(self) -> bool:
        """Validasi sederhana memastikan postalCode angka positif."""
        return isinstance(self.postalCode, int) and self.postalCode > 0

    def outputAsLabel(self) -> str:
        """Mengembalikan alamat dalam format label."""
        return f"{self.street}, {self.city}, {self.state} {self.postalCode}, {self.country}"
