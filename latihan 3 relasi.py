# Class Nilai
class Nilai:
    def __init__(self, kode_mk, skor):
        self.kode_mk = kode_mk
        self.skor = skor

    def __str__(self):
        return f"{self.kode_mk}: {self.skor}"


# Class Mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    def __str__(self):
        nilai_str = "\n   ".join(str(n) for n in self.daftar_nilai)
        return f"Mahasiswa: {self.nama} ({self.nim})\n   {nilai_str}"


# ---------------------------------------------------------
# Membuat 3 Mahasiswa
mhs1 = Mahasiswa("230001", "Mia")
mhs2 = Mahasiswa("230002", "Rafi")
mhs3 = Mahasiswa("230003", "Dewi")

# Membuat beberapa objek Nilai & menambahkannya
mhs1.tambah_nilai(Nilai("TI101", 88))
mhs1.tambah_nilai(Nilai("TI202", 92))

mhs2.tambah_nilai(Nilai("SI110", 85))
mhs2.tambah_nilai(Nilai("SI220", 90))

mhs3.tambah_nilai(Nilai("TI101", 78))
mhs3.tambah_nilai(Nilai("SI110", 80))


# Tampilkan hasil
print(mhs1)
print()
print(mhs2)
print()
print(mhs3)