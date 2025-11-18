Studi Kasus 1 – Person, Student, Professor, Address
Studi kasus ini mengimplementasikan relasi:
Inheritance: Student dan Professor mewarisi Person
Association: Person memiliki (0..1) Address
Supervision relationship: Professor dapat supervise Student (di diagram, namun tidak diwajibkan pada kode sesuai instruksi)
Fitur Utama
Validasi pada objek Address.
Method spesifik:
purchaseParkingPass() pada Person.
isEligibleToEnroll() dan getSeminarsTaken() pada Student.
Penyimpanan atribut salary, staffNumber, yearsOfService, dan numberOfClasses pada Professor.
Cara Menjalankan Studi Kasus 1
cd StudiKasus1
python main.py

Studi Kasus 2 – Book, Author, LibraryItem, LibraryMember
Deskripsi
Studi kasus ini mengimplementasikan sistem perpustakaan sederhana dengan konsep
Inheritance: Book mewarisi LibraryItem
Association: Book memiliki Author
Aggregation: LibraryMember memiliki daftar LibraryItem yang dipinjam
Fitur Utama
Informasi penulis & perhitungan umur (get_age()).
Override method display_info() dan calculate_late_fee() pada Book.
Proses peminjaman & pengembalian item oleh member.
Cara Menjalankan Studi Kasus 2
cd StudiKasus2
python main.py

Proses Berpikir (Ringkasan)
Membaca class diagram dan mengidentifikasi relasi antar-class.
Menentukan struktur folder agar rapi dan sesuai instruksi tugas.
Membuat class satu per satu sesuai atribut dan method pada diagram.
Mengimplementasikan inheritance, association, dan override method.
Menambahkan dokumentasi pada setiap class & method.
Membuat main.py sebagai entry point dengan contoh penggunaan object.
Menjalankan program untuk memastikan tidak ada error.

Dokumentasi Penggunaan AI
Dalam proses penyelesaian tugas ini, saya memanfaatkan bantuan AI hanya untuk:
Menjelaskan class diagram
Menghasilkan template kode OOP yang sesuai instruksi
Mempersiapkan README.md
