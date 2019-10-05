"""
task 6 of computer security lessons
"""

import hashlib

def checksum(file_path):
    with open(file_path, "rb") as file:
        return hashlib.md5(file.read()).hexdigest()

print(checksum("1.txt"))