from person import Person

class Professor(Person):
    """
    Class Professor sebagai turunan dari Person.
    """
    def __init__(self, name: str, phone: str, email: str,
                 salary: int, staffNumber: int,
                 yearsOfService: int, numberOfClasses: int, address=None):
        super().__init__(name, phone, email, address)
        self.salary = salary
        self._staffNumber = staffNumber
        self._yearsOfService = yearsOfService
        self._numberOfClasses = numberOfClasses
