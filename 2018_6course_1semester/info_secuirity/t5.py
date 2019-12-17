"""
task 5 of computer security lessons
"""
SIMILAR_CHARS = [
        # // (En char, Cyr char)
        # // lowercase
        ('a', 'а'),
        ('c', 'с'),
        ('e', 'е'),
        ('o', 'о'),
        ('p', 'р'),
        ('y', 'у'),
        # // uppercase
        ('A', 'А'),
        ('B', 'В'),
        ('C', 'С'),
        ('E', 'Е'),
        ('H', 'Н'),
        ('K', 'К'),
        ('M', 'М'),
        ('O', 'О'),
        ('P', 'Р'),
        ('T', 'Т'),
        ('X', 'Х'),
    ]


# TODO fist stage - main functions
# message to bytes to bits
# encrypt text with message

# decrypt text, output message in bits
# decrypt bits - bytes - message

# TODO second stage - additions
# prepare text (make shure that all letters in the same language)


def iterate_bits(message: bytes):
    """
     Transform bytes string to bits

    ``iterate_bits(message_text.encode("utf-8"))``

    :param message: string of bytes
    :return: boolean on each iteration
    """
    for byte in message:
        for bit in "{:08b}".format(byte):
            yield bit == "1"

def check_text(text, flag):
    """
    check text and change all wrong chars to same language
    :param text:
    :param flag:
    :return:
    """
    if flag == "ru->en":
        char_map = dict(SIMILAR_CHARS)
        new_text_list = [char_map[char] if (char in char_map.keys()) else char for char in text]
        new_text = "".join(new_text_list)

        return new_text

    elif flag == "en->ru":
        char_map = [(y,x) for x,y in SIMILAR_CHARS]
        char_map = dict(char_map)
        new_text_list = [char_map[char] if (char in char_map.keys()) else char for char in text]
        new_text = "".join(new_text_list)

        return new_text

    raise RuntimeError("flag error")




def encrypt(text:str, encrypt_type:str, message:bytes):
    """
     Encrypt text with message
    :return: encrypted text
    """
    char_map = SIMILAR_CHARS

    if encrypt_type == "ru->en":
        char_map = [(y,x) for x,y in char_map]
        char_map = dict(char_map)
    elif encrypt_type == "en->ru":
        char_map = dict(char_map)

    message = [bit for bit in iterate_bits(message)]

    new_text = []
    for char in text:
        if (char in char_map.keys()) and message:
            encrypt_char = message.pop(0)
            if encrypt_char:
                new_text.append(char_map[char])
            else:
                new_text.append(char)
        else:
            new_text.append(char)

    if message:
        raise RuntimeError("text is too short")

    return "".join(new_text)


def boole_list_to_bytes(bit_message:list):
    """
    message in bits transform to bytes
    :return: byte string
    """
    b_number = 0
    byte_list = []
    one_cool_byte = 0
    for item in bit_message:
        one_cool_byte <<= 1
        if item:
            one_cool_byte += 1
        b_number += 1
        if b_number == 8:
            byte_list.append(one_cool_byte)
            b_number = 0
            one_cool_byte = 0
    return bytes(byte_list).rstrip(b"\x00")     # return byte string


def decrypt(text, encrypt_type:str):
    char_map = SIMILAR_CHARS
    if encrypt_type == "ru->en":
        char_map = [(y, x) for x, y in char_map]
        char_map = dict(char_map)
    elif encrypt_type == "en->ru":
        char_map = dict(char_map)

    message = []
    for char in text:
        if char in char_map.values() or char in char_map.keys():
            if char in char_map.values():
                message.append(True)
            else:
                message.append(False)

    message = boole_list_to_bytes(message)
    return message


if __name__ == '__main__':
    message = "hello"
    # encrypt
    with open("text_carrier.txt", "r") as file:

        file_text = file.read()
        flag = "ru->en"
        checked_file_text = check_text(file_text, flag)

        result = encrypt(checked_file_text, flag, message.encode("utf-8"))

        with open("encrypted_text.txt", "w") as new_file:
            new_file.write(result)

    # decrypt
    with open("encrypted_text.txt", "r") as file:
        file_text = file.read()

        result = decrypt(file_text, "ru->en")
        with open("new_text_carrier.txt", "w") as new_file:
            new_file.write(result.decode("utf-8"))