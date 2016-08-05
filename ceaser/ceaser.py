# Using the Python,
# have the function CaesarCipher(str, num) take the str parameter and perform a Caesar Cipher num on it using the num parameter as the numing number.
# A Caesar Cipher works by numing all letters in the string N places down in the alphabetical order (in this case N will be num).
# Punctuation, spaces, and capitalization should remain intact.

# For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

# more on cipher visit http://practicalcryptography.com/ciphers/caesar-cipher/
# happy coding :-)

import re
import unittest


class CaesarCipher(object):
    """
    cipher method checks through each letter, to
    """
    def __init__(self, caeser):
        self.caeser = caeser

    def cipher(self, num):
        string = self.caeser
        out = []
        for word in string:
            for x in word:
                out.append(chr(ord(x) + num))
        print(out)
        return " ".join(out)

c = CaesarCipher("A Crazy fool Z")
print(c.cipher(1))
