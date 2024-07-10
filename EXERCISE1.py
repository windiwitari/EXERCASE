def pencarian(history_stack, kunci):
    history_stack.append(kunci)
    print(f'{kunci} ditambahkan ke riwayat pencarian')

def hapus_history(history_stack, delete_stack):
    if history_stack:
        last_stack = history_stack.pop()
        delete_stack.append(last_stack)
        print(f'"{last_stack}" dihapus dari riwayat pencarian.')
    else:
        print('Tidak ada pencarian untuk dihapus.')

def undo(history_stack, deleted_stack):
    if deleted_stack:
        last_deleted = deleted_stack.pop()
        history_stack.append(last_deleted)
        print(f'"{last_deleted}" dikembalikan ke riwayat pencarian.')
    else:
        print('Tidak ada operasi yang bisa di-undo.')