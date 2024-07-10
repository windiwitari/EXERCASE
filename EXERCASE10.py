import pandas as pd

data = [
    [10,20,5],
    [30,10,7],
    [35,20,10],
    [8,7,9],
    [14,28,10],
    [10,20,5],
    [5,7,8,]
]

hari=['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
barang=['Barang A','Barang B','Barang C',]

df = pd.DataFrame(data, index=hari, columns=barang)
print(df)
print('\n')

print('Total penjualan untuk setiap produk selama seminggu')
total_penjualan_seminggu = df.sum()
print(total_penjualan_seminggu)
print('\n')

print('Total penjualan produk setiap hari (Senin - Minggu)')
total_penjualan_setiap_hari = df.sum(axis=1)
print(total_penjualan_setiap_hari)
print('\n')

print('Produk dengan penjualan terbanyak selama seminggu')
produk_terbanyak_seminggu = total_penjualan_seminggu.idxmax(axis=0)
print('\n')

print('Hari dengan penjualan tertinggi untuk setiap produk'.title)
hari_dengan_penjualan_tertinggi = total_penjualan_setiap_hari.idxmax()
print(hari_dengan_penjualan_tertinggi) 
print('\n')     


# print('Total penjualan untuk setiap produk selama seminggu')
# total_perbaris = df.sum(axis=0)
# total_perkolom = df.sum(axis=1)
# print(total_perbaris)
# print(total_perkolom)
# print('\n')

# print('Total penjualan produk setiap hari (Senin - Minggu)')
# index_tertinggi = df.idxmax() # nampilin index tertinggi berdasarkan baris dan kolom
# index_tertinggi_baris = df.idxmax(axis=1)
# print(index_tertinggi)
# print(index_tertinggi_baris)
# print('\n')

# print('Produk dengan penjualan terbanyak')

# index_tertinggi_perbaris = total_perbaris.idxmax() # 
# print(index_tertinggi_perbaris)

#=================================================

# import numpy as np
# import pandas as pd

# # Data penjualan produk dalam seminggu
# data_penjualan = np.array([
#     [10, 20, 5],  # Senin
#     [30, 10, 7],  # Selasa
#     [35, 20, 10],  # Rabu
#     [8, 7, 9],  # Kamis
#     [14, 28, 10],  # Jumat
#     [10, 20, 5],  # Sabtu
#     [5, 7, 8],  # Minggu
# ])


# # Buat DataFrame dari data penjualan
# produk = ['Produk A', 'Produk B', 'Produk C']
# hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
# df_penjualan = pd.DataFrame(data_penjualan, columns=produk, index=hari)

# # Hitung total penjualan untuk setiap produk selama seminggu
# total_penjualan_produk = df_penjualan.sum()

# # Hitung total penjualan setiap hari (Senin - Minggu)
# total_penjualan_hari = df_penjualan.sum(axis=1)

# # Temukan produk dengan penjualan terbanyak selama seminggu
# produk_terbanyak = total_penjualan_produk.idxmax()

# # Temukan hari dengan penjualan tertinggi untuk setiap produk
# hari_tertinggi_per_produk = df_penjualan.idxmax()

# print("Total penjualan untuk setiap produk selama seminggu:")
# print(total_penjualan_produk)
# print("\nTotal penjualan setiap hari (Senin - Minggu):")
# print(total_penjualan_hari)
# print("\nProduk dengan penjualan terbanyak selama seminggu:")
# print(produk_terbanyak)
# print("Temukan Hari dengan penjualan tertinggi untuk setiap produk:")
# print(hari_tertinggi_per_produk)
