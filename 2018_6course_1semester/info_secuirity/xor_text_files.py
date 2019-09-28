"""
task 3 of computer security lessons
text only
"""

def key_polisher(key:str):
    new_key = ""
    for char in key:
        char_id = int(ord(char))
        while char_id > 255:
            char_id -= 256
        new_key += chr(char_id)
    return new_key


def xor_file_for_txt(file, key):
    listed_key = [char for char in key]     # make list key from string key
    for string in file:
        newfile_string = b""
        for strings_byte in string:
            char = listed_key.pop(0)    # use char from key (like from "keykeykeykey.." string)
            listed_key.append(char)     # but doesnt change the key sequence in general

            # bin(byte)^bin(int(ord(char)))
            char_id = int(ord(char))
            newfile_string += bytes( [strings_byte ^ char_id] ) # XOR byte from image string and char
        write_file.write(newfile_string)


if __name__ == '__main__':
    # filename = "Ca-VhyIs3uU1.jpgcoded"    # doesnt wark
    # filename = "1.txt"
    filename = "1.txtcoded"

    file = open(filename, "rb")
    key = "привет всем"

    key = key_polisher(key)
    write_file = open(filename + "coded", "wb")

    xor_file_for_txt(file, key)

    file.close()
    write_file.close()