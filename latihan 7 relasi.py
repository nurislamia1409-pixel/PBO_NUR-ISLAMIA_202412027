class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai: Nilai):
        self.daftar_nilai.append(nilai)

    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


# ===========================
# REPORT PROGRAM (dari soal)
# ===========================
def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"\nLAPORAN PROGRAM STUDI: {prodi.nama}")
    print("Mata Kuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
    print("Mahasiswa dan Nilai Rata-rata:")

    for m in semua_mahasiswa:
        relevan = [
            n for n in m.daftar_nilai
            if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)
        ]

        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"  {m.nim} - {m.nama}: {round(avg, 2)}")

    print("-" * 40)


def tampilkan_matakuliah_semua_prodi(universitas):
    print("\n=== DAFTAR MATA KULIAH PER PROGRAM STUDI ===")
    for prodi in universitas.programs:
        print(f"{prodi.nama}: ", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]))


def tampilkan_nilai_mahasiswa(daftar_mhs):
    print("\n=== DAFTAR NILAI MAHASISWA ===")
    for m in daftar_mhs:
        nilai_list = ", ".join([f"{n.kode_mk}: {n.skor}" for n in m.daftar_nilai]) or "-"
        print(f"{m.nim} - {m.nama} -> {nilai_list}")


def tampilkan_rata_rata(daftar_mhs):
    print("\n=== RATA-RATA NILAI MAHASISWA ===")
    for m in daftar_mhs:
        print(f"{m.nim} - {m.nama}: {round(m.rata_rata(), 2)}")


# ===========================
# PROGRAM UTAMA
# ===========================
if __name__ == "__main__":
    # a. Tambah 3 Program Studi
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_bd = uni.buat_program("Bisnis Digital")

    # b. Tambahkan 2 mata kuliah untuk tiap prodi
    prodi_ti.tambah_matakuliah(MataKuliah("TI101", "Pemrograman Dasar"))
    prodi_ti.tambah_matakuliah(MataKuliah("TI102", "Struktur Data"))

    prodi_si.tambah_matakuliah(MataKuliah("SI201", "Basis Data"))
    prodi_si.tambah_matakuliah(MataKuliah("SI202", "Analisis Sistem"))

    prodi_bd.tambah_matakuliah(MataKuliah("BD301", "Pemasaran Digital"))
    prodi_bd.tambah_matakuliah(MataKuliah("BD302", "Business Analytics"))

    # c. Buat 3 mahasiswa + nilai
    m1 = Mahasiswa("23001", "Farhan")
    m2 = Mahasiswa("23002", "Nia")
    m3 = Mahasiswa("23003", "Lia")

    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))

    m2.tambah_nilai(Nilai("SI201", 88))
    m2.tambah_nilai(Nilai("SI202", 80))

    m3.tambah_nilai(Nilai("BD301", 92))
    m3.tambah_nilai(Nilai("BD302", 89))

    # d. Tampilkan daftar mata kuliah
    tampilkan_matakuliah_semua_prodi(uni)

    # e. Tampilkan nilai mahasiswa
    tampilkan_nilai_mahasiswa([m1, m2, m3])

    # f. Tampilkan rata-rata nilai mahasiswa
    tampilkan_rata_rata([m1, m2, m3])

    # ===========================
    # g. PANGGIL REPORT PROGRAM!
    # ===========================
    print("\n=== LAPORAN DETAIL PER PROGRAM STUDI ===")
    for prodi in uni.programs:
        report_program(prodi, [m1, m2, m3])