
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
} #variaabel global

user = {"Attol": {'password': 'adminGanteng67', 'role': 'admin'}}#variaabel global
userLogin = None #variaabel global
keranjang = [] #variabel global

def tampilkan_produk():
    tabel = []
    no = 1
    for ID, item in produk.items():
        status = "Ready" if item['stok'] > 0 else "Not Ready"
        tabel.append([no, ID, item['Diecast'], item['stok'], status, f"Rp{item['Harga']:,}"])
        no += 1
    print(tabulate(tabel, headers=["No", "ID", "Nama", "Stok", "Status", "Harga"], tablefmt="grid"))


def menu_admin():
    while True:
        pilihan = select(
            message="=== Menu Admin ===",
            choices=["Lihat Produk", "Tambah Produk", "Update Stok", "Hapus Produk", "Keluar"]
        ).value

        if pilihan == "Lihat Produk":
            tampilkan_produk()
        elif pilihan == "Tambah Produk":
            nama = text(message="Nama produk:").value
            stok = int(text(message="Stok:").value)
            harga = int(text(message="Harga:").value)
            IDbaru = max(produk.keys()) + 1
            produk[IDbaru] = {'Diecast': nama, 'stok': stok, 'Harga': harga}
            print("Produk berhasil ditambahkan.")
        elif pilihan == "Update Stok":
            tampilkan_produk()
            ID = int(text(message="ID produk:").value)
            if ID in produk:
                jumlah = int(text(message="Jumlah stok baru:").value)
                produk[ID]['stok'] = jumlah
                print("Stok berhasil diupdate.")
            else:
                print("ID tidak ditemukan.")
        elif pilihan == "Hapus Produk":
            tampilkan_produk()
            ID = int(text(message="ID produk yang ingin dihapus:").value)
            if ID in produk:
                produk.pop(ID)
                print("Produk dihapus.")
            else:
                print("ID tidak ditemukan.")
        elif pilihan == "Keluar":
            break

def menu_pembeli():
    while True:
        pilihan = select(
            message="=== Menu Pembeli ===",
            choices=["Lihat Produk", "Tambah ke Keranjang", "Lihat Keranjang", "Edit Jumlah di Keranjang", "Hapus dari Keranjang", "Checkout", "Keluar"]
        ).value

        if pilihan == "Lihat Produk":
            tampilkan_produk()
        elif pilihan == "Tambah ke Keranjang":
            tampilkan_produk()
            ID = int(text(message="ID produk:").value)
            if ID not in produk or produk[ID]['stok'] == 0:
                print("Produk tidak tersedia.")
                continue
            jumlah = int(text(message="Jumlah beli:").value)
            if jumlah > produk[ID]['stok']:
                print("Stok tidak cukup.")
                continue
            keranjang.append({'ID': ID, 'Nama': produk[ID]['Diecast'], 'Jumlah': jumlah, 'Harga': produk[ID]['Harga']})
            print("Produk ditambahkan ke keranjang.")
        elif pilihan == "Lihat Keranjang":
            if not keranjang:
                print("Keranjang kosong.")
            else:
                tabel = []
                no = 1
                for item in keranjang:
                    total = item['Jumlah'] * item['Harga']
                    tabel.append([no, item['ID'], item['Nama'], item['Jumlah'], f"Rp{total:,}"])
                    no += 1
                print(tabulate(tabel, headers=["No", "ID", "Nama", "Jumlah", "Total"], tablefmt="grid"))
        elif pilihan == "Edit Jumlah di Keranjang":
            if not keranjang:
                print("Keranjang kosong.")
            else:
                tabel = []
                no = 1
                for item in keranjang:
                    total = item['Jumlah'] * item['Harga']
                    tabel.append([no, item['ID'], item['Nama'], item['Jumlah'], f"Rp{total:,}"])
                    no += 1
                print(tabulate(tabel, headers=["No", "ID", "Nama", "Jumlah", "Total"], tablefmt="grid"))
                nomor = int(text(message="Nomor produk di keranjang yang ingin diubah:").value)
                if 1 <= nomor <= len(keranjang):
                    new_jumlah = int(text(message="Jumlah baru:").value)
                    if new_jumlah <= produk[keranjang[nomor-1]['ID']]['stok']:
                        keranjang[nomor-1]['Jumlah'] = new_jumlah
                        print("Jumlah berhasil diubah.")
                    else:
                        print("Stok tidak cukup.")
                else:
                    print("Nomor tidak valid.")
        elif pilihan == "Hapus dari Keranjang":
            if not keranjang:
                print("Keranjang kosong.")
            else:
                nomor = int(text(message="Nomor produk di keranjang yang ingin dihapus:").value)
                if 1 <= nomor <= len(keranjang):
                    keranjang.pop(nomor-1)
                    print("Produk dihapus dari keranjang.")
                else:
                    print("Nomor tidak valid.")
        elif pilihan == "Checkout":
            if not keranjang:
                print("Keranjang kosong.")
            else:
                total_bayar = sum(item['Jumlah'] * item['Harga'] for item in keranjang)
                print(f"Total pembayaran: Rp{total_bayar:,}")
                konfirmasi = confirm(message="Lanjutkan pembayaran?").value
                if konfirmasi:
                    for item in keranjang:
                        produk[item['ID']]['stok'] -= item['Jumlah']
                    keranjang.clear()
                    print("Checkout berhasil. Terima kasih!")
                else:
                    print("Checkout dibatalkan.")
        elif pilihan == "Keluar":
            break


def registrasi():
    username = text(message="Masukkan Nama Anda:").value.strip()
    if username in user:
        print("Username sudah tersedia.")
        return
    password = text(message="Masukkan Password:").value.strip()
    role = select(message="Masuk sebagai:", choices=["admin", "pembeli"]).value
    user[username] = {'password': password, 'role': role}
    print("Registrasi berhasil.")

def login():
    global userLogin
    username = text(message="Username:").value.strip()
    password = text(message="Password:").value.strip()
    if username not in user or user[username]['password'] != password:
        print("Username atau password salah.")
        return
    userLogin = {'username': username, 'role': user[username]['role']}
    print(f"Login berhasil sebagai {userLogin['role']}")
    if userLogin['role'] == 'admin':
        menu_admin()
    else:
        menu_pembeli()


print("Selamat datang di Le Mans Diecast Indonesia")

while True:
    pilihan = select(
        message="=== Menu Awal ===",
        choices=["Registrasi", "Login", "Keluar"]
    ).value

    if pilihan == "Registrasi":
        registrasi()
    elif pilihan == "Login":
        login()
    elif pilihan == "Keluar":
        print("Terima kasih telah menggunakan layanan kami.")
        break

