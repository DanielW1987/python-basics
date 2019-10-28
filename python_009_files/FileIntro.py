import os
import sys
from typing import TextIO

"""
File modes
r  = Open text file for reading.
     The stream is positioned at the beginning of the file.

r+ = Open for reading and writing.
     The stream is positioned at the beginning of the file.

w  = Truncate file to zero length or create text file for writing.
     The stream is positioned at the beginning of the file.
w+ = Open for reading and writing. The file is created if it does not exist, otherwise it is truncated.

     The stream is positioned at the beginning of the file.

a  = Open for writing. The file is created if it does not exist.
     The stream is positioned at the end of the file.
     Subsequent writes to the file will always end up at the then current end of file,
     irrespective of any intervening fseek(3) or similar.

a+ = Open for reading and writing. The file is created if it does not exist.
     The stream is positioned at the end of the file.
     Subsequent writes to the file will always end up at the then current
     end of file, irrespective of any intervening fseek(3) or similar.

x  = Open for exclusive creation, failing if the file already exists.
"""

# writing to a file
file1: TextIO = open("myfile.txt", "w")
text: str = "Lorem ipsum dolor..."
file1.write(text)
file1.close()

# reading from a file
file2: TextIO = open("myfile.txt", "r")
read_text: str = file2.read()
assert read_text == text
file2.close()

# check if file exists
if os.path.isfile("myfile.txt"):
    print("File exists")
else:
    print("File does not exist")
    sys.exit()
