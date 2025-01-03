import tkinter as tk
import time
import math

# Membuat jendela utama
root = tk.Tk()
root.title("Jam Analog")

# Membuat kanvas untuk menggambar jam
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Membuat fungsi untuk menggambar jam analog
def draw_clock():
    # Menghapus gambar lama
    canvas.delete("all")
    
    # Menggambar lingkaran jam
    canvas.create_oval(50, 50, 350, 350, width=4)
    
    # Menggambar angka jam
    for i in range(1, 13):
        angle = math.radians(360 * (i / 12))
        x = 200 + 140 * math.cos(angle)
        y = 200 - 140 * math.sin(angle)
        canvas.create_text(x, y, text=str(i), font=('Helvetica', 12, 'bold'))
    
    # Mendapatkan waktu saat ini
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Menghitung posisi jarum jam
    hour_angle = math.radians(360 * (hours / 12) - 90)
    minute_angle = math.radians(360 * (minutes / 60) - 90)
    second_angle = math.radians(360 * (seconds / 60) - 90)

    # Menggambar jarum jam
    canvas.create_line(200, 200, 200 + 60 * math.cos(hour_angle), 200 + 60 * math.sin(hour_angle), width=6, fill="black")
    
    # Menggambar jarum menit
    canvas.create_line(200, 200, 200 + 80 * math.cos(minute_angle), 200 + 80 * math.sin(minute_angle), width=4, fill="blue")
    
    # Menggambar jarum detik
    canvas.create_line(200, 200, 200 + 100 * math.cos(second_angle), 200 + 100 * math.sin(second_angle), width=2, fill="red")
    
    # Mengupdate jam setiap detik
    root.after(1000, draw_clock)

# Menjalankan fungsi menggambar jam
draw_clock()

# Menjalankan aplikasi
root.mainloop()
