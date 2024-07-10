class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f'"{item}" ditambahkan ke dalam stack.')

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            print(f'"{item}" dihapus dari stack.')
            return item
        else:
            print("Stack kosong, tidak ada yang bisa dihapus.")
            return None

    def peek(self):
        if self.stack:
            print(f'Item di puncak stack: "{self.stack[-1]}"')
            return self.stack[-1]
        else:
            print("Stack kosong.")
            return None

    def is_empty(self):
        return not self.stack

def main():
    stack = Stack()
    pilihan_map = {
        '1': ("Masukkan item yang akan ditambahkan ke dalam stack: ", stack.push),
        '2': (None, stack.pop),
        '3': (None, stack.peek),
        '4': (None, lambda: print("Stack kosong." if stack.is_empty() else "Stack tidak kosong.")),
        '5': (None, exit)
    }

    while True:
        print("\nPilihan:")
        for i in range(1, 6):
            print(f"{i}. {pilihan_map[str(i)][0] if pilihan_map[str(i)][0] else ''}{['Push', 'Pop', 'Peek/Top', 'isEmpty', 'Keluar'][i-1]}")
        
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
        
        if pilihan in pilihan_map:
            arg, func = pilihan_map[pilihan]
            if arg:
                func(input(arg))
            else:
                func()
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")

if __name__ == "__main__":
    main()
