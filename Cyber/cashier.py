import matplotlib.pyplot as plt

# Menu Makanan dan Minuman
menu_makanan = {
    "Nasi Goreng": 25000,
    "Mie Goreng": 20000,
    "Ayam Bakar": 30000,
    "Sate": 28000,
    "Bakso": 18000
}

menu_minuman = {
    "Teh Manis": 5000,
    "Es Jeruk": 7000,
    "Kopi": 10000,
    "Air Mineral": 3000,
    "Es Teh": 6000
}

# Fungsi untuk menampilkan menu
def display_menu():
    print("\n=== Menu Makanan ===")
    for makanan, harga in menu_makanan.items():
        print(f"{makanan}: Rp {harga}")

    print("\n=== Menu Minuman ===")
    for minuman, harga in menu_minuman.items():
        print(f"{minuman}: Rp {harga}")

# Fungsi untuk memilih makanan dan minuman serta menghitung total harga
def order_menu():
    print("\n=== Pemesanan Menu ===")
    display_menu()

    # Memilih Makanan
    makanan_choice = input("\nMasukkan nama makanan yang ingin dipesan: ")
    makanan_price = 0
    if makanan_choice in menu_makanan:
        makanan_price = menu_makanan[makanan_choice]
        print(f"Anda memilih {makanan_choice} dengan harga Rp {makanan_price}")
    else:
        print("Makanan tidak tersedia dalam menu!")

    # Memilih Minuman
    minuman_choice = input("\nMasukkan nama minuman yang ingin dipesan: ")
    minuman_price = 0
    if minuman_choice in menu_minuman:
        minuman_price = menu_minuman[minuman_choice]
        print(f"Anda memilih {minuman_choice} dengan harga Rp {minuman_price}")
    else:
        print("Minuman tidak tersedia dalam menu!")

    # Menghitung total harga
    total_price = makanan_price + minuman_price
    print(f"\nTotal harga pesanan: Rp {total_price}")

    # Menampilkan Visualisasi Data
    display_visualization(makanan_choice, minuman_choice, makanan_price, minuman_price, total_price)

# Fungsi untuk menampilkan visualisasi data
def display_visualization(makanan_choice, minuman_choice, makanan_price, minuman_price, total_price):
    # Membuat data untuk visualisasi
    items = [makanan_choice, minuman_choice]
    prices = [makanan_price, minuman_price]

    # Membuat grafik batang
    plt.figure(figsize=(8, 5))
    plt.bar(items, prices, color=['blue', 'green'])
    plt.xlabel('Item')
    plt.ylabel('Harga (Rp)')
    plt.title('Harga Makanan dan Minuman yang Dipesan')

    # Menambahkan total harga ke grafik
    plt.text(1, max(prices) + 2000, f'Total: Rp {total_price}', ha='center', color='black', fontsize=12)
    plt.show()

# Fungsi utama
def main():
    while True:
        print("\n=== Menu Restoran ===")
        print("1. Lihat Menu dan Pesan")
        print("2. Keluar")
        choice = input("Pilih opsi (1/2): ")
        if choice == "1":
            order_menu()
        elif choice == "2":
            print("Terima kasih telah mengunjungi restoran kami!")
            break
        else:
            print("Pilihan tidak valid! Coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    main()
