# /// script
# requires-python = ">=3.11"
# dependencies = [
#    "screeninfo",
# ]
# ///

from screeninfo import get_monitors

for m in get_monitors():
    print(f"Monitor: {m.name}, Width: {m.width}, Height: {m.height}, x={m.x}, y={m.y}")