from abc import ABC, abstractmethod

# 1. ABSTRACTION - Abstract Class Pengguna
class Pengguna(ABC):
    """Abstract class untuk pengguna sistem."""
    
    def __init__(self, nama):
        self.nama = nama
    
    @abstractmethod
    def akses(self):
        """Abstract method untuk hak akses pengguna."""
        pass


# 2. ABSTRACTION - Class Turunan Member
class Member(Pengguna):
    """Class turunan dari Pengguna dengan atribut poin."""
    
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin
    
    def akses(self):
        """Implementasi method akses untuk member."""
        return f"Hak akses Member: {self.nama} dapat mengakses fitur premium dan mendapatkan diskon khusus."
    
    # SPECIAL METHODS
    def __str__(self):
        """Menampilkan informasi member."""
        return f"Member: {self.nama} – Poin: {self.poin}"
    
    def __add__(self, other):
        """Menjumlahkan poin dua member."""
        if isinstance(other, Member):
            return self.poin + other.poin
        return NotImplemented
    
    def __len__(self):
        """Mengembalikan panjang nama member."""
        return len(self.nama)


# 4. CUSTOM EXCEPTION
class PoinTidakValidError(Exception):
    """Custom exception untuk poin yang tidak valid."""
    pass


# EXCEPTION HANDLING - Program utama
def main():
    """Program utama untuk input dan proses member."""
    
    print("="*60)
    print("PROGRAM SISTEM MEMBER DENGAN ABSTRACTION")
    print("="*60 + "\n")
    
    member_list = []
    
    for i in range(2):
        while True:
            try:
                print(f"Masukkan data Member {i+1}:")
                nama = input(f"Nama Member {i+1}: ").strip()
                
                if nama == "":
                    print("Error: Nama tidak boleh kosong.\n")
                    continue
                
                poin_input = input(f"Poin Member {i+1}: ").strip()
                
                if poin_input == "":
                    raise ValueError("Input poin tidak boleh kosong.")
                
                poin = int(poin_input)
                
                if poin < 0:
                    raise PoinTidakValidError("Poin tidak boleh negatif.")
                
                member = Member(nama, poin)
                member_list.append(member)
                print("Member berhasil ditambahkan.\n")
                break
                
            except ValueError:
                print("Error: Input poin harus berupa angka.\n")
            except PoinTidakValidError as e:
                print(f"Custom Error: {e}\n")
    
    m1, m2 = member_list
    
    print("\n" + "="*60)
    print("HASIL DATA MEMBER")
    print("="*60 + "\n")
    
    # Info member
    print("1. Info Member:")
    print(m1)
    print(m2, "\n")
    
    # Hak akses
    print("2. Hak Akses:")
    print(m1.akses())
    print(m2.akses(), "\n")
    
    # Penjumlahan poin
    print("3. Jumlah Total Poin:")
    print(m1 + m2, "\n")
    
    # Panjang nama
    print("4. Panjang Nama:")
    print(len(m1))
    print(len(m2))
    
    print("\n" + "="*60)
    print("Program selesai.")
    print("="*60)


if __name__ == "__main__":
    main()