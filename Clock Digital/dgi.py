import tkinter as tk
import time

# Membuat jendela utama
root = tk.Tk()
root.title("Jam LED Digital")

# Mengatur ukuran dan background jendela
root.geometry("400x200")
root.configure(bg='black')

# Fungsi untuk memperbarui waktu
def update_time():
    # Mendapatkan waktu saat ini
    current_time = time.strftime("%H:%M:%S")
    
    # Menampilkan waktu di label
    time_label.config(text=current_time)
    
    # Memperbarui waktu setiap 1000 ms (1 detik)
    root.after(1000, update_time)

# Membuat label untuk menampilkan waktu
time_label = tk.Label(root, font=('Helvetica', 48, 'bold'), fg='Green', bg='black')
time_label.pack(pady=50)

# Menjalankan fungsi untuk memperbarui waktu
update_time()

# Menjalankan aplikasi
root.mainloop()
