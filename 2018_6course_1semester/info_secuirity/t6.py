"""
task 6 of computer security lessons
"""

def parity_word(text: bytes):
    previous_char = text[0]
    for char in text[1:]:
        previous_char = previous_char^char
    return previous_char



def parity_word_v2(text: bytes, word_len=4):
    chunked_text = [text[i:i+word_len] for i in range(0, len(text), word_len)]

    if len(chunked_text[-1]) != word_len:
        chunked_text[-1] += b"\x00"*(word_len-len(chunked_text[-1]))

    summer_chunk = [0 for i in range(word_len)]
    for chunk in chunked_text:
        new_chunk = []
        for byte in chunk:
            new_chunk.append(byte)
        summer_chunk = [x^y for x,y in zip(summer_chunk, new_chunk)]

    return b"".join([bytes(summer_chunk)])


if __name__ == '__main__':
    with open("text_carrier.txt", "rb") as file:
        result = parity_word_v2(file.read(), 4)
        print(int.from_bytes(result, 'big'))
        2668073485

