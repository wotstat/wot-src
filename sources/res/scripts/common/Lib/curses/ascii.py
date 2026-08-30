NUL = 0
SOH = 1
STX = 2
ETX = 3
EOT = 4
ENQ = 5
ACK = 6
BEL = 7
BS = 8
TAB = 9
HT = 9
LF = 10
NL = 10
VT = 11
FF = 12
CR = 13
SO = 14
SI = 15
DLE = 16
DC1 = 17
DC2 = 18
DC3 = 19
DC4 = 20
NAK = 21
SYN = 22
ETB = 23
CAN = 24
EM = 25
SUB = 26
ESC = 27
FS = 28
GS = 29
RS = 30
US = 31
SP = 32
DEL = 127
controlnames = [
 34, 35, 36, 37, 38, 39, 40, 41, 
 42, 43, 44, 45, 46, 47, 48, 49, 
 50, 
 51, 52, 53, 54, 55, 56, 57, 
 58, 59, 60, 61, 62, 63, 64, 65, 
 66]

def _ctoi(c):
    if type(c) == type(b''):
        return ord(c)
    else:
        return c

    return


def isalnum(c):
    return isalpha(c) or isdigit(c)


def isalpha(c):
    return isupper(c) or islower(c)


def isascii(c):
    return 0 <= _ctoi(c) <= 127


def isblank(c):
    return _ctoi(c) in (9, 32)


def iscntrl(c):
    return 0 <= _ctoi(c) <= 31 or _ctoi(c) == 127


def isdigit(c):
    return 48 <= _ctoi(c) <= 57


def isgraph(c):
    return 33 <= _ctoi(c) <= 126


def islower(c):
    return 97 <= _ctoi(c) <= 122


def isprint(c):
    return 32 <= _ctoi(c) <= 126


def ispunct(c):
    return isgraph(c) and not isalnum(c)


def isspace(c):
    return _ctoi(c) in (9, 10, 11, 12, 13, 32)


def isupper(c):
    return 65 <= _ctoi(c) <= 90


def isxdigit(c):
    return ((isdigit(c)) or 65 <= _ctoi(c) <= 70) or 97 <= _ctoi(c) <= 102


def isctrl(c):
    return 0 <= _ctoi(c) < 32


def ismeta(c):
    return _ctoi(c) > 127


def ascii(c):
    if type(c) == type(b''):
        return chr(_ctoi(c) & 127)
    else:
        return _ctoi(c) & 127

    return


def ctrl(c):
    if type(c) == type(b''):
        return chr(_ctoi(c) & 31)
    else:
        return _ctoi(c) & 31

    return


def alt(c):
    if type(c) == type(b''):
        return chr(_ctoi(c) | 128)
    else:
        return _ctoi(c) | 128

    return


def unctrl(c):
    bits = _ctoi(c)
    if bits == 127:
        rep = b'^?'
    elif isprint(bits & 127):
        rep = chr(bits & 127)
    else:
        rep = b'^' + chr((bits & 127 | 32) + 32)
    if bits & 128:
        return b'!' + rep
    return rep
