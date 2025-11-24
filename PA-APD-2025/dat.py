from tabulate import tabulate

produk = {
    1: {'Diecast': 'Ferrari 499p', 'stok': 2, 'Harga': 330000},
    2: {'Diecast': 'Porsche 963 LMDh', 'stok': 0, 'Harga': 400000},
    3: {'Diecast': 'Ferrari SF-24', 'stok': 0, 'Harga': 140000},
    4: {'Diecast': 'Porsche 911 GT3', 'stok': 5, 'Harga': 100000},
    5: {'Diecast': 'BMW M4 GT3', 'stok': 0, 'Harga': 150000},
    6: {'Diecast': 'BMW M V8 Hybrid', 'stok': 1, 'Harga': 300000},
    7: {'Diecast': 'Mercedes AMG Petronas F1', 'stok': 0, 'Harga': 140000},
    8: {'Diecast': 'McLaren F1', 'stok': 3, 'Harga': 140000},
    9: {'Diecast': 'Lotus 67', 'stok': 0, 'Harga': 40000},
    10: {'Diecast': 'Peugeot 9x8', 'stok': 6, 'Harga': 190000},
    11: {'Diecast': 'Cadillac V-Series R V8', 'stok': 0, 'Harga': 50000}
}

user = {"Attol": {'password': 'adminGanteng67', 'role': 'admin'}}
userLogin = None
keranjang = []

def tampilkan_produk():
    tabel = []
    for no, (_, item) in enumerate(produk.items(), start=1):
        status = "Ready" if item['stok'] > 0 else "Not Ready"
        tabel.append([no, item['Diecast'], item['stok'], status, f"Rp{item['Harga']:,}"])
    print(tabulate(tabel, headers=["No", "Nama", "Stok", "Status", "Harga"], tablefmt="grid"))

def get_id_by_nomor(nomor):
    if nomor < 1 or nomor > len(produk):
        return None
    return list(produk.keys())[nomor - 1]

def tampilkan_keranjang(keranjang):
    if not keranjang:
        print("Keranjang kosong.")
        return
    tabel = []
    for no, item in enumerate(keranjang, start=1):
        total = item['Jumlah'] * item['Harga']
        tabel.append([no, item['Nama'], item['Jumlah'], f"Rp{total:,}"])
    print(tabulate(tabel, headers=["No", "Nama", "Jumlah", "Total"], tablefmt="grid"))

