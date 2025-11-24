from dat import produk
from tabulate import tabulate

def tampilkan_produk():
    tabel = []
    for ID, item in produk.items():
        status = "Ready" if item['stok'] > 0 else "Not Ready"
        tabel.append([ID, item['Diecast'], item['stok'], status, f"Rp{item['Harga']:,}"])
    print(tabulate(tabel, headers=["ID", "Nama", "Stok", "Status", "Harga"], tablefmt="grid"))

def menu_admin():
    while True:
        print("""
=== Menu Admin ===
1. Lihat Produk
2. Tambah Produk
3. Update Stok
4. Hapus Produk
5. Keluar
""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            tambah_produk()
        elif pilihan == "3":
            update_stok()
        elif pilihan == "4":
            hapus_produk()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

def tambah_produk():
    nama = input("Nama produk: ")
    stok = input("Stok: ")
    harga = input("Harga: ")
    if not stok.isdigit() or not harga.isdigit():
        print("Stok dan harga harus angka.")
        return
    IDbaru = max(produk.keys()) + 1
    produk[IDbaru] = {'Diecast': nama, 'stok': int(stok), 'Harga': int(harga)}
    print("Produk berhasil ditambahkan.")

def update_stok():
    tampilkan_produk()
    ID = input("ID produk: ")
    if not ID.isdigit() or int(ID) not in produk:
        print("ID tidak valid.")
        return
    ID = int(ID)
    aksi = input("Tambah/Kurangi: ").lower()
    jumlah = input("Jumlah: ")
    if not jumlah.isdigit():
        print("Jumlah harus angka.")
        return
    jumlah = int(jumlah)
    if aksi == "tambah":
        produk[ID]['stok'] += jumlah
    elif aksi == "kurangi":
        produk[ID]['stok'] = max(0, produk[ID]['stok'] - jumlah)
    else:
        print("Aksi tidak valid.")
        return
    print("Stok berhasil diupdate.")

def hapus_produk():
    tampilkan_produk()
    ID = input("ID produk yang ingin dihapus: ")
    if not ID.isdigit() or int(ID) not in produk:
        print("ID tidak valid.")
        return
    ID = int(ID)
    nama = produk[ID]['Diecast']
    konfirmasi = input(f"Yakin hapus {nama}? (ya/tidak): ").lower()
    if konfirmasi == "ya":
        produk.pop(ID)
        print("Produk dihapus.")
    else:
        print("Penghapusan dibatalkan.")

