import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.seconds = 0

        # Label untuk menampilkan waktu
        self.time_label = tk.Label(root, text="0:00", font=('Helvetica', 48), fg='green')
        self.time_label.pack(pady=50)

        # Tombol untuk mulai/menghentikan stopwatch
        self.start_button = tk.Button(root, text="Start", font=('Helvetica', 20), command=self.start_stop)
        self.start_button.pack(side='left', padx=10)

        # Tombol untuk reset stopwatch
        self.reset_button = tk.Button(root, text="Reset", font=('Helvetica', 20), command=self.reset)
        self.reset_button.pack(side='right', padx=10)

        # Update waktu setiap detik
        self.update_time()

    def start_stop(self):
        """Mulai atau hentikan stopwatch."""
        if self.running:
            self.running = False
            self.start_button.config(text="Start")
        else:
            self.running = True
            self.start_button.config(text="Stop")
            self.update_time()

    def reset(self):
        """Reset stopwatch ke 0."""
        self.running = False
        self.seconds = 0
        self.time_label.config(text="0:00")
        self.start_button.config(text="Start")

    def update_time(self):
        """Perbarui waktu setiap detik jika stopwatch berjalan."""
        if self.running:
            self.seconds += 1
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            self.time_label.config(text=f"{minutes}:{seconds:02d}")
            self.root.after(1000, self.update_time)  # Panggil update_time setiap 1 detik

# Membuat jendela utama
root = tk.Tk()
stopwatch = Stopwatch(root)

# Menjalankan aplikasi
root.mainloop()
