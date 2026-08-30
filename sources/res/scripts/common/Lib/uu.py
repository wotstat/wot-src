import binascii, os, sys
__all__ = [
 b'Error', b'encode', b'decode']

class Error(Exception):
    pass


def encode(in_file, out_file, name=None, mode=None):
    opened_files = []
    try:
        if in_file == b'-':
            in_file = sys.stdin
        elif isinstance(in_file, basestring):
            if name is None:
                name = os.path.basename(in_file)
            if mode is None:
                try:
                    mode = os.stat(in_file).st_mode
                except AttributeError:
                    pass

            in_file = open(in_file, b'rb')
            opened_files.append(in_file)
        if out_file == b'-':
            out_file = sys.stdout
        elif isinstance(out_file, basestring):
            out_file = open(out_file, b'wb')
            opened_files.append(out_file)
        if name is None:
            name = b'-'
        if mode is None:
            mode = 438
        name = name.replace(b'\n', b'\\n')
        name = name.replace(b'\r', b'\\r')
        out_file.write(b'begin %o %s\n' % (mode & 511, name))
        data = in_file.read(45)
        while len(data) > 0:
            out_file.write(binascii.b2a_uu(data))
            data = in_file.read(45)

        out_file.write(b' \nend\n')
    finally:
        for f in opened_files:
            f.close()

    return


def decode(in_file, out_file=None, mode=None, quiet=0):
    opened_files = []
    if in_file == b'-':
        in_file = sys.stdin
    elif isinstance(in_file, basestring):
        in_file = open(in_file)
        opened_files.append(in_file)
    try:
        while True:
            hdr = in_file.readline()
            if not hdr:
                raise Error(b'No valid begin line found in input file')
            if not hdr.startswith(b'begin'):
                continue
            hdrfields = hdr.split(b' ', 2)
            if len(hdrfields) == 3 and hdrfields[0] == b'begin':
                try:
                    int(hdrfields[1], 8)
                    break
                except ValueError:
                    pass

        if out_file is None:
            out_file = hdrfields[2].rstrip()
            if os.path.exists(out_file):
                raise Error(b'Cannot overwrite existing file: %s' % out_file)
        if mode is None:
            mode = int(hdrfields[1], 8)
        if out_file == b'-':
            out_file = sys.stdout
        elif isinstance(out_file, basestring):
            fp = open(out_file, b'wb')
            try:
                os.path.chmod(out_file, mode)
            except AttributeError:
                pass

            out_file = fp
            opened_files.append(out_file)
        s = in_file.readline()
        while s and s.strip() != b'end':
            try:
                data = binascii.a2b_uu(s)
            except binascii.Error as v:
                nbytes = ((ord(s[0]) - 32 & 63) * 4 + 5) // 3
                data = binascii.a2b_uu(s[:nbytes])
                if not quiet:
                    sys.stderr.write(b'Warning: %s\n' % v)

            out_file.write(data)
            s = in_file.readline()

        if not s:
            raise Error(b'Truncated input file')
    finally:
        for f in opened_files:
            f.close()

    return


def test():
    import optparse
    parser = optparse.OptionParser(usage=b'usage: %prog [-d] [-t] [input [output]]')
    parser.add_option(b'-d', b'--decode', dest=b'decode', help=b'Decode (instead of encode)?', default=False, action=b'store_true')
    parser.add_option(b'-t', b'--text', dest=b'text', help=b'data is text, encoded format unix-compatible text?', default=False, action=b'store_true')
    options, args = parser.parse_args()
    if len(args) > 2:
        parser.error(b'incorrect number of arguments')
        sys.exit(1)
    input = sys.stdin
    output = sys.stdout
    if len(args) > 0:
        input = args[0]
    if len(args) > 1:
        output = args[1]
    if options.decode:
        if options.text:
            if isinstance(output, basestring):
                output = open(output, b'w')
            else:
                print sys.argv[0], b': cannot do -t to stdout'
                sys.exit(1)
        decode(input, output)
    elif options.text:
        if isinstance(input, basestring):
            input = open(input, b'r')
        else:
            print sys.argv[0], b': cannot do -t from stdin'
            sys.exit(1)
    encode(input, output)
    return


if __name__ == b'__main__':
    test()
