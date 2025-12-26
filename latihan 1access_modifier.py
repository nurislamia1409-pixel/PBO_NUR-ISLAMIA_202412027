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
# Contoh Penggunaan
# ===============================
if __name__ == "__main__":
    m1 = Mahasiswa("23001", "Budi", 3, 3.4)

    print("DATA AWAL")
    print("NIM:", m1.nim)
    print("Nama:", m1.nama)
    print("Semester:", m1.get_semester())
    print("IPK:", m1.get_ipk())

    # Update data
    m1.set_semester(4)
    m1.set_ipk(3.8)

    print("\nSETELAH UPDATE")
    print("Semester:", m1.get_semester())
    print("IPK:", m1.get_ipk())
