import cv2
import numpy as np

def detect_hand():
    # Mengakses kamera
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break

        # Mengubah gambar ke ruang warna HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Rentang warna kulit (HSV)
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)
        
        # Menerapkan mask untuk mendeteksi kulit
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
        # Menghaluskan mask untuk mengurangi noise
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        
        # Menampilkan hasil mask yang mendeteksi kulit
        res = cv2.bitwise_and(frame, frame, mask=mask)
        
        # Menampilkan gambar asli dan hasil deteksi tangan
        cv2.imshow("Original", frame)
        cv2.imshow("Detected Hand", res)
        
        # Menunggu input untuk keluar (tekan 'q' untuk keluar)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Menutup kamera dan window
    cap.release()
    cv2.destroyAllWindows()

# Fungsi utama
def main():
    print("Deteksi tangan dimulai... Tekan 'q' untuk keluar.")
    detect_hand()

if __name__ == "__main__":
    main()
