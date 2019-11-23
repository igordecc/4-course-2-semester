"""
task 3 of computer security lessons
"""

def xor_string(string:bytes, key:bytes) -> bytes:
    i = 0
    new_string = []
    for sb in string:
        kb = key[i]
        new_string.append(bytes([sb ^ kb]))
        if i < key.__len__() - 1:
            i += 1
        else:
            i = 0
    new_string = b"".join(new_string)
    return new_string


def xor_file2(input_path:str, output_path:str, key:str):
    with open(input_path, "rb") as file:
        file_string = file.read()   # in bytes! because "rb"
        new_file_string = xor_string(file_string, key.encode("utf-8"))
    with open(output_path, "wb") as file:
        file.write(new_file_string)


# TEST xor_string("encode string".encode("utf-8"),"key".encode("utf-8"))
# TEST xor_string # string = xor_string(xor_string("encode string".encode("utf-8"),"key".encode("utf-8")), "key".encode("utf-8"))

if __name__ == '__main__':
    # xor_file2("Ca-VhyIs3uU.jpg", "Ca-VhyIs3uU1.jpg", "give me your image")
    # xor_file2("Ca-VhyIs3uU1.jpg", "Ca-VhyIs3uU2.jpg", "give me your image")

    xor_file2("1.txt", "1.txtcoded", "равыл")
    xor_file2("1.txtcoded", "1.txtcodedcoded", "дайте картинку")