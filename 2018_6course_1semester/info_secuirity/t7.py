"""
task 7 of computer security lessons
"""

# TODO
# bytes from file

# return match files
    # iterate over directories
    # search bytes in files

## take file (or some bytes from file)
## recursive iteration over directories
## check bytes and file, is it the same and add to files list

import sys
import os

def take_n_bytes(file_name:str, n_bytes:int) -> bytes:
    with open(file_name, "rb") as file:
        return file.read()[:n_bytes]


def find_files(file_bytes, start_dir):
    found_paths = []
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if search_bytes_in_files(file_bytes, file_path):
                found_paths.append(file_path)
    return found_paths


def search_bytes_in_files(bytes_to_find:bytes, file_path):
    with open(file_path, "rb") as file:
       file_string = file.read()
    return file_string.find(bytes_to_find) != -1

if __name__ == '__main__':
    file_path = "./1.txt"
    file_bytes = take_n_bytes(file_path, 16)
    print(file_bytes)
    files = find_files(file_bytes, "./")
    print(files)


