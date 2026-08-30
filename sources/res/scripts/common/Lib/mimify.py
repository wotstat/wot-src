MAXLEN = 200
CHARSET = b'ISO-8859-1'
QUOTE = b'> '
import re, warnings
warnings.warn(b'the mimify module is deprecated; use the email package instead', DeprecationWarning, 2)
__all__ = [
 b'mimify', b'unmimify', b'mime_encode_header', b'mime_decode_header']
qp = re.compile(b'^content-transfer-encoding:\\s*quoted-printable', re.I)
base64_re = re.compile(b'^content-transfer-encoding:\\s*base64', re.I)
mp = re.compile(b'^content-type:.*multipart/.*boundary="?([^;"\n]*)', re.I | re.S)
chrset = re.compile(b'^(content-type:.*charset=")(us-ascii|iso-8859-[0-9]+)(".*)', re.I | re.S)
he = re.compile(b'^-*\n')
mime_code = re.compile(b'=([0-9a-f][0-9a-f])', re.I)
mime_head = re.compile(b'=\\?iso-8859-1\\?q\\?([^? \t\n]+)\\?=', re.I)
repl = re.compile(b'^subject:\\s+re: ', re.I)

class File:

    def __init__(self, file, boundary):
        self.file = file
        self.boundary = boundary
        self.peek = None
        return

    def readline(self):
        if self.peek is not None:
            return b''
        else:
            line = self.file.readline()
            if not line:
                return line
            if self.boundary:
                if line == self.boundary + b'\n':
                    self.peek = line
                    return b''
                if line == self.boundary + b'--\n':
                    self.peek = line
                    return b''
            return line


class HeaderFile:

    def __init__(self, file):
        self.file = file
        self.peek = None
        return

    def readline(self):
        if self.peek is not None:
            line = self.peek
            self.peek = None
        else:
            line = self.file.readline()
        if not line:
            return line
        else:
            if he.match(line):
                return line
            while 1:
                self.peek = self.file.readline()
                if len(self.peek) == 0 or self.peek[0] != b' ' and self.peek[0] != b'\t':
                    return line
                line = line + self.peek
                self.peek = None

            return


def mime_decode(line):
    newline = b''
    pos = 0
    while 1:
        res = mime_code.search(line, pos)
        if res is None:
            break
        newline = newline + line[pos:res.start(0)] + chr(int(res.group(1), 16))
        pos = res.end(0)

    return newline + line[pos:]


def mime_decode_header(line):
    newline = b''
    pos = 0
    while 1:
        res = mime_head.search(line, pos)
        if res is None:
            break
        match = res.group(1)
        match = (b' ').join(match.split(b'_'))
        newline = newline + line[pos:res.start(0)] + mime_decode(match)
        pos = res.end(0)

    return newline + line[pos:]


def unmimify_part(ifile, ofile, decode_base64=0):
    multipart = None
    quoted_printable = 0
    is_base64 = 0
    is_repl = 0
    if ifile.boundary and ifile.boundary[:2] == QUOTE:
        prefix = QUOTE
    else:
        prefix = b''
    hfile = HeaderFile(ifile)
    while 1:
        line = hfile.readline()
        if not line:
            return
        if prefix and line[:len(prefix)] == prefix:
            line = line[len(prefix):]
            pref = prefix
        else:
            pref = b''
        line = mime_decode_header(line)
        if qp.match(line):
            quoted_printable = 1
            continue
        if decode_base64 and base64_re.match(line):
            is_base64 = 1
            continue
        ofile.write(pref + line)
        if not prefix and repl.match(line):
            is_repl = 1
        mp_res = mp.match(line)
        if mp_res:
            multipart = b'--' + mp_res.group(1)
        if he.match(line):
            break

    if is_repl and (quoted_printable or multipart):
        is_repl = 0
    while 1:
        line = ifile.readline()
        if not line:
            return
        line = re.sub(mime_head, b'\\1', line)
        if prefix and line[:len(prefix)] == prefix:
            line = line[len(prefix):]
            pref = prefix
        else:
            pref = b''
        while multipart:
            if line == multipart + b'--\n':
                ofile.write(pref + line)
                multipart = None
                line = None
                break
            if line == multipart + b'\n':
                ofile.write(pref + line)
                nifile = File(ifile, multipart)
                unmimify_part(nifile, ofile, decode_base64)
                line = nifile.peek
                if not line:
                    break
                continue
            break

        if line and quoted_printable:
            while line[-2:] == b'=\n':
                line = line[:-2]
                newline = ifile.readline()
                if newline[:len(QUOTE)] == QUOTE:
                    newline = newline[len(QUOTE):]
                line = line + newline

            line = mime_decode(line)
        if line and is_base64 and not pref:
            import base64
            line = base64.decodestring(line)
        if line:
            ofile.write(pref + line)

    return


def unmimify(infile, outfile, decode_base64=0):
    if type(infile) == type(b''):
        ifile = open(infile)
        if type(outfile) == type(b'') and infile == outfile:
            import os
            d, f = os.path.split(infile)
            os.rename(infile, os.path.join(d, b',' + f))
    else:
        ifile = infile
    if type(outfile) == type(b''):
        ofile = open(outfile, b'w')
    else:
        ofile = outfile
    nifile = File(ifile, None)
    unmimify_part(nifile, ofile, decode_base64)
    ofile.flush()
    return


mime_char = re.compile(b'[=\x7f-\xff]')
mime_header_char = re.compile(b'[=?\x7f-\xff]')

def mime_encode(line, header):
    if header:
        reg = mime_header_char
    else:
        reg = mime_char
    newline = b''
    pos = 0
    if len(line) >= 5 and line[:5] == b'From ':
        newline = (b'=%02x' % ord(b'F')).upper()
        pos = 1
    while 1:
        res = reg.search(line, pos)
        if res is None:
            break
        newline = newline + line[pos:res.start(0)] + (b'=%02x' % ord(res.group(0))).upper()
        pos = res.end(0)

    line = newline + line[pos:]
    newline = b''
    while len(line) >= 75:
        i = 73
        while line[i] == b'=' or line[i - 1] == b'=':
            i = i - 1

        i = i + 1
        newline = newline + line[:i] + b'=\n'
        line = line[i:]

    return newline + line


mime_header = re.compile(b'([ \t(]|^)([-a-zA-Z0-9_+]*[\x7f-\xff][-a-zA-Z0-9_+\x7f-\xff]*)(?=[ \t)]|\n)')

def mime_encode_header(line):
    newline = b''
    pos = 0
    while 1:
        res = mime_header.search(line, pos)
        if res is None:
            break
        newline = b'%s%s%s=?%s?Q?%s?=' % (
         newline, line[pos:res.start(0)], res.group(1),
         CHARSET, mime_encode(res.group(2), 1))
        pos = res.end(0)

    return newline + line[pos:]


mv = re.compile(b'^mime-version:', re.I)
cte = re.compile(b'^content-transfer-encoding:', re.I)
iso_char = re.compile(b'[\x7f-\xff]')

def mimify_part(ifile, ofile, is_mime):
    has_cte = is_qp = is_base64 = 0
    multipart = None
    must_quote_body = must_quote_header = has_iso_chars = 0
    header = []
    header_end = b''
    message = []
    message_end = b''
    hfile = HeaderFile(ifile)
    while 1:
        line = hfile.readline()
        if not line:
            break
        if not must_quote_header and iso_char.search(line):
            must_quote_header = 1
        if mv.match(line):
            is_mime = 1
        if cte.match(line):
            has_cte = 1
            if qp.match(line):
                is_qp = 1
            elif base64_re.match(line):
                is_base64 = 1
        mp_res = mp.match(line)
        if mp_res:
            multipart = b'--' + mp_res.group(1)
        if he.match(line):
            header_end = line
            break
        header.append(line)

    while 1:
        line = ifile.readline()
        if not line:
            break
        if multipart:
            if line == multipart + b'--\n':
                message_end = line
                break
            if line == multipart + b'\n':
                message_end = line
                break
        if is_base64:
            message.append(line)
            continue
        if is_qp:
            while line[-2:] == b'=\n':
                line = line[:-2]
                newline = ifile.readline()
                if newline[:len(QUOTE)] == QUOTE:
                    newline = newline[len(QUOTE):]
                line = line + newline

            line = mime_decode(line)
        message.append(line)
        if not has_iso_chars:
            if iso_char.search(line):
                has_iso_chars = must_quote_body = 1
        if not must_quote_body:
            if len(line) > MAXLEN:
                must_quote_body = 1

    for line in header:
        if must_quote_header:
            line = mime_encode_header(line)
        chrset_res = chrset.match(line)
        if chrset_res:
            if has_iso_chars:
                if chrset_res.group(2).lower() == b'us-ascii':
                    line = b'%s%s%s' % (chrset_res.group(1),
                     CHARSET,
                     chrset_res.group(3))
            else:
                line = b'%sus-ascii%s' % chrset_res.group(1, 3)
        if has_cte and cte.match(line):
            line = b'Content-Transfer-Encoding: '
            if is_base64:
                line = line + b'base64\n'
            elif must_quote_body:
                line = line + b'quoted-printable\n'
            else:
                line = line + b'7bit\n'
        ofile.write(line)

    if (must_quote_header or must_quote_body) and not is_mime:
        ofile.write(b'Mime-Version: 1.0\n')
        ofile.write(b'Content-Type: text/plain; ')
        if has_iso_chars:
            ofile.write(b'charset="%s"\n' % CHARSET)
        else:
            ofile.write(b'charset="us-ascii"\n')
    if must_quote_body and not has_cte:
        ofile.write(b'Content-Transfer-Encoding: quoted-printable\n')
    ofile.write(header_end)
    for line in message:
        if must_quote_body:
            line = mime_encode(line, 0)
        ofile.write(line)

    ofile.write(message_end)
    line = message_end
    while multipart:
        if line == multipart + b'--\n':
            while 1:
                line = ifile.readline()
                if not line:
                    return
                if must_quote_body:
                    line = mime_encode(line, 0)
                ofile.write(line)

        if line == multipart + b'\n':
            nifile = File(ifile, multipart)
            mimify_part(nifile, ofile, 1)
            line = nifile.peek
            if not line:
                break
            ofile.write(line)
            continue
        while 1:
            line = ifile.readline()
            if not line:
                return
            if must_quote_body:
                line = mime_encode(line, 0)
            ofile.write(line)

    return


def mimify(infile, outfile):
    if type(infile) == type(b''):
        ifile = open(infile)
        if type(outfile) == type(b'') and infile == outfile:
            import os
            d, f = os.path.split(infile)
            os.rename(infile, os.path.join(d, b',' + f))
    else:
        ifile = infile
    if type(outfile) == type(b''):
        ofile = open(outfile, b'w')
    else:
        ofile = outfile
    nifile = File(ifile, None)
    mimify_part(nifile, ofile, 0)
    ofile.flush()
    return


import sys
if __name__ == b'__main__' or len(sys.argv) > 0 and sys.argv[0] == b'mimify':
    import getopt
    usage = b'Usage: mimify [-l len] -[ed] [infile [outfile]]'
    decode_base64 = 0
    opts, args = getopt.getopt(sys.argv[1:], b'l:edb')
    if len(args) not in (0, 1, 2):
        print usage
        sys.exit(1)
    if ((b'-e', b'') in opts) == ((b'-d', b'') in opts) or (b'-b', b'') in opts and (b'-d', b'') not in opts:
        print usage
        sys.exit(1)
    for o, a in opts:
        if o == b'-e':
            encode = mimify
        elif o == b'-d':
            encode = unmimify
        elif o == b'-l':
            try:
                MAXLEN = int(a)
            except (ValueError, OverflowError):
                print usage
                sys.exit(1)

        elif o == b'-b':
            decode_base64 = 1

    if len(args) == 0:
        encode_args = (
         sys.stdin, sys.stdout)
    elif len(args) == 1:
        encode_args = (
         args[0], sys.stdout)
    else:
        encode_args = (
         args[0], args[1])
    if decode_base64:
        encode_args = encode_args + (decode_base64,)
    encode(*encode_args)
