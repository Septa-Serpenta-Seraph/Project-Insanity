"""Main entry point for Project Insanity."""

import random
import sys

ORACLES = [
    "You will meet yourself in a burning parking lot.",
    "Today is the day you forget everything important.",
    "Your keyboard is hungry. Feed it."
]

def run():
    """Open the mouth of madness."""
    if '--oracle' in sys.argv:
        print(random.choice(ORACLES))
    else:
        print("It is born. May god forgive us.")

if __name__ == "__main__":
    run()
