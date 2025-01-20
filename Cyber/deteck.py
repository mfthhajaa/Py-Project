import cv2

# Muat pre-trained Haar Cascade classifier untuk deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Menggunakan kamera untuk mendeteksi wajah
def detect_face():
    # Mengakses kamera
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Mengubah gambar menjadi grayscale (lebih cepat untuk deteksi)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Deteksi wajah pada gambar grayscale
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        # Gambar persegi panjang di sekitar wajah yang terdeteksi
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Warna biru, ketebalan 2px
        
        # Menampilkan gambar dengan wajah yang terdeteksi
        cv2.imshow("Deteksi Wajah", frame)
        
        # Menunggu input untuk keluar (tekan 'q' untuk keluar)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Menutup kamera dan window
    cap.release()
    cv2.destroyAllWindows()

# Fungsi utama
def main():
    print("Deteksi wajah dimulai... Tekan 'q' untuk keluar.")
    detect_face()

if __name__ == "__main__":
    main()
