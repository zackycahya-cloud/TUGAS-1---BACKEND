from person import Person

class Student(Person):
    """
    Class Student sebagai turunan dari Person.
    """
    def __init__(self, name: str, phone: str, email: str, studentNumber: int, averageMark: int, address=None):
        super().__init__(name, phone, email, address)
        self.studentNumber = studentNumber
        self.averageMark = averageMark

    def isEligibleToEnroll(self, course: str) -> bool:
        """Menentukan apakah student bisa enroll."""
        return self.averageMark >= 60

    def getSeminarsTaken(self) -> int:
        """Mengembalikan jumlah seminar (dummy)."""
        return 5
