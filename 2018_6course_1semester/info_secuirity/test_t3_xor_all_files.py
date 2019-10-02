import unittest
import t3_xor_all_files
import re

class TestXorAllFiles(unittest.TestCase):
    def test_files_exist(self):
        self.assertIsNotNone(t3_xor_all_files.file)

    def test_reverse_encoding(self):
        file = t3_xor_all_files.file
        xored = t3_xor_all_files.xor_file_for_txt(file)
        decoded_file = t3_xor_all_files.xor_file_for_txt(file)
        self.assertEquals(file, decoded_file)

    def test_key(self):
        key = t3_xor_all_files.key()
        for char in key:
            result = re.match(["а-я"|"0-9"|"."|","|"!"|";"|"?"|" "], key)
            self.assertIsNotNone(result)


