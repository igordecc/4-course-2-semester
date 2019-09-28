"""
task 3 of computer security lessons
"""

import os
import sys

filename = "Ca-VhyIs3uU.jpg"

# with open(filename, "rb") as file:
#     print(format(file))

file = open(filename, "rb")
key = "привет всем"


def xor_file(file, key):
    newfile = ""
    listed_key = [char for char in key]     # make list key from string key
    for string in file:
        for byte in string:
            char = listed_key.pop(0)    # use char from key (like from "keykeykeykey.." string)
            listed_key.append(char)     # but doesnt change the key sequence in general
            print(bin(byte), "\n")
            print(byte, "\n")
            binary_number = bin(int(byte)) # byte to bin

            # newfile += bin(bit)^bin(char)
    return newfile

xor_file(file, key)

file.close()
