# Class MataKuliah
class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"{self.kode} - {self.nama} ({self.sks} SKS)"


# Class ProgramStudi
class ProgramStudi:
    def __init__(self, nama_prodi):
        self.nama_prodi = nama_prodi
        self.mata_kuliah = []

    def tambah_mata_kuliah(self, matkul):
        self.mata_kuliah.append(matkul)

    def __str__(self):
        daftar_mk = "\n   ".join(str(mk) for mk in self.mata_kuliah)
        return f"Program Studi: {self.nama_prodi}\n   {daftar_mk}"


# Class Universitas
class Universitas:
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas
        self.program_studi = []

    def tambah_program_studi(self, prodi):
        self.program_studi.append(prodi)

    def __str__(self):
        daftar_prodi = "\n".join(str(prodi) for prodi in self.program_studi)
        return f"Universitas: {self.nama_universitas}\n{daftar_prodi}"


# -------------------------------------------
# Membuat objek Universitas
univ = Universitas("Universitas Teknologi Nusantara")

# Membuat dua Program Studi
prodi_TI = ProgramStudi("Teknik Informatika")
prodi_SI = ProgramStudi("Sistem Informasi")

# Menambahkan masing-masing 2 Mata Kuliah
prodi_TI.tambah_mata_kuliah(MataKuliah("TI101", "Pemrograman Dasar", 3))
prodi_TI.tambah_mata_kuliah(MataKuliah("TI202", "Struktur Data", 3))

prodi_SI.tambah_mata_kuliah(MataKuliah("SI110", "Analisis Sistem", 3))
prodi_SI.tambah_mata_kuliah(MataKuliah("SI220", "Manajemen Basis Data", 3))

# Menambahkan Prodi ke Universitas
univ.tambah_program_studi(prodi_TI)
univ.tambah_program_studi(prodi_SI)

# Output
print(univ)