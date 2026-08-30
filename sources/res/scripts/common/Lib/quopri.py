__all__ = [
 b'encode', b'decode', b'encodestring', b'decodestring']
ESCAPE = b'='
MAXLINESIZE = 76
HEX = b'0123456789ABCDEF'
EMPTYSTRING = b''
try:
    from binascii import a2b_qp, b2a_qp
except ImportError:
    a2b_qp = None
    b2a_qp = None

def needsquoting(c, quotetabs, header):
    if c in b' \t':
        return quotetabs
    if c == b'_':
        return header
    return c == ESCAPE or not b' ' <= c <= b'~'


def quote(c):
    i = ord(c)
    return ESCAPE + HEX[i // 16] + HEX[i % 16]


def encode(input, output, quotetabs, header=0):
    if b2a_qp is not None:
        data = input.read()
        odata = b2a_qp(data, quotetabs=quotetabs, header=header)
        output.write(odata)
        return
    else:

        def write(s, output=output, lineEnd=b'\n'):
            if s and s[-1:] in b' \t':
                output.write(s[:-1] + quote(s[-1]) + lineEnd)
            elif s == b'.':
                output.write(quote(s) + lineEnd)
            else:
                output.write(s + lineEnd)
            return

        prevline = None
        while 1:
            line = input.readline()
            if not line:
                break
            outline = []
            stripped = b''
            if line[-1:] == b'\n':
                line = line[:-1]
                stripped = b'\n'
            for c in line:
                if needsquoting(c, quotetabs, header):
                    c = quote(c)
                if header and c == b' ':
                    outline.append(b'_')
                else:
                    outline.append(c)

            if prevline is not None:
                write(prevline)
            thisline = EMPTYSTRING.join(outline)
            while len(thisline) > MAXLINESIZE:
                write(thisline[:MAXLINESIZE - 1], lineEnd=b'=\n')
                thisline = thisline[MAXLINESIZE - 1:]

            prevline = thisline

        if prevline is not None:
            write(prevline, lineEnd=stripped)
        return


def encodestring(s, quotetabs=0, header=0):
    if b2a_qp is not None:
        return b2a_qp(s, quotetabs=quotetabs, header=header)
    else:
        from cStringIO import StringIO
        infp = StringIO(s)
        outfp = StringIO()
        encode(infp, outfp, quotetabs, header)
        return outfp.getvalue()


def decode(input, output, header=0):
    if a2b_qp is not None:
        data = input.read()
        odata = a2b_qp(data, header=header)
        output.write(odata)
        return
    else:
        new = b''
        while 1:
            line = input.readline()
            if not line:
                break
            i, n = 0, len(line)
            if n > 0 and line[n - 1] == b'\n':
                partial = 0
                n = n - 1
                while n > 0 and line[n - 1] in b' \t\r':
                    n = n - 1

            else:
                partial = 1
            while i < n:
                c = line[i]
                if c == b'_' and header:
                    new = new + b' '
                    i = i + 1
                elif c != ESCAPE:
                    new = new + c
                    i = i + 1
                elif i + 1 == n and not partial:
                    partial = 1
                    break
                elif i + 1 < n and line[i + 1] == ESCAPE:
                    new = new + ESCAPE
                    i = i + 2
                elif i + 2 < n and ishex(line[i + 1]) and ishex(line[i + 2]):
                    new = new + chr(unhex(line[i + 1:i + 3]))
                    i = i + 3
                else:
                    new = new + c
                    i = i + 1

            if not partial:
                output.write(new + b'\n')
                new = b''

        if new:
            output.write(new)
        return


def decodestring(s, header=0):
    if a2b_qp is not None:
        return a2b_qp(s, header=header)
    else:
        from cStringIO import StringIO
        infp = StringIO(s)
        outfp = StringIO()
        decode(infp, outfp, header=header)
        return outfp.getvalue()


def ishex(c):
    return ((b'0' <= c <= b'9') or b'a' <= c <= b'f') or b'A' <= c <= b'F'


def unhex(s):
    bits = 0
    for c in s:
        if b'0' <= c <= b'9':
            i = ord(b'0')
        elif b'a' <= c <= b'f':
            i = ord(b'a') - 10
        elif b'A' <= c <= b'F':
            i = ord(b'A') - 10
        else:
            break
        bits = bits * 16 + (ord(c) - i)

    return bits


def main():
    import sys, getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], b'td')
    except getopt.error as msg:
        sys.stdout = sys.stderr
        print msg
        print b'usage: quopri [-t | -d] [file] ...'
        print b'-t: quote tabs'
        print b'-d: decode; default encode'
        sys.exit(2)

    deco = 0
    tabs = 0
    for o, a in opts:
        if o == b'-t':
            tabs = 1
        if o == b'-d':
            deco = 1

    if tabs and deco:
        sys.stdout = sys.stderr
        print b'-t and -d are mutually exclusive'
        sys.exit(2)
    if not args:
        args = [b'-']
    sts = 0
    for file in args:
        if file == b'-':
            fp = sys.stdin
        else:
            try:
                fp = open(file)
            except IOError as msg:
                sys.stderr.write(b"%s: can't open (%s)\n" % (file, msg))
                sts = 1
                continue

        if deco:
            decode(fp, sys.stdout)
        else:
            encode(fp, sys.stdout, tabs)
        if fp is not sys.stdin:
            fp.close()

    if sts:
        sys.exit(sts)
    return


if __name__ == b'__main__':
    main()
