class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


# --- Membuat objek mata kuliah ---
mk1 = MataKuliah("TI101", "Pemrograman Dasar")
mk2 = MataKuliah("TI102", "Basis Data")

# --- Membuat objek mahasiswa ---
mhs1 = Mahasiswa("23001", "Budi")
mhs2 = Mahasiswa("23002", "Siti")
mhs3 = Mahasiswa("23003", "Rani")

# --- Mendaftarkan mahasiswa ke mata kuliah ---
mk1.tambah_mahasiswa(mhs1)
mk1.tambah_mahasiswa(mhs2)

mk2.tambah_mahasiswa(mhs2)
mk2.tambah_mahasiswa(mhs3)

# --- Menampilkan output sesuai soal ---
print("Daftar Mahasiswa", mk1.nama)
print(mk1.daftar_mahasiswa())
print("Jumlah:", mk1.jumlah_mahasiswa())

print("\nDaftar Mahasiswa", mk2.nama)
print(mk2.daftar_mahasiswa())
print("Jumlah:", mk2.jumlah_mahasiswa())