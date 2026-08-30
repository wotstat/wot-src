from warnings import warnpy3k
warnpy3k(b'the fpformat module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import re
__all__ = [
 b'fix', b'sci', b'NotANumber']
decoder = re.compile(b'^([-+]?)(\\d*)((?:\\.\\d*)?)(([eE][-+]?\\d+)?)$')
try:

    class NotANumber(ValueError):
        pass


except TypeError:
    NotANumber = b'fpformat.NotANumber'

def extract(s):
    res = decoder.match(s)
    if res is None:
        raise NotANumber, s
    sign, intpart, fraction, exppart = res.group(1, 2, 3, 4)
    intpart = intpart.lstrip(b'0')
    if sign == b'+':
        sign = b''
    if fraction:
        fraction = fraction[1:]
    if exppart:
        expo = int(exppart[1:])
    else:
        expo = 0
    return (
     sign, intpart, fraction, expo)


def unexpo(intpart, fraction, expo):
    if expo > 0:
        f = len(fraction)
        intpart, fraction = intpart + fraction[:expo], fraction[expo:]
        if expo > f:
            intpart = intpart + b'0' * (expo - f)
    elif expo < 0:
        i = len(intpart)
        intpart, fraction = intpart[:expo], intpart[expo:] + fraction
        if expo < -i:
            fraction = b'0' * (-expo - i) + fraction
    return (
     intpart, fraction)


def roundfrac(intpart, fraction, digs):
    f = len(fraction)
    if f <= digs:
        return (intpart, fraction + b'0' * (digs - f))
    else:
        i = len(intpart)
        if i + digs < 0:
            return (b'0' * -digs, b'')
        total = intpart + fraction
        nextdigit = total[i + digs]
        if nextdigit >= b'5':
            n = i + digs - 1
            while 1:
                if n >= 0:
                    if total[n] != b'9':
                        break
                    n = n - 1
            else:
                total = b'0' + total
                i = i + 1
                n = 0

            total = total[:n] + chr(ord(total[n]) + 1) + b'0' * (len(total) - n - 1)
            intpart, fraction = total[:i], total[i:]
        if digs >= 0:
            return (intpart, fraction[:digs])
        return (intpart[:digs] + b'0' * -digs, b'')

    return


def fix(x, digs):
    if type(x) != type(b''):
        x = repr(x)
    try:
        sign, intpart, fraction, expo = extract(x)
    except NotANumber:
        return x

    intpart, fraction = unexpo(intpart, fraction, expo)
    intpart, fraction = roundfrac(intpart, fraction, digs)
    while intpart and intpart[0] == b'0':
        intpart = intpart[1:]

    if intpart == b'':
        intpart = b'0'
    if digs > 0:
        return sign + intpart + b'.' + fraction
    else:
        return sign + intpart

    return


def sci(x, digs):
    if type(x) != type(b''):
        x = repr(x)
    sign, intpart, fraction, expo = extract(x)
    if not intpart:
        while fraction and fraction[0] == b'0':
            fraction = fraction[1:]
            expo = expo - 1

        if fraction:
            intpart, fraction = fraction[0], fraction[1:]
            expo = expo - 1
        else:
            intpart = b'0'
    else:
        expo = expo + len(intpart) - 1
        intpart, fraction = intpart[0], intpart[1:] + fraction
    digs = max(0, digs)
    intpart, fraction = roundfrac(intpart, fraction, digs)
    if len(intpart) > 1:
        intpart, fraction, expo = intpart[0], intpart[1:] + fraction[:-1], expo + len(intpart) - 1
    s = sign + intpart
    if digs > 0:
        s = s + b'.' + fraction
    e = repr(abs(expo))
    e = b'0' * (3 - len(e)) + e
    if expo < 0:
        e = b'-' + e
    else:
        e = b'+' + e
    return s + b'e' + e


def test():
    try:
        while 1:
            x, digs = input(b'Enter (x, digs): ')
            print x, fix(x, digs), sci(x, digs)

    except (EOFError, KeyboardInterrupt):
        pass

    return
