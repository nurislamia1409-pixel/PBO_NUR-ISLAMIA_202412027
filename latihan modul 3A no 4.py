class Penulis:
    def __init__(self, nama):
        self.nama = nama


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis  # Composition


# Demonstrasi
p = Penulis("Nur islamia")
b = Buku("Hujan", p)

print("Judul Buku:", b.judul)
print("Nama Penulis:", b.penulis.nama)