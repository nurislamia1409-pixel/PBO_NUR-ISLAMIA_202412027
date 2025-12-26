class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim              # public
        self.nama = nama            # public
        self._semester = semester   # protected
        self.__ipk = ipk            # private

    # Getter semester (protected)
    def get_semester(self):
        return self._semester

    # Setter semester (protected)
    def set_semester(self, sem):
        if sem <= 0:
            raise ValueError("Semester tidak boleh kurang dari 1.")
        self._semester = sem

    # Getter IPK (private)
    def get_ipk(self):
        return self.__ipk

    # Setter IPK (private)
    def set_ipk(self, nilai):
        if nilai < 0 or nilai > 4:
            raise ValueError("IPK harus di antara 0 - 4.")
        self.__ipk = nilai


# ===============================
# Bagian (b) & (c)
# ===============================
if __name__ == "__main__":
    # Membuat 2 objek mahasiswa
    m1 = Mahasiswa("23001", "Budi", 3, 3.4)
    m2 = Mahasiswa("23002", "Siti", 5, 3.9)

    print("=== DATA AWAL ===")
    print("M1:", m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
    print("M2:", m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())

    # ===============================
    # Bagian (c) — Ganti semester & IPK
    # ===============================

    m1.set_semester(4)   # Contoh: semester Budi diganti ke 4
    m1.set_ipk(3.75)     # Contoh: IPK Budi diganti ke 3.75

    m2.set_semester(6)   # Contoh: semester Siti diganti ke 6
    m2.set_ipk(3.95)     # Contoh: IPK Siti diganti ke 3.95

    print("\n=== SETELAH DIUPDATE ===")
    print("M1:", m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
    print("M2:", m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())
