__revision__ = b'$Id$'
import sys
if sys.version_info[0] == 2:
    from types import UnicodeType as _UnicodeType

    def b(s):
        return s


    def bchr(s):
        return chr(s)


    def bstr(s):
        return str(s)


    def bord(s):
        return ord(s)


    def tobytes(s):
        if isinstance(s, _UnicodeType):
            return s.encode(b'latin-1')
        else:
            return (b'').join(s)

        return


    def tostr(bs):
        return unicode(bs, b'latin-1')


    from StringIO import StringIO as BytesIO
else:

    def b(s):
        return s.encode(b'latin-1')


    def bchr(s):
        return bytes([s])


    def bstr(s):
        if isinstance(s, str):
            return bytes(s, b'latin-1')
        else:
            return bytes(s)

        return


    def bord(s):
        return s


    def tobytes(s):
        if isinstance(s, bytes):
            return s
        else:
            if isinstance(s, str):
                return s.encode(b'latin-1')
            return bytes(s)

        return


    def tostr(bs):
        return bs.decode(b'latin-1')


    from io import BytesIO
