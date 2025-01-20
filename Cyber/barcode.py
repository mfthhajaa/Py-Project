import cv2
from pyzbar.pyzbar import decode

# Simulasi database produk dengan harga berdasarkan barcode
produk_database = {
    "123456789012": {"nama": "Produk A", "harga": 10000},
    "987654321098": {"nama": "Produk B", "harga": 20000},
    "555": {"nama": "Produk C", "harga": 15000},
}

# Fungsi untuk memindai barcode menggunakan kamera
def scan_barcode():
    # Menggunakan kamera default (biasanya kamera laptop)
    cap = cv2.VideoCapture(0)
    total_harga = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Mendekode barcode yang ada dalam frame
        barcodes = decode(frame)
        
        for barcode in barcodes:
            # Mendekode data dari barcode
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type
            
            # Menampilkan informasi barcode pada gambar
            rect_points = barcode.polygon
            if len(rect_points) == 4:
                pts = rect_points
            else:
                pts = cv2.convexHull(np.array([point for point in rect_points], dtype=np.int32))
            cv2.polylines(frame, [pts], True, (0, 0, 255), 2)
            
            # Menambahkan informasi produk ke total harga
            if barcode_data in produk_database:
                produk = produk_database[barcode_data]
                print(f"Produk ditemukan: {produk['nama']} - Rp {produk['harga']}")
                total_harga += produk['harga']
        
        # Menampilkan gambar dengan barcode yang terdeteksi
        cv2.imshow("Scan Barcode", frame)
        
        # Menunggu input dari keyboard untuk keluar (tekan 'q' untuk keluar)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Menampilkan total harga
    print(f"\nTotal Harga Transaksi: Rp {total_harga}")
    
    # Menutup kamera dan window
    cap.release()
    cv2.destroyAllWindows()

# Fungsi utama
def main():
    print("=== Aplikasi Kasir dengan Scan Barcode ===")
    scan_barcode()

# Jalankan program utama
if __name__ == "__main__":
    main()
