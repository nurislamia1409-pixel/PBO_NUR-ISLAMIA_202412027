class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"


# Contoh penggunaan
p = Person("Nur Islamia", 21)
print(p.info())