class UmurTidakValidError(Exception):
    """Umur tidak masuk akal (kurang dari 0 atau tidak sesuai aturan)."""
    pass


class UmurTerlaluMudaError(Exception):
    """Umur terlalu muda (<5)."""
    pass


class UmurTerlaluTuaError(Exception):
    """Umur terlalu tua (>100)."""
    pass


class AkunTidakDiizinkanError(Exception):
    """Akun hanya boleh dibuat jika umur ≥ 18."""
    pass


def set_umur(umur):
    """Validasi umur dan lempar custom exception sesuai kondisi."""

    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")

    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda! Minimal 5 tahun.")

    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua! Maksimum 100 tahun.")

    return umur


def daftar_akun(umur):
    """Validasi umur 18 ke atas yang boleh daftar akun."""

    if umur < 18:
        raise AkunTidakDiizinkanError("Akun hanya boleh untuk umur 18 ke atas.")
    
    return "Akun berhasil dibuat!"


if __name__ == "__main__":

    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur_valid = set_umur(u)
            print("Umur valid:", umur_valid)

            # Coba daftar akun
            status = daftar_akun(umur_valid)
            print(status)

            break  # keluar jika semua valid

        except ValueError:
            print("Error: Input harus berupa bilangan bulat!")

        except UmurTidakValidError as e:
            print("Error:", e)

        except UmurTerlaluMudaError as e:
            print("Error:", e)

        except UmurTerlaluTuaError as e:
            print("Error:", e)

        except AkunTidakDiizinkanError as e:
            print("Error:", e)

        print("Silahkan coba lagi.\n")