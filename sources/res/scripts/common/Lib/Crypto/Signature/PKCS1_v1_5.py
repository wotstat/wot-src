__revision__ = b'$Id$'
__all__ = [b'new', b'PKCS115_SigScheme']
import sys, Crypto.Util.number
from Crypto.Util.number import ceil_div
from Crypto.Util.asn1 import DerSequence, DerNull, DerOctetString, DerObjectId
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from Crypto.Util.py21compat import *
from Crypto.Util.py3compat import *

class PKCS115_SigScheme:

    def __init__(self, key):
        self._key = key
        return

    def can_sign(self):
        return self._key.has_private()

    def sign(self, mhash):
        modBits = Crypto.Util.number.size(self._key.n)
        k = ceil_div(modBits, 8)
        em = EMSA_PKCS1_V1_5_ENCODE(mhash, k)
        m = self._key.decrypt(em)
        S = bchr(0) * (k - len(m)) + m
        return S

    def verify(self, mhash, S):
        modBits = Crypto.Util.number.size(self._key.n)
        k = ceil_div(modBits, 8)
        if len(S) != k:
            return 0
        m = self._key.encrypt(S, 0)[0]
        em1 = bchr(0) * (k - len(m)) + m
        try:
            em2_with_params = EMSA_PKCS1_V1_5_ENCODE(mhash, k, True)
            if _HASH_OIDS[mhash.name].startswith(b'1.2.840.113549.2.'):
                em2_without_params = em2_with_params
            else:
                em2_without_params = EMSA_PKCS1_V1_5_ENCODE(mhash, k, False)
        except ValueError:
            return 0

        return em1 == em2_with_params or em1 == em2_without_params


def EMSA_PKCS1_V1_5_ENCODE(hash, emLen, with_hash_parameters=True):
    if with_hash_parameters:
        digestAlgo = DerSequence([
         DerObjectId(_HASH_OIDS[hash.name]).encode(),
         DerNull().encode()])
    else:
        digestAlgo = DerSequence([
         DerObjectId(_HASH_OIDS[hash.name]).encode()])
    digest = DerOctetString(hash.digest())
    digestInfo = DerSequence([
     digestAlgo.encode(),
     digest.encode()]).encode()
    if emLen < len(digestInfo) + 11:
        raise TypeError(b'Selected hash algorith has a too long digest (%d bytes).' % len(digest))
    PS = bchr(255) * (emLen - len(digestInfo) - 3)
    return b(b'\x00\x01') + PS + bchr(0) + digestInfo


def new(key):
    return PKCS115_SigScheme(key)


_HASH_OIDS = {b'MD2': b'1.2.840.113549.2.2', 
   b'md2': b'1.2.840.113549.2.2', 
   b'MD4': b'1.2.840.113549.2.4', 
   b'md4': b'1.2.840.113549.2.4', 
   b'MD5': b'1.2.840.113549.2.5', 
   b'md5': b'1.2.840.113549.2.5', 
   b'RIPEMD160': b'1.3.36.3.2.1', 
   b'ripemd160': b'1.3.36.3.2.1', 
   b'SHA1': b'1.3.14.3.2.26', 
   b'sha1': b'1.3.14.3.2.26', 
   b'SHA224': b'2.16.840.1.101.3.4.2.4', 
   b'sha224': b'2.16.840.1.101.3.4.2.4', 
   b'SHA256': b'2.16.840.1.101.3.4.2.1', 
   b'sha256': b'2.16.840.1.101.3.4.2.1', 
   b'SHA384': b'2.16.840.1.101.3.4.2.2', 
   b'sha384': b'2.16.840.1.101.3.4.2.2', 
   b'SHA512': b'2.16.840.1.101.3.4.2.3', 
   b'sha512': b'2.16.840.1.101.3.4.2.3'}
