"""Main entry point for Project Insanity."""

import random
import sys
from tkinter import Tk, Button, Label, StringVar

ORACLES = [
    "You will meet yourself in a burning parking lot.",
    "Today is the day you forget everything important.",
    "Your keyboard is hungry. Feed it."
]


def launch_gui():
    """Launch a simple Tkinter GUI that reveals prophecies."""
    root = Tk()
    root.title("Project Insanity")

    message = StringVar()
    message.set("Invoke the oracle to receive a prophecy")

    label = Label(root, textvariable=message, width=50)
    label.pack(padx=10, pady=10)

    def reveal():
        message.set(random.choice(ORACLES))

    btn = Button(root, text="Invoke Oracle", command=reveal)
    btn.pack(pady=5)

    root.mainloop()

def run():
    """Open the mouth of madness."""
    if '--gui' in sys.argv:
        launch_gui()
    elif '--oracle' in sys.argv:
        print(random.choice(ORACLES))
    else:
        print("It is born. May god forgive us.")

if __name__ == "__main__":
    run()
