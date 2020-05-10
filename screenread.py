import keyboard
from subprocess import run
from threading import Thread

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

def get_clipboard():
    root = tk.Tk()
    root.withdraw()
    clip = root.clipboard_get()
    return clip


def on_say():
    clip = get_clipboard()
    run(["say", clip])


def main():
    print("Select any text. Press Control + c and Control + 1 ")
    listen = Thread(target=add_listen())
    listen.start()


def add_listen():
    keyboard.add_hotkey("ctrl+1", on_say)
    keyboard.wait("shift+esc")


if __name__ == "__main__":
    main()
