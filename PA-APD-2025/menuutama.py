from auth import registrasi, login

def menu_utama():
    print("Selamat datang di Le Mans Diecast Indonesia")
    while True:
        print("""
=== Menu Utama ===
1. Registrasi
2. Login
3. Keluar
""")
        opsi = input("Pilih menu: ").strip()
        if opsi == "1":
            registrasi()
        elif opsi == "2":
            login()
        elif opsi == "3":
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid.")
