import struct
try:
    from cStringIO import StringIO as _StringIO
except ImportError:
    from StringIO import StringIO as _StringIO

from functools import wraps
__all__ = [
 b'Error', b'Packer', b'Unpacker', b'ConversionError']

class Error(Exception):

    def __init__(self, msg):
        self.msg = msg
        return

    def __repr__(self):
        return repr(self.msg)

    def __str__(self):
        return str(self.msg)


class ConversionError(Error):
    pass


def raise_conversion_error(function):

    @wraps(function)
    def result(self, value):
        try:
            return function(self, value)
        except struct.error as e:
            raise ConversionError(e.args[0])

        return

    return result


class Packer:

    def __init__(self):
        self.reset()
        return

    def reset(self):
        self.__buf = _StringIO()
        return

    def get_buffer(self):
        return self.__buf.getvalue()

    get_buf = get_buffer

    @raise_conversion_error
    def pack_uint(self, x):
        self.__buf.write(struct.pack(b'>L', x))
        return

    @raise_conversion_error
    def pack_int(self, x):
        self.__buf.write(struct.pack(b'>l', x))
        return

    pack_enum = pack_int

    def pack_bool(self, x):
        if x:
            self.__buf.write(b'\x00\x00\x00\x01')
        else:
            self.__buf.write(b'\x00\x00\x00\x00')
        return

    def pack_uhyper(self, x):
        try:
            self.pack_uint(x >> 32 & 4294967295L)
        except (TypeError, struct.error) as e:
            raise ConversionError(e.args[0])

        try:
            self.pack_uint(x & 4294967295L)
        except (TypeError, struct.error) as e:
            raise ConversionError(e.args[0])

        return

    pack_hyper = pack_uhyper

    @raise_conversion_error
    def pack_float(self, x):
        self.__buf.write(struct.pack(b'>f', x))
        return

    @raise_conversion_error
    def pack_double(self, x):
        self.__buf.write(struct.pack(b'>d', x))
        return

    def pack_fstring(self, n, s):
        if n < 0:
            raise ValueError, b'fstring size must be nonnegative'
        data = s[:n]
        n = (n + 3) // 4 * 4
        data = data + (n - len(data)) * b'\x00'
        self.__buf.write(data)
        return

    pack_fopaque = pack_fstring

    def pack_string(self, s):
        n = len(s)
        self.pack_uint(n)
        self.pack_fstring(n, s)
        return

    pack_opaque = pack_string
    pack_bytes = pack_string

    def pack_list(self, list, pack_item):
        for item in list:
            self.pack_uint(1)
            pack_item(item)

        self.pack_uint(0)
        return

    def pack_farray(self, n, list, pack_item):
        if len(list) != n:
            raise ValueError, b'wrong array size'
        for item in list:
            pack_item(item)

        return

    def pack_array(self, list, pack_item):
        n = len(list)
        self.pack_uint(n)
        self.pack_farray(n, list, pack_item)
        return


class Unpacker:

    def __init__(self, data):
        self.reset(data)
        return

    def reset(self, data):
        self.__buf = data
        self.__pos = 0
        return

    def get_position(self):
        return self.__pos

    def set_position(self, position):
        self.__pos = position
        return

    def get_buffer(self):
        return self.__buf

    def done(self):
        if self.__pos < len(self.__buf):
            raise Error(b'unextracted data remains')
        return

    def unpack_uint(self):
        i = self.__pos
        self.__pos = j = i + 4
        data = self.__buf[i:j]
        if len(data) < 4:
            raise EOFError
        x = struct.unpack(b'>L', data)[0]
        try:
            return int(x)
        except OverflowError:
            return x

        return

    def unpack_int(self):
        i = self.__pos
        self.__pos = j = i + 4
        data = self.__buf[i:j]
        if len(data) < 4:
            raise EOFError
        return struct.unpack(b'>l', data)[0]

    unpack_enum = unpack_int

    def unpack_bool(self):
        return bool(self.unpack_int())

    def unpack_uhyper(self):
        hi = self.unpack_uint()
        lo = self.unpack_uint()
        return long(hi) << 32 | lo

    def unpack_hyper(self):
        x = self.unpack_uhyper()
        if x >= 9223372036854775808L:
            x = x - 18446744073709551616L
        return x

    def unpack_float(self):
        i = self.__pos
        self.__pos = j = i + 4
        data = self.__buf[i:j]
        if len(data) < 4:
            raise EOFError
        return struct.unpack(b'>f', data)[0]

    def unpack_double(self):
        i = self.__pos
        self.__pos = j = i + 8
        data = self.__buf[i:j]
        if len(data) < 8:
            raise EOFError
        return struct.unpack(b'>d', data)[0]

    def unpack_fstring(self, n):
        if n < 0:
            raise ValueError, b'fstring size must be nonnegative'
        i = self.__pos
        j = i + (n + 3) // 4 * 4
        if j > len(self.__buf):
            raise EOFError
        self.__pos = j
        return self.__buf[i:i + n]

    unpack_fopaque = unpack_fstring

    def unpack_string(self):
        n = self.unpack_uint()
        return self.unpack_fstring(n)

    unpack_opaque = unpack_string
    unpack_bytes = unpack_string

    def unpack_list(self, unpack_item):
        list = []
        while 1:
            x = self.unpack_uint()
            if x == 0:
                break
            if x != 1:
                raise ConversionError, b'0 or 1 expected, got %r' % (x,)
            item = unpack_item()
            list.append(item)

        return list

    def unpack_farray(self, n, unpack_item):
        list = []
        for i in range(n):
            list.append(unpack_item())

        return list

    def unpack_array(self, unpack_item):
        n = self.unpack_uint()
        return self.unpack_farray(n, unpack_item)
