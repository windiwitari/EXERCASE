
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun = tahun

    def set_judul(self, judul):
        self.__judul = judul

    def set_penulis(self, penulis):
        self.__penulis = penulis

    def set_tahun(self, tahun):
        self.__tahun = tahun

    def informasi_buku(self):
        return f"Judul: {self.__judul}, Penulis: {self.__penulis}, Tahun Terbit: {self.__tahun}"

# Kelas turunan untuk Ebook
class Ebook(Buku):
    def __init__(self, judul, penulis, tahun, ukuran_file):
        super().__init__(judul, penulis, tahun)
        self.__ukuran_file = ukuran_file

    def set_ukuran_file(self, ukuran_file):
        self.__ukuran_file = ukuran_file

    def informasi_ebook(self):
        return f"{self.informasi_buku()}, Ukuran File: {self.__ukuran_file} MB"

# Fungsi utama untuk menjalankan program
def main():
    # Membuat objek Buku
    buku = Buku("Buku OOP", "Budi", 2020)
    print(buku.informasi_buku())

    # Membuat objek Ebook
    ebook = Ebook("Ebook OOP", "Andi", 2021, 5)
    print(ebook.informasi_ebook())

    # Memperbarui informasi Ebook
    ebook.set_judul("Ebook OOP Terbaru")
    ebook.set_ukuran_file(10)
    print(ebook.informasi_ebook())

if __name__ == "__main__":
    main()
