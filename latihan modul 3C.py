class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"


class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)   # memanggil konstruktor Person
        self.nim = nim

    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur} tahun, NIM: {self.nim}"


# Contoh penggunaan
m1 = Mahasiswa("Nur Islamia", 21, "202412027")
print(m1.info())