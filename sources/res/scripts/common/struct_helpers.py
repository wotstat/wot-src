from __future__ import absolute_import
from struct import unpack, pack

def unpackByte(char):
    return unpack(b'B', char)[0]


def packByte(code):
    return pack(b'B', code)
