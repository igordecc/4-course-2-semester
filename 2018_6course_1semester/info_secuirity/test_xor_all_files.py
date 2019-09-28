import unittest
import xor_all_files
import re

class TestXorAllFiles(unittest.TestCase):
    def test_files_exist(self):
        self.assertIsNotNone(xor_all_files.file)

    def test_reverse_encoding(self):
        file = xor_all_files.file
        xored = xor_all_files.xor_file(file)
        decoded_file = xor_all_files.xor_file(file)
        self.assertEquals(file, decoded_file)

    def test_key(self):
        key = xor_all_files.key()
        for char in key:
            result = re.match(["а-я"|"0-9"|"."|","|"!"|";"|"?"|" "], key)
            self.assertIsNotNone(result)


