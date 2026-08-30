__revision__ = b'$Id$'
from Crypto.Util.py3compat import *
import _ARC4

class ARC4Cipher:

    def __init__(self, key, *args, **kwargs):
        if len(args) > 0:
            ndrop = args[0]
            args = args[1:]
        else:
            ndrop = kwargs.get(b'drop', 0)
            if ndrop:
                del kwargs[b'drop']
        self._cipher = _ARC4.new(key, *args, **kwargs)
        if ndrop:
            self._cipher.encrypt(b(b'\x00') * ndrop)
        self.block_size = self._cipher.block_size
        self.key_size = self._cipher.key_size
        return

    def encrypt(self, plaintext):
        return self._cipher.encrypt(plaintext)

    def decrypt(self, ciphertext):
        return self._cipher.decrypt(ciphertext)


def new(key, *args, **kwargs):
    return ARC4Cipher(key, *args, **kwargs)


block_size = 1
key_size = xrange(1, 257)
