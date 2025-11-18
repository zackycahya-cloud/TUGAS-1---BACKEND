from address import Address
from student import Student
from professor import Professor

def main():
    addr = Address("Jl. Kenanga", "Denpasar", "Bali", 80221, "Indonesia")

    student = Student("Budi", "08123456", "budi@mail.com", 12345, 85, addr)
    professor = Professor("Dr. Ida", "08999999", "ida@mail.com",
                          15000000, 101, 10, 3, addr)

    print(student.name, "- Eligible:", student.isEligibleToEnroll("OOP"))
    print("Address:", student.address.outputAsLabel())

    student.purchaseParkingPass()
    professor.purchaseParkingPass()

if __name__ == "__main__":
    main()
