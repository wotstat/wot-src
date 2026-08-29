__all__ = [
 b'encode', b'decode']
import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Crypto.Util.py21compat import *
from Crypto.Util.py3compat import *
import re
from binascii import hexlify, unhexlify, a2b_base64, b2a_base64
from Crypto.Hash import MD5
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import DES, DES3, AES
from Crypto.Protocol.KDF import PBKDF1
from Crypto.Random import get_random_bytes

def encode(data, marker, passphrase=None, randfunc=None):
    if randfunc is None:
        randfunc = get_random_bytes
    out = b'-----BEGIN %s-----\n' % marker
    if passphrase:
        salt = randfunc(8)
        key = PBKDF1(passphrase, salt, 16, 1, MD5)
        key += PBKDF1(key + passphrase, salt, 8, 1, MD5)
        objenc = DES3.new(key, DES3.MODE_CBC, salt)
        out += b'Proc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,%s\n\n' % tostr(hexlify(salt).upper())
        data = objenc.encrypt(pad(data, objenc.block_size))
    chunks = [tostr(b2a_base64(data[i:i + 48])) for i in range(0, len(data), 48)]
    out += (b'').join(chunks)
    out += b'-----END %s-----' % marker
    return out


def decode(pem_data, passphrase=None):
    r = re.compile(b'\\s*-----BEGIN (.*)-----\n')
    m = r.match(pem_data)
    if not m:
        raise ValueError(b'Not a valid PEM pre boundary')
    marker = m.group(1)
    r = re.compile(b'-----END (.*)-----\\s*$')
    m = r.search(pem_data)
    if not m or m.group(1) != marker:
        raise ValueError(b'Not a valid PEM post boundary')
    lines = pem_data.replace(b' ', b'').split()
    if lines[1].startswith(b'Proc-Type:4,ENCRYPTED'):
        if not passphrase:
            raise ValueError(b'PEM is encrypted, but no passphrase available')
        DEK = lines[2].split(b':')
        if len(DEK) != 2 or DEK[0] != b'DEK-Info':
            raise ValueError(b'PEM encryption format not supported.')
        algo, salt = DEK[1].split(b',')
        salt = unhexlify(tobytes(salt))
        if algo == b'DES-CBC':
            key = PBKDF1(passphrase, salt, 8, 1, MD5)
            objdec = DES.new(key, DES.MODE_CBC, salt)
        elif algo == b'DES-EDE3-CBC':
            key = PBKDF1(passphrase, salt, 16, 1, MD5)
            key += PBKDF1(key + passphrase, salt, 8, 1, MD5)
            objdec = DES3.new(key, DES3.MODE_CBC, salt)
        elif algo == b'AES-128-CBC':
            key = PBKDF1(passphrase, salt[:8], 16, 1, MD5)
            objdec = AES.new(key, AES.MODE_CBC, salt)
        else:
            raise ValueError(b'Unsupport PEM encryption algorithm.')
        lines = lines[2:]
    else:
        objdec = None
    data = a2b_base64(b((b'').join(lines[1:-1])))
    enc_flag = False
    if objdec:
        data = unpad(objdec.decrypt(data), objdec.block_size)
        enc_flag = True
    return (data, marker, enc_flag)
