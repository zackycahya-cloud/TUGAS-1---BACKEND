from address import Address

class Person:
    """
    Class induk untuk Student dan Professor.
    """
    def __init__(self, name: str, phoneNumber: str, emailAddress: str, address: Address = None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = address

    def purchaseParkingPass(self):
        """Method simulasi pembelian kartu parkir."""
        print(f"{self.name} has purchased a parking pass.")
