# ==========================
#   CLASS BUKU
# ==========================
class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku
        self._stok = stok               # Protected
        self.__lokasi_rak = lokasi_rak  # Private

    # Getter & Setter lokasi rak (private)
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi_baru):
        self.__lokasi_rak = lokasi_baru

    # Method tambah & kurangi stok
    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah
        else:
            print("Stok tidak mencukupi!")

    # Info Buku
    def info_buku(self):
        return f"{self.kode_buku} - {self.judul} | Stok: {self._stok}"


# ==========================
#   CLASS ANGGOTA
# ==========================
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=3):
        self.id_anggota = id_anggota
        self.nama = nama
        self._maks_pinjam = maks_pinjam      # Protected
        self.__status_aktif = True           # Private
        self.daftar_peminjaman = []          # Aggregation

    # Getter status aktif anggota
    def get_status(self):
        return self.__status_aktif

    # Setter status aktif anggota
    def set_status(self, status):
        self.__status_aktif = status

    # Pinjam buku
    def pinjam_buku(self, buku, tanggal_pinjam, tanggal_kembali):
        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print(f"{self.nama} telah mencapai batas maksimum peminjaman!")
            return None

        if buku._stok <= 0:
            print(f"Stok buku '{buku.judul}' habis!")
            return None

        # kurangi stok buku
        buku.kurangi_stok(1)

        # buat objek peminjaman
        peminjaman = Peminjam(buku.kode_buku, tanggal_pinjam, tanggal_kembali)
        self.daftar_peminjaman.append(peminjaman)

        return peminjaman

    # Mengembalikan buku
    def kembalikan_buku(self, buku):
        if self.daftar_peminjaman:
            buku.tambah_stok(1)
            self.daftar_peminjaman.pop(0)
        else:
            print("Tidak ada buku yang dipinjam.")

    # Info peminjaman anggota
    def info_peminjaman(self):
        if not self.daftar_peminjaman:
            return "Tidak ada peminjaman."

        info = ""
        for p in self.daftar_peminjaman:
            info += p.info_peminjaman() + "\n"
        return info


# ==========================
#   CLASS PEMINJAM (Association)
# ==========================
class Peminjam:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = "Dipinjam"

    def info_peminjaman(self):
        return f"Buku: {self.kode_buku} | Pinjam: {self.tanggal_pinjam} | Kembali: {self.tanggal_kembali} | Status: {self.status}"


# ==========================
#   CLASS PERPUSTAKAAN (Composition)
# ==========================
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []  # Perpustakaan memiliki buku (composition)

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def info_buku(self):
        print("\n=== DAFTAR BUKU ===")
        for b in self.daftar_buku:
            print(b.info_buku())


# =====================================
#   INSTANSIASI & DEMONSTRASI PROGRAM
# =====================================

# 1. Buat 3 buku
b1 = Buku("Algoritma", "Siregar", "BK01", 3, "Rak A1")
b2 = Buku("Basis Data", "Andi", "BK02", 2, "Rak B2")
b3 = Buku("Jaringan Komputer", "Budi", "BK03", 1, "Rak C1")

# 2. Buat 2 anggota
a1 = Anggota("A01", "Mia")
a2 = Anggota("A02", "Rafi")

# Buat perpustakaan dan masukkan buku
perpus = Perpustakaan("Perpus Kampus")
perpus.tambah_buku(b1)
perpus.tambah_buku(b2)
perpus.tambah_buku(b3)

# 3. Anggota 1 pinjam 2 buku
a1.pinjam_buku(b1, "2025-11-01", "2025-11-07")
a1.pinjam_buku(b2, "2025-11-01", "2025-11-07")

# 4. Anggota 2 pinjam 1 buku
a2.pinjam_buku(b3, "2025-11-01", "2025-11-07")

# 5. Pengembalian buku oleh Anggota 1
a1.kembalikan_buku(b1)

# ================================
#   OUTPUT DEMONSTRASI
# ================================
print("\n===== INFORMASI BUKU =====")
perpus.info_buku()

print("\n===== INFORMASI ANGGOTA =====")
print(f"{a1.id_anggota} - {a1.nama}, Status: {a1.get_status()}")
print(f"{a2.id_anggota} - {a2.nama}, Status: {a2.get_status()}")

print("\n===== DAFTAR PEMINJAMAN MIA =====")
print(a1.info_peminjaman())

print("\n===== DAFTAR PEMINJAMAN RAFI =====")
print(a2.info_peminjaman())