import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class Tugas:
    def __init__(self, nama, status="Belum Selesai"):
        self.nama = nama
        self.status = status


class AplikasiToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("500x400")

        # List of objects
        self.daftar_tugas = []

        # Frame input
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Nama Tugas:").grid(row=0, column=0)
        self.entry_tugas = tk.Entry(frame_input, width=30)
        self.entry_tugas.grid(row=0, column=1, padx=5)

        tk.Button(
            frame_input,
            text="Tambah",
            command=self.tambah_tugas
        ).grid(row=0, column=2, padx=5)

        # Frame tombol
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.tandai_selesai).pack(side=tk.LEFT, padx=5)

        # Frame tabel
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            frame_tabel,
            columns=("Tugas", "Status"),
            show="headings"
        )
        self.tree.heading("Tugas", text="Nama Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def tambah_tugas(self):
        nama = self.entry_tugas.get()
        if nama:
            tugas_baru = Tugas(nama)
            self.daftar_tugas.append(tugas_baru)
            self.tree.insert("", tk.END, values=(nama, tugas_baru.status))
            self.entry_tugas.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama tugas tidak boleh kosong!")

    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            self.tree.delete(selected[0])
            del self.daftar_tugas[index]
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")

    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]

            nama_baru = simpledialog.askstring(
                "Edit Tugas",
                "Masukkan nama tugas baru:",
                initialvalue=tugas.nama
            )

            if nama_baru:
                tugas.nama = nama_baru
                self.tree.item(
                    selected[0],
                    values=(tugas.nama, tugas.status)
                )
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

    def tandai_selesai(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]
            tugas.status = "Selesai"

            self.tree.item(
                selected[0],
                values=(tugas.nama, tugas.status)
            )
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan ditandai selesai!")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiToDoList(root)
    root.mainloop()