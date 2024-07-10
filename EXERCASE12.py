from collections import deque

class AntrianBank:
    def __init__(self):
        self.antrian = deque()

    def tambah_antrian(self, nama_pelanggan):
        self.antrian.append(nama_pelanggan)
        print(f'Masukan Nama Pelanggan : {nama_pelanggan}')
        print(f'"{nama_pelanggan}" Berhasil ditambahkan ke antrian')

    def antrian_selanjutnya(self):
        if self.antrian:
            pelanggan_selanjutnya = self.antrian.popleft()
            print(f'Pelanggan "{pelanggan_selanjutnya}" sedang dilayani.')
        else:
            print("Tidak ada pelanggan dalam antrian.")

    def lihat_antrian(self):
        if self.antrian:
            print("Daftar antrian saat ini:", list(self.antrian))
        else:
            print("Tidak ada pelanggan dalam antrian.")

    def lihat_pelanggan_di_depan(self):
        if self.antrian:
            print(f'Pelanggan di depan antrian: "{self.antrian[0]}"')
        else:
            print("Tidak ada pelanggan dalam antrian.")

    def status_antrian(self):
        if self.antrian:
            pelanggan_sedang_dilayani = self.antrian[0]
            pelanggan_selanjutnya = self.antrian[1] if len(self.antrian) > 1 else "Tidak ada"
            jumlah_antrian = len(self.antrian)
            print(f'\nAntrian Sekarang : Pelanggan "{pelanggan_sedang_dilayani}" Sedang di CS')
            print(f'Antrian Selanjutnya : Pelanggan "{pelanggan_selanjutnya}"')
            print(f'Jumlah Antrian : {jumlah_antrian}')
        else:
            print("\nTidak ada pelanggan dalam antrian.")


# Fungsi utama untuk menjalankan program
def utama():
    antrian_bank = AntrianBank()
    
    while True:
        antrian_bank.status_antrian()
        print("Pilihan:")
        print("1. Tambah Antrian")
        print("2. Antrian Selanjutnya")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == '1':
            nama_pelanggan = input("Masukkan Nama Pelanggan: ")
            antrian_bank.tambah_antrian(nama_pelanggan)
        elif pilihan == '2':
            antrian_bank.antrian_selanjutnya()
        elif pilihan == '3':
            antrian_bank.lihat_antrian()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
        print("="*30)

if __name__ == "__main__":
    utama()
