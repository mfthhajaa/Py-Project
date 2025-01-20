import hashlib

# Simulasi database pengguna dan saldo
user_database = {
    "user1": {"password": hashlib.sha256("password123".encode()).hexdigest(), "saldo": 50000},
    "user2": {"password": hashlib.sha256("mypassword".encode()).hexdigest(), "saldo": 100000}
}

# Fungsi untuk hashing password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Fungsi login
def login():
    print("=== Login ===")
    username = input("Masukkan username: ")
    if username not in user_database:
        print("Username tidak ditemukan! Silakan registrasi terlebih dahulu.")
        return None
    
    password = input("Masukkan password: ")
    hashed_password = hash_password(password)
    
    if user_database[username]["password"] == hashed_password:
        print(f"Login berhasil! Selamat datang, {username}.")
        return username
    else:
        print("Password salah!")
        return None

# Fungsi untuk setor uang
def setor_tunai(username):
    print("\n=== Setor Uang ===")
    try:
        jumlah = float(input("Masukkan jumlah uang yang ingin disetor: Rp "))
        if jumlah <= 0:
            print("Jumlah setor harus lebih dari 0.")
            return
        user_database[username]["saldo"] += jumlah
        print(f"Berhasil setor Rp {jumlah}. Saldo saat ini: Rp {user_database[username]['saldo']}")
    except ValueError:
        print("Masukkan jumlah yang valid.")

# Fungsi untuk tarik tunai
def tarik_tunai(username):
    print("\n=== Tarik Tunai ===")
    try:
        jumlah = float(input("Masukkan jumlah uang yang ingin ditarik: Rp "))
        if jumlah <= 0:
            print("Jumlah tarik tunai harus lebih dari 0.")
            return
        if jumlah > user_database[username]["saldo"]:
            print("Saldo tidak cukup untuk melakukan penarikan.")
            return
        user_database[username]["saldo"] -= jumlah
        print(f"Berhasil tarik Rp {jumlah}. Saldo saat ini: Rp {user_database[username]['saldo']}")
    except ValueError:
        print("Masukkan jumlah yang valid.")

# Fungsi untuk cek saldo
def cek_saldo(username):
    print(f"\nSaldo Anda saat ini: Rp {user_database[username]['saldo']}")

# Fungsi utama
def main():
    while True:
        print("\n=== Sistem Bank ===")
        print("1. Login")
        print("2. Keluar")
        choice = input("Pilih opsi (1/2): ")

        if choice == "1":
            username = login()
            if username:
                while True:
                    print("\n=== Menu Bank ===")
                    print("1. Setor Uang")
                    print("2. Tarik Tunai")
                    print("3. Cek Saldo")
                    print("4. Logout")
                    menu_choice = input("Pilih opsi (1/2/3/4): ")

                    if menu_choice == "1":
                        setor_tunai(username)
                    elif menu_choice == "2":
                        tarik_tunai(username)
                    elif menu_choice == "3":
                        cek_saldo(username)
                    elif menu_choice == "4":
                        print("Logout berhasil! Sampai jumpa lagi.")
                        break
                    else:
                        print("Pilihan tidak valid! Coba lagi.")
        elif choice == "2":
            print("Terima kasih telah menggunakan sistem bank kami!")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    main()
