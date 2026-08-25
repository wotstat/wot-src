import re, struct, string, binascii
__all__ = [
 2, 3, 4, 5, 
 6, 7, 8, 9, 
 10, 11, 
 12, 13, 
 14, 15]
_translation = [chr(_x) for _x in range(256)]
EMPTYSTRING = b''

def _translate(s, altchars):
    translation = _translation[:]
    for k, v in altchars.items():
        translation[ord(k)] = v

    return s.translate((b'').join(translation))


def b64encode(s, altchars=None):
    encoded = binascii.b2a_base64(s)[:-1]
    if altchars is not None:
        return encoded.translate(string.maketrans(b'+/', altchars[:2]))
    else:
        return encoded


def b64decode(s, altchars=None):
    if altchars is not None:
        s = s.translate(string.maketrans(altchars[:2], b'+/'))
    try:
        return binascii.a2b_base64(s)
    except binascii.Error as msg:
        raise TypeError(msg)

    return


def standard_b64encode(s):
    return b64encode(s)


def standard_b64decode(s):
    return b64decode(s)


_urlsafe_encode_translation = string.maketrans(b'+/', b'-_')
_urlsafe_decode_translation = string.maketrans(b'-_', b'+/')

def urlsafe_b64encode(s):
    return b64encode(s).translate(_urlsafe_encode_translation)


def urlsafe_b64decode(s):
    return b64decode(s.translate(_urlsafe_decode_translation))


_b32alphabet = {0: b'A', 
   9: b'J', 18: b'S', 27: b'3', 1: b'B', 
   10: b'K', 19: b'T', 28: b'4', 2: b'C', 
   11: b'L', 20: b'U', 29: b'5', 3: b'D', 
   12: b'M', 21: b'V', 30: b'6', 4: b'E', 
   13: b'N', 22: b'W', 31: b'7', 5: b'F', 
   14: b'O', 23: b'X', 6: b'G', 
   15: b'P', 24: b'Y', 7: b'H', 
   16: b'Q', 25: b'Z', 8: b'I', 
   17: b'R', 26: b'2'}
_b32tab = _b32alphabet.items()
_b32tab.sort()
_b32tab = [v for k, v in _b32tab]
_b32rev = dict([(v, long(k)) for k, v in _b32alphabet.items()])

def b32encode(s):
    parts = []
    quanta, leftover = divmod(len(s), 5)
    if leftover:
        s += b'\x00' * (5 - leftover)
        quanta += 1
    for i in range(quanta):
        c1, c2, c3 = struct.unpack(b'!HHB', s[i * 5:(i + 1) * 5])
        c2 += (c1 & 1) << 16
        c3 += (c2 & 3) << 8
        parts.extend([_b32tab[c1 >> 11],
         _b32tab[c1 >> 6 & 31],
         _b32tab[c1 >> 1 & 31],
         _b32tab[c2 >> 12],
         _b32tab[c2 >> 7 & 31],
         _b32tab[c2 >> 2 & 31],
         _b32tab[c3 >> 5],
         _b32tab[c3 & 31]])

    encoded = EMPTYSTRING.join(parts)
    if leftover == 1:
        return encoded[:-6] + b'======'
    if leftover == 2:
        return encoded[:-4] + b'===='
    if leftover == 3:
        return encoded[:-3] + b'==='
    if leftover == 4:
        return encoded[:-1] + b'='
    return encoded


def b32decode(s, casefold=False, map01=None):
    quanta, leftover = divmod(len(s), 8)
    if leftover:
        raise TypeError(b'Incorrect padding')
    if map01:
        s = s.translate(string.maketrans(b'01', b'O' + map01))
    if casefold:
        s = s.upper()
    padchars = 0
    mo = re.search(b'(?P<pad>[=]*)$', s)
    if mo:
        padchars = len(mo.group(b'pad'))
        if padchars > 0:
            s = s[:-padchars]
    parts = []
    acc = 0
    shift = 35
    for c in s:
        val = _b32rev.get(c)
        if val is None:
            raise TypeError(b'Non-base32 digit found')
        acc += _b32rev[c] << shift
        shift -= 5
        if shift < 0:
            parts.append(binascii.unhexlify(b'%010x' % acc))
            acc = 0
            shift = 35

    last = binascii.unhexlify(b'%010x' % acc)
    if padchars == 0:
        last = b''
    elif padchars == 1:
        last = last[:-1]
    elif padchars == 3:
        last = last[:-2]
    elif padchars == 4:
        last = last[:-3]
    elif padchars == 6:
        last = last[:-4]
    else:
        raise TypeError(b'Incorrect padding')
    parts.append(last)
    return EMPTYSTRING.join(parts)


def b16encode(s):
    return binascii.hexlify(s).upper()


def b16decode(s, casefold=False):
    if casefold:
        s = s.upper()
    if re.search(b'[^0-9A-F]', s):
        raise TypeError(b'Non-base16 digit found')
    return binascii.unhexlify(s)


MAXLINESIZE = 76
MAXBINSIZE = MAXLINESIZE // 4 * 3

def encode(input, output):
    while True:
        s = input.read(MAXBINSIZE)
        if not s:
            break
        while len(s) < MAXBINSIZE:
            ns = input.read(MAXBINSIZE - len(s))
            if not ns:
                break
            s += ns

        line = binascii.b2a_base64(s)
        output.write(line)

    return


def decode(input, output):
    while True:
        line = input.readline()
        if not line:
            break
        s = binascii.a2b_base64(line)
        output.write(s)

    return


def encodestring(s):
    pieces = []
    for i in range(0, len(s), MAXBINSIZE):
        chunk = s[i:i + MAXBINSIZE]
        pieces.append(binascii.b2a_base64(chunk))

    return (b'').join(pieces)


def decodestring(s):
    return binascii.a2b_base64(s)


def test():
    import sys, getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], b'deut')
    except getopt.error as msg:
        sys.stdout = sys.stderr
        print msg
        print b"usage: %s [-d|-e|-u|-t] [file|-]\n        -d, -u: decode\n        -e: encode (default)\n        -t: encode and decode string 'Aladdin:open sesame'" % sys.argv[0]
        sys.exit(2)

    func = encode
    for o, a in opts:
        if o == b'-e':
            func = encode
        if o == b'-d':
            func = decode
        if o == b'-u':
            func = decode
        if o == b'-t':
            test1()
            return

    if args and args[0] != b'-':
        with open(args[0], b'rb') as f:
            func(f, sys.stdout)
    else:
        func(sys.stdin, sys.stdout)
    return


def test1():
    s0 = b'Aladdin:open sesame'
    s1 = encodestring(s0)
    s2 = decodestring(s1)
    print s0, repr(s1), s2
    return


if __name__ == b'__main__':
    test()
