import sys
import pyperclip


if len(sys.argv) <= 1:
    print(
        """
        Convert any character with a code higher than 127 to its
        unicode escaped literal, and put the converted text in the clipboard"""
    )
    exit()

filename = sys.argv[1]
with open(filename, encoding="utf-8") as original:
    text = original.read()

escaped_text = ""
for character in text:
    code = ord(character)
    if code > 127:
        escaped_text += "\\" + hex(code)[2:].zfill(6)
    else:
        escaped_text += chr(code)

pyperclip.copy(escaped_text)
print("The escaped text has been copied to the clipboard")
