import hashlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk hashing password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Database sederhana untuk menyimpan username dan password (hashed)
user_database = {}

# Fungsi untuk registrasi pengguna baru
def register():
    print("=== Registrasi Pengguna Baru ===")
    username = input("Masukkan username: ")
    if username in user_database:
        print("Username sudah terdaftar! Silakan gunakan username lain.")
        return
    password = input("Masukkan password: ")
    hashed_password = hash_password(password)
    user_database[username] = hashed_password
    print("Registrasi berhasil!")

# Fungsi untuk login
def login():
    print("=== Login ===")
    username = input("Masukkan username: ")
    if username not in user_database:
        print("Username tidak ditemukan! Silakan registrasi terlebih dahulu.")
        return False
    password = input("Masukkan password: ")
    hashed_password = hash_password(password)
    if user_database[username] == hashed_password:
        print("Login berhasil! Selamat datang,", username)
        return True
    else:
        print("Password salah!")
        return False

# Fungsi untuk analisis deskriptif
def descriptive_analysis(data):
    print("\nStatistik Deskriptif:")
    print(data.describe())

# Fungsi untuk analisis visualisasi
def data_visualization(data):
    print("\nMembuka visualisasi data...")
    sns.pairplot(data)
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Heatmap Korelasi")
    plt.show()

# Fungsi untuk analisis korelasi
def correlation_analysis(data):
    print("\nMenganalisis Korelasi Antar Variabel:")
    correlation = data.corr()
    print(correlation)

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Heatmap Korelasi")
    plt.show()

# Fungsi untuk pilihan analisis data
def data_analysis():
    print("\n=== Pilihan Analisis Data ===")
    print("1. Analisis Deskriptif")
    print("2. Visualisasi Data")
    print("3. Analisis Korelasi")
    choice = input("Pilih opsi (1/2/3): ")

    # Menggunakan dataset bawaan Seaborn: tips
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    data = pd.read_csv(url)

    if choice == "1":
        descriptive_analysis(data)
    elif choice == "2":
        data_visualization(data)
    elif choice == "3":
        correlation_analysis(data)
    else:
        print("Pilihan tidak valid! Kembali ke menu utama.")

# Fungsi utama
def main():
    while True:
        print("\n=== Sistem Login dan Analisis Data ===")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                # Jika login berhasil, akses analisis data
                data_analysis()
        elif choice == "3":
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    main()
