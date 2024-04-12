from pynput.mouse import Controller
from pynput import keyboard

mousecontroller = Controller()

def on_release(key):
    if key == keyboard.Key.down:
        mousecontroller.scroll(0, -1)
    elif key == keyboard.Key.up:
        mousecontroller.scroll(0, 1)

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()