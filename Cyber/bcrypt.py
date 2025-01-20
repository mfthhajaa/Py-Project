import bcrypt

# Hashing kata sandi
password = "mypassword".encode()
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
print(f"Hashed Password: {hashed_password}")

# Verifikasi kata sandi
password_input = "mypassword".encode()
if bcrypt.checkpw(password_input, hashed_password):
    print("Password cocok!")
else:
    print("Password salah!")
