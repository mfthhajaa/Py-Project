import time

# Threshold percobaan login
MAX_ATTEMPTS = 3
LOCKOUT_TIME = 10  # detik

login_attempts = 0
locked_until = None

while True:
    if locked_until and time.time() < locked_until:
        print(f"Akun terkunci! Tunggu {int(locked_until - time.time())} detik.")
        time.sleep(1)
        continue

    password = input("Masukkan password: ")
    if password == "csfgw712":
        print("Login berhasil!")
        break
    else:
        print("Password salah!")
        login_attempts += 1

        if login_attempts >= MAX_ATTEMPTS:
            print("Terlalu banyak percobaan! Akun terkunci.")
            locked_until = time.time() + LOCKOUT_TIME
            login_attempts = 0
