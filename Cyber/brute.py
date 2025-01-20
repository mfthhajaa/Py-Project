# Contoh simulasi pencocokan password brute force
import itertools

# Daftar karakter dan target password
characters = "User.1783945003"
target_password = "******"

print("Starting brute force attack...")
for attempt in itertools.product(characters, repeat=len(target_password)):
    attempt_password = ''.join(attempt)
    print(f"Trying: {attempt_password}")
    if attempt_password == target_password:
        print(f"Password ditemukan: {attempt_password}")
        break
