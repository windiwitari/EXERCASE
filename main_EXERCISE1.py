import EXERCISE1 as ls

history_stack = []
delete_stack = []

def show_menu():
    while True:
        print('==='*12)
        print("\nRiwayat pencarian saat ini:", history_stack)
        print('==='*12)
        print("Pilihan:")
        print("1. Tambah pencarian")
        print("2. Hapus pencarian terakhir")
        print("3. Undo")
        print("4. Keluar")
        print('==='*12)

        pilihan = input("Pilih operasi (1/2/3/4): ")

        if pilihan == '1':
            kunci = input("Masukkan data: ")
            ls.pencarian(history_stack, kunci)
        elif pilihan == '2':
            ls.hapus_history(history_stack, delete_stack)
        elif pilihan == '3':
            ls.undo(history_stack, delete_stack)
        elif pilihan == '4':
            break
        else:
            print('==='*12)
            print('Hey, data tidak valid bro!')
show_menu()