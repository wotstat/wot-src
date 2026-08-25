r"""hashlib module - A common interface to many hash functions.

new(name, string='') - returns a new hash object implementing the
                       given hash function; initializing the hash
                       using the given string data.

Named constructor functions are also available, these are much faster
than using new():

md5(), sha1(), sha224(), sha256(), sha384(), and sha512()

More algorithms may be available on your platform but the above are guaranteed
to exist.  See the algorithms_guaranteed and algorithms_available attributes
to find out what algorithm names can be passed to new().

NOTE: If you want the adler32 or crc32 hash functions they are available in
the zlib module.

Choose your hash function wisely.  Some have known collision weaknesses.
sha384 and sha512 will be slow on 32 bit platforms.

Hash objects have these methods:
 - update(arg): Update the hash object with the string arg. Repeated calls
                are equivalent to a single call with the concatenation of all
                the arguments.
 - digest():    Return the digest of the strings passed to the update() method
                so far. This may contain non-ASCII characters, including
                NUL bytes.
 - hexdigest(): Like digest() except the digest is returned as a string of
                double length, containing only hexadecimal digits.
 - copy():      Return a copy (clone) of the hash object. This can be used to
                efficiently compute the digests of strings that share a common
                initial substring.

For example, to obtain the digest of the string 'Nobody inspects the
spammish repetition':

    >>> import hashlib
    >>> m = hashlib.md5()
    >>> m.update("Nobody inspects")
    >>> m.update(" the spammish repetition")
    >>> m.digest()
    '\xbbd\x9c\x83\xdd\x1e\xa5\xc9\xd9\xde\xc9\xa1\x8d\xf0\xff\xe9'

More condensed:

    >>> hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()
    'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'

"""
__always_supported = (b'md5', b'sha1', b'sha224', b'sha256', b'sha384', b'sha512')
algorithms_guaranteed = set(__always_supported)
algorithms_available = set(__always_supported)
algorithms = __always_supported
__all__ = __always_supported + (b'new', b'algorithms_guaranteed', b'algorithms_available', b'algorithms', b'pbkdf2_hmac')

def __get_builtin_constructor(name):
    try:
        if name in (b'SHA1', b'sha1'):
            import _sha
            return _sha.new
        if name in (b'MD5', b'md5'):
            import _md5
            return _md5.new
        if name in (b'SHA256', b'sha256', b'SHA224', b'sha224'):
            import _sha256
            bs = name[3:]
            if bs == b'256':
                return _sha256.sha256
            if bs == b'224':
                return _sha256.sha224
        elif name in (b'SHA512', b'sha512', b'SHA384', b'sha384'):
            import _sha512
            bs = name[3:]
            if bs == b'512':
                return _sha512.sha512
            if bs == b'384':
                return _sha512.sha384
    except ImportError:
        pass

    raise ValueError(b'unsupported hash type ' + name)
    return


def __get_openssl_constructor(name):
    try:
        f = getattr(_hashlib, b'openssl_' + name)
        f()
        return f
    except (AttributeError, ValueError):
        return __get_builtin_constructor(name)

    return


def __py_new(name, string=b''):
    return __get_builtin_constructor(name)(string)


def __hash_new(name, string=b''):
    try:
        return _hashlib.new(name, string)
    except ValueError:
        return __get_builtin_constructor(name)(string)

    return


try:
    import _hashlib
    new = __hash_new
    __get_hash = __get_openssl_constructor
    algorithms_available = algorithms_available.union(_hashlib.openssl_md_meth_names)
except ImportError:
    new = __py_new
    __get_hash = __get_builtin_constructor

for __func_name in __always_supported:
    try:
        globals()[__func_name] = __get_hash(__func_name)
    except ValueError:
        import logging
        logging.exception(b'code for hash %s was not found.', __func_name)

try:
    from _hashlib import pbkdf2_hmac
except ImportError:
    import binascii, struct
    _trans_5C = (b'').join(chr(x ^ 92) for x in range(256))
    _trans_36 = (b'').join(chr(x ^ 54) for x in range(256))

    def pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None):
        if not isinstance(hash_name, str):
            raise TypeError(hash_name)
        if not isinstance(password, (bytes, bytearray)):
            password = bytes(buffer(password))
        if not isinstance(salt, (bytes, bytearray)):
            salt = bytes(buffer(salt))
        inner = new(hash_name)
        outer = new(hash_name)
        blocksize = getattr(inner, b'block_size', 64)
        if len(password) > blocksize:
            password = new(hash_name, password).digest()
        password = password + b'\x00' * (blocksize - len(password))
        inner.update(password.translate(_trans_36))
        outer.update(password.translate(_trans_5C))

        def prf(msg, inner=inner, outer=outer):
            icpy = inner.copy()
            ocpy = outer.copy()
            icpy.update(msg)
            ocpy.update(icpy.digest())
            return ocpy.digest()

        if iterations < 1:
            raise ValueError(iterations)
        if dklen is None:
            dklen = outer.digest_size
        if dklen < 1:
            raise ValueError(dklen)
        hex_format_string = b'%%0%ix' % (new(hash_name).digest_size * 2)
        dkey = b''
        loop = 1
        while len(dkey) < dklen:
            prev = prf(salt + struct.pack(b'>I', loop))
            rkey = int(binascii.hexlify(prev), 16)
            for i in xrange(iterations - 1):
                prev = prf(prev)
                rkey ^= int(binascii.hexlify(prev), 16)

            loop += 1
            dkey += binascii.unhexlify(hex_format_string % rkey)

        return dkey[:dklen]


del __always_supported
del __func_name
del __get_hash
del __py_new
del __hash_new
del __get_openssl_constructor
