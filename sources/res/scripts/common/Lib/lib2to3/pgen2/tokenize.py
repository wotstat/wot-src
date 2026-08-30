__author__ = b'Ka-Ping Yee <ping@lfw.org>'
__credits__ = b'GvR, ESR, Tim Peters, Thomas Wouters, Fred Drake, Skip Montanaro'
import string, re
from codecs import BOM_UTF8, lookup
from lib2to3.pgen2.token import *
from . import token
__all__ = [x for x in dir(token) if x[0] != b'_'] + [b'tokenize',
 b'generate_tokens', b'untokenize']
del token
try:
    bytes
except NameError:
    bytes = str

def group(*choices):
    return b'(' + (b'|').join(choices) + b')'


def any(*choices):
    return group(*choices) + b'*'


def maybe(*choices):
    return group(*choices) + b'?'


Whitespace = b'[ \\f\\t]*'
Comment = b'#[^\\r\\n]*'
Ignore = Whitespace + any(b'\\\\\\r?\\n' + Whitespace) + maybe(Comment)
Name = b'[a-zA-Z_]\\w*'
Binnumber = b'0[bB][01]*'
Hexnumber = b'0[xX][\\da-fA-F]*[lL]?'
Octnumber = b'0[oO]?[0-7]*[lL]?'
Decnumber = b'[1-9]\\d*[lL]?'
Intnumber = group(Binnumber, Hexnumber, Octnumber, Decnumber)
Exponent = b'[eE][-+]?\\d+'
Pointfloat = group(b'\\d+\\.\\d*', b'\\.\\d+') + maybe(Exponent)
Expfloat = b'\\d+' + Exponent
Floatnumber = group(Pointfloat, Expfloat)
Imagnumber = group(b'\\d+[jJ]', Floatnumber + b'[jJ]')
Number = group(Imagnumber, Floatnumber, Intnumber)
Single = b"[^'\\\\]*(?:\\\\.[^'\\\\]*)*'"
Double = b'[^"\\\\]*(?:\\\\.[^"\\\\]*)*"'
Single3 = b"[^'\\\\]*(?:(?:\\\\.|'(?!''))[^'\\\\]*)*'''"
Double3 = b'[^"\\\\]*(?:(?:\\\\.|"(?!""))[^"\\\\]*)*"""'
Triple = group(b"[ubUB]?[rR]?'''", b'[ubUB]?[rR]?"""')
String = group(b"[uU]?[rR]?'[^\\n'\\\\]*(?:\\\\.[^\\n'\\\\]*)*'", b'[uU]?[rR]?"[^\\n"\\\\]*(?:\\\\.[^\\n"\\\\]*)*"')
Operator = group(b'\\*\\*=?', b'>>=?', b'<<=?', b'<>', b'!=', b'//=?', b'->', b'[+\\-*/%&@|^=<>]=?', b'~')
Bracket = b'[][(){}]'
Special = group(b'\\r?\\n', b'[:;.,`@]')
Funny = group(Operator, Bracket, Special)
PlainToken = group(Number, Funny, String, Name)
Token = Ignore + PlainToken
ContStr = group(b"[uUbB]?[rR]?'[^\\n'\\\\]*(?:\\\\.[^\\n'\\\\]*)*" + group(b"'", b'\\\\\\r?\\n'), b'[uUbB]?[rR]?"[^\\n"\\\\]*(?:\\\\.[^\\n"\\\\]*)*' + group(b'"', b'\\\\\\r?\\n'))
PseudoExtras = group(b'\\\\\\r?\\n', Comment, Triple)
PseudoToken = Whitespace + group(PseudoExtras, Number, Funny, ContStr, Name)
tokenprog, pseudoprog, single3prog, double3prog = map(re.compile, (Token, PseudoToken, Single3, Double3))
endprogs = {b"'": (re.compile(Single)), b'"': (re.compile(Double)), b"'''": single3prog, 
   b'"""': double3prog, b"r'''": single3prog, 
   b'r"""': double3prog, b"u'''": single3prog, 
   b'u"""': double3prog, b"b'''": single3prog, 
   b'b"""': double3prog, b"ur'''": single3prog, 
   b'ur"""': double3prog, b"br'''": single3prog, 
   b'br"""': double3prog, b"R'''": single3prog, 
   b'R"""': double3prog, b"U'''": single3prog, 
   b'U"""': double3prog, b"B'''": single3prog, 
   b'B"""': double3prog, b"uR'''": single3prog, 
   b'uR"""': double3prog, b"Ur'''": single3prog, 
   b'Ur"""': double3prog, b"UR'''": single3prog, 
   b'UR"""': double3prog, b"bR'''": single3prog, 
   b'bR"""': double3prog, b"Br'''": single3prog, 
   b'Br"""': double3prog, b"BR'''": single3prog, 
   b'BR"""': double3prog, b'r': None, 
   b'R': None, b'u': None, 
   b'U': None, b'b': None, 
   b'B': None}
triple_quoted = {}
for t in (b"'''", b'"""', b"r'''", b'r"""', b"R'''", b'R"""', b"u'''", b'u"""', b"U'''", b'U"""', b"b'''", b'b"""', b"B'''", b'B"""', b"ur'''", b'ur"""', b"Ur'''", b'Ur"""', b"uR'''", b'uR"""', b"UR'''", b'UR"""', b"br'''", b'br"""', b"Br'''", b'Br"""', b"bR'''", b'bR"""', b"BR'''", b'BR"""'):
    triple_quoted[t] = t

single_quoted = {}
for t in (b"'", b'"', b"r'", b'r"', b"R'", b'R"', b"u'", b'u"', b"U'", b'U"', b"b'", b'b"', b"B'", b'B"', b"ur'", b'ur"', b"Ur'", b'Ur"', b"uR'", b'uR"', b"UR'", b'UR"', b"br'", b'br"', b"Br'", b'Br"', b"bR'", b'bR"', b"BR'", b'BR"'):
    single_quoted[t] = t

tabsize = 8

class TokenError(Exception):
    pass


class StopTokenizing(Exception):
    pass


def printtoken(type, token, start, end, line):
    srow, scol = start
    erow, ecol = end
    print b'%d,%d-%d,%d:\t%s\t%s' % (
     srow, scol, erow, ecol, tok_name[type], repr(token))
    return


def tokenize(readline, tokeneater=printtoken):
    try:
        tokenize_loop(readline, tokeneater)
    except StopTokenizing:
        pass

    return


def tokenize_loop(readline, tokeneater):
    for token_info in generate_tokens(readline):
        tokeneater(*token_info)

    return


class Untokenizer:

    def __init__(self):
        self.tokens = []
        self.prev_row = 1
        self.prev_col = 0
        return

    def add_whitespace(self, start):
        row, col = start
        col_offset = col - self.prev_col
        if col_offset:
            self.tokens.append(b' ' * col_offset)
        return

    def untokenize(self, iterable):
        for t in iterable:
            if len(t) == 2:
                self.compat(t, iterable)
                break
            tok_type, token, start, end, line = t
            self.add_whitespace(start)
            self.tokens.append(token)
            self.prev_row, self.prev_col = end
            if tok_type in (NEWLINE, NL):
                self.prev_row += 1
                self.prev_col = 0

        return (b'').join(self.tokens)

    def compat(self, token, iterable):
        startline = False
        indents = []
        toks_append = self.tokens.append
        toknum, tokval = token
        if toknum in (NAME, NUMBER):
            tokval += b' '
        if toknum in (NEWLINE, NL):
            startline = True
        for tok in iterable:
            toknum, tokval = tok[:2]
            if toknum in (NAME, NUMBER):
                tokval += b' '
            if toknum == INDENT:
                indents.append(tokval)
                continue
            elif toknum == DEDENT:
                indents.pop()
                continue
            elif toknum in (NEWLINE, NL):
                startline = True
            elif startline and indents:
                toks_append(indents[-1])
                startline = False
            toks_append(tokval)

        return


cookie_re = re.compile(b'^[ \\t\\f]*#.*?coding[:=][ \\t]*([-\\w.]+)')
blank_re = re.compile(b'^[ \\t\\f]*(?:[#\\r\\n]|$)')

def _get_normal_name(orig_enc):
    enc = orig_enc[:12].lower().replace(b'_', b'-')
    if enc == b'utf-8' or enc.startswith(b'utf-8-'):
        return b'utf-8'
    if enc in (b'latin-1', b'iso-8859-1', b'iso-latin-1') or enc.startswith((b'latin-1-', b'iso-8859-1-', b'iso-latin-1-')):
        return b'iso-8859-1'
    return orig_enc


def detect_encoding(readline):
    bom_found = False
    encoding = None
    default = b'utf-8'

    def read_or_stop():
        try:
            return readline()
        except StopIteration:
            return bytes()

        return

    def find_cookie(line):
        try:
            line_string = line.decode(b'ascii')
        except UnicodeDecodeError:
            return

        match = cookie_re.match(line_string)
        if not match:
            return
        else:
            encoding = _get_normal_name(match.group(1))
            try:
                codec = lookup(encoding)
            except LookupError:
                raise SyntaxError(b'unknown encoding: ' + encoding)

            if bom_found:
                if codec.name != b'utf-8':
                    raise SyntaxError(b'encoding problem: utf-8')
                encoding += b'-sig'
            return encoding

    first = read_or_stop()
    if first.startswith(BOM_UTF8):
        bom_found = True
        first = first[3:]
        default = b'utf-8-sig'
    if not first:
        return (default, [])
    else:
        encoding = find_cookie(first)
        if encoding:
            return (encoding, [first])
        if not blank_re.match(first):
            return (default, [first])
        second = read_or_stop()
        if not second:
            return (default, [first])
        encoding = find_cookie(second)
        if encoding:
            return (encoding, [first, second])
        return (default, [first, second])


def untokenize(iterable):
    ut = Untokenizer()
    return ut.untokenize(iterable)


def generate_tokens(readline):
    lnum = parenlev = continued = 0
    namechars, numchars = string.ascii_letters + b'_', b'0123456789'
    contstr, needcont = (b'', 0)
    contline = None
    indents = [0]
    while 1:
        try:
            line = readline()
        except StopIteration:
            line = b''

        lnum = lnum + 1
        pos, max = 0, len(line)
        if contstr:
            if not line:
                raise TokenError, (b'EOF in multi-line string', strstart)
            endmatch = endprog.match(line)
            if endmatch:
                pos = end = endmatch.end(0)
                yield (STRING, contstr + line[:end],
                 strstart, (lnum, end), contline + line)
                contstr, needcont = (b'', 0)
                contline = None
            elif needcont and line[-2:] != b'\\\n' and line[-3:] != b'\\\r\n':
                yield (
                 ERRORTOKEN, contstr + line,
                 strstart, (lnum, len(line)), contline)
                contstr = b''
                contline = None
                continue
            else:
                contstr = contstr + line
                contline = contline + line
                continue
        elif parenlev == 0 and not continued:
            if not line:
                break
            column = 0
            while pos < max:
                if line[pos] == b' ':
                    column = column + 1
                elif line[pos] == b'\t':
                    column = (column // tabsize + 1) * tabsize
                elif line[pos] == b'\x0c':
                    column = 0
                else:
                    break
                pos = pos + 1

            if pos == max:
                break
            if line[pos] in b'#\r\n':
                if line[pos] == b'#':
                    comment_token = line[pos:].rstrip(b'\r\n')
                    nl_pos = pos + len(comment_token)
                    yield (COMMENT, comment_token,
                     (
                      lnum, pos), (lnum, pos + len(comment_token)), line)
                    yield (NL, line[nl_pos:],
                     (
                      lnum, nl_pos), (lnum, len(line)), line)
                else:
                    yield (
                     (
                      NL, COMMENT)[line[pos] == b'#'], line[pos:],
                     (
                      lnum, pos), (lnum, len(line)), line)
                continue
            if column > indents[-1]:
                indents.append(column)
                yield (INDENT, line[:pos], (lnum, 0), (lnum, pos), line)
            while column < indents[-1]:
                if column not in indents:
                    raise IndentationError(b'unindent does not match any outer indentation level', (
                     b'<tokenize>', lnum, pos, line))
                indents = indents[:-1]
                yield (DEDENT, b'', (lnum, pos), (lnum, pos), line)

        elif not line:
            raise TokenError, (b'EOF in multi-line statement', (lnum, 0))
        continued = 0
        while pos < max:
            pseudomatch = pseudoprog.match(line, pos)
            if pseudomatch:
                start, end = pseudomatch.span(1)
                spos, epos, pos = (lnum, start), (lnum, end), end
                token, initial = line[start:end], line[start]
                if initial in numchars or initial == b'.' and token != b'.':
                    yield (
                     NUMBER, token, spos, epos, line)
                elif initial in b'\r\n':
                    newline = NEWLINE
                    if parenlev > 0:
                        newline = NL
                    yield (
                     newline, token, spos, epos, line)
                if initial == b'#':
                    yield (COMMENT, token, spos, epos, line)
                elif token in triple_quoted:
                    endprog = endprogs[token]
                    endmatch = endprog.match(line, pos)
                    if endmatch:
                        pos = endmatch.end(0)
                        token = line[start:pos]
                        yield (STRING, token, spos, (lnum, pos), line)
                    else:
                        strstart = (
                         lnum, start)
                        contstr = line[start:]
                        contline = line
                        break
                elif initial in single_quoted or token[:2] in single_quoted or token[:3] in single_quoted:
                    if token[-1] == b'\n':
                        strstart = (
                         lnum, start)
                        endprog = endprogs[initial] or endprogs[token[1]] or endprogs[token[2]]
                        contstr, needcont = line[start:], 1
                        contline = line
                        break
                    else:
                        yield (
                         STRING, token, spos, epos, line)
                if initial in namechars:
                    yield (
                     NAME, token, spos, epos, line)
                elif initial == b'\\':
                    yield (NL, token, spos, (lnum, pos), line)
                    continued = 1
                else:
                    if initial in b'([{':
                        parenlev = parenlev + 1
                    elif initial in b')]}':
                        parenlev = parenlev - 1
                    yield (
                     OP, token, spos, epos, line)
            else:
                yield (
                 ERRORTOKEN, line[pos],
                 (
                  lnum, pos), (lnum, pos + 1), line)
                pos = pos + 1

    for indent in indents[1:]:
        yield (
         DEDENT, b'', (lnum, 0), (lnum, 0), b'')

    yield (
     ENDMARKER, b'', (lnum, 0), (lnum, 0), b'')
    return


if __name__ == b'__main__':
    import sys
    if len(sys.argv) > 1:
        tokenize(open(sys.argv[1]).readline)
    else:
        tokenize(sys.stdin.readline)
