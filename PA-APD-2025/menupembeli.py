from dat import produk, keranjang, tampilkan_produk, tampilkan_keranjang, get_id_by_nomor

def pembeli_tambah_ke_keranjang():
    tampilkan_produk()
    try:
        nomor = int(input("Masukkan nomor produk: "))
        ID = get_id_by_nomor(nomor)
        if ID is None:
            print("Pilihan tidak valid.")
            return
        stok_tersedia = produk[ID]['stok']
        if stok_tersedia == 0:
            print("Produk tidak tersedia.")
            return
        jumlah = int(input("Jumlah beli: "))
        if jumlah <= 0 or jumlah > stok_tersedia:
            print("Jumlah tidak valid atau stok tidak cukup.")
            return
        produk[ID]['stok'] -= jumlah
        keranjang.append({'Nama': produk[ID]['Diecast'], 'Jumlah': jumlah, 'Harga': produk[ID]['Harga'], 'ID': ID})
        print("Produk berhasil ditambahkan ke keranjang.")
    except ValueError:
        print("Pilihan tidak valid.")

def pembeli_lihat_keranjang():
    tampilkan_keranjang(keranjang)

def pembeli_edit_jumlah_keranjang():
    tampilkan_keranjang(keranjang)
    try:
        nomor = int(input("Nomor item yang ingin diubah: "))
        if nomor < 1 or nomor > len(keranjang):
            print("Pilihan tidak valid.")
            return
        new_jumlah = int(input("Jumlah baru: "))
        if new_jumlah <= 0:
            print("Jumlah harus lebih dari 0.")
            return
        item = keranjang[nomor - 1]
        ID = item['ID']
        stok_tersedia = produk[ID]['stok'] + item['Jumlah']
        if new_jumlah > stok_tersedia:
            print("Stok tidak cukup.")
            return
        selisih = new_jumlah - item['Jumlah']
        produk[ID]['stok'] -= selisih
        item['Jumlah'] = new_jumlah
        print("Jumlah berhasil diubah.")
    except ValueError:
        print("Pilihan tidak valid.")

def pembeli_hapus_dari_keranjang():
    tampilkan_keranjang(keranjang)
    try:
        nomor = int(input("Nomor yang ingin dihapus: "))
        if nomor < 1 or nomor > len(keranjang):
            print("Pilihan tidak valid.")
            return
        item = keranjang.pop(nomor - 1)
        ID = item['ID']
        produk[ID]['stok'] += item['Jumlah']
        print("Produk dihapus dari keranjang.")
    except ValueError:
        print("Pilihan tidak valid.")
def menu_pembeli():
    while True:
        print("""
=== Menu Pembeli ===
1. Lihat Produk
2. Tambah ke Keranjang
3. Lihat Keranjang
4. Edit Jumlah di Keranjang
5. Hapus dari Keranjang
6. Checkout
7. Keluar
""")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            pembeli_tambah_ke_keranjang()
        elif pilihan == "3":
            pembeli_lihat_keranjang()
        elif pilihan == "4":
            pembeli_edit_jumlah_keranjang()
        elif pilihan == "5":
            pembeli_hapus_dari_keranjang()
        elif pilihan == "6":
            print("Checkout berhasil. Terima kasih telah berbelanja!")
            keranjang.clear()
        elif pilihan == "7":
            print("Keluar dari menu pembeli.")
            break
        else:
            print("Pilihan tidak valid.")
