import re
simple_escapes = {b'a': b'\x07', b'b': b'\x08', 
   b'f': b'\x0c', 
   b'n': b'\n', 
   b'r': b'\r', 
   b't': b'\t', 
   b'v': b'\x0b', 
   b"'": b"'", 
   b'"': b'"', 
   b'\\': b'\\'}

def escape(m):
    all, tail = m.group(0, 1)
    esc = simple_escapes.get(tail)
    if esc is not None:
        return esc
    else:
        if tail.startswith(b'x'):
            hexes = tail[1:]
            if len(hexes) < 2:
                raise ValueError(b"invalid hex string escape ('\\%s')" % tail)
            try:
                i = int(hexes, 16)
            except ValueError:
                raise ValueError(b"invalid hex string escape ('\\%s')" % tail)

        else:
            try:
                i = int(tail, 8)
            except ValueError:
                raise ValueError(b"invalid octal string escape ('\\%s')" % tail)

        return chr(i)


def evalString(s):
    q = s[0]
    if s[:3] == q * 3:
        q = q * 3
    s = s[len(q):-len(q)]
    return re.sub(b'\\\\(\\\'|\\"|\\\\|[abfnrtv]|x.{0,2}|[0-7]{1,3})', escape, s)


def test():
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        if e != c:
            print i, c, s, e

    return


if __name__ == b'__main__':
    test()
