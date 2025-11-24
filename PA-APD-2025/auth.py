from dat import user, userLogin
from menuadmin import menu_admin
from menupembeli import menu_pembeli

def registrasi():
    try:
        username = input("Masukkan Nama Anda: ").strip()
        if not username:
            raise ValueError("Nama tidak boleh kosong!")
        if not username.isalnum():
            raise ValueError("Nama hanya boleh huruf dan angka, tidak boleh simbol!")
        if username in user:
            raise KeyError("Username sudah tersedia.")

        password = input("Masukkan Password: ").strip()
        if not password:
            raise ValueError("Password tidak boleh kosong!")

        role = input("Masuk sebagai (Admin/Pembeli): ").strip().lower()
        if role not in ['admin', 'pembeli']:
            raise ValueError("Role tidak valid.")

        user[username] = {'password': password, 'role': role}
        print("Registrasi berhasil.")

    except (ValueError, KeyError) as e:
        print("Error:", e)

def login():
    global userLogin
    try:
        username = input("Username: ").strip()
        if not username:
            raise ValueError("Username tidak boleh kosong!")
        if not username.isalnum():
            raise ValueError("Username hanya boleh huruf dan angka, tidak boleh simbol!")

        password = input("Password: ").strip()
        if not password:
            raise ValueError("Password tidak boleh kosong!")

        if username not in user:
            raise KeyError("Username tidak ditemukan.")
        if user[username]['password'] != password:
            raise ValueError("Password salah.")

        userLogin = {'username': username, 'role': user[username]['role']}
        print(f"Login berhasil sebagai {userLogin['role']}")

        if userLogin['role'] == 'admin':
            menu_admin()
        else:
            menu_pembeli()

    except (ValueError, KeyError) as e:
        print("Error:", e)

