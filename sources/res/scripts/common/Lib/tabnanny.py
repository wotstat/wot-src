__version__ = b'6'
import os, sys, getopt, tokenize
if not hasattr(tokenize, b'NL'):
    raise ValueError(b"tokenize.NL doesn't exist -- tokenize module too old")
__all__ = [b'check', b'NannyNag', b'process_tokens']
verbose = 0
filename_only = 0

def errprint(*args):
    sep = b''
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = b' '

    sys.stderr.write(b'\n')
    return


def main():
    global filename_only
    global verbose
    try:
        opts, args = getopt.getopt(sys.argv[1:], b'qv')
    except getopt.error as msg:
        errprint(msg)
        return

    for o, a in opts:
        if o == b'-q':
            filename_only = filename_only + 1
        if o == b'-v':
            verbose = verbose + 1

    if not args:
        errprint(b'Usage:', sys.argv[0], b'[-v] file_or_directory ...')
        return
    for arg in args:
        check(arg)

    return


class NannyNag(Exception):

    def __init__(self, lineno, msg, line):
        self.lineno, self.msg, self.line = lineno, msg, line
        return

    def get_lineno(self):
        return self.lineno

    def get_msg(self):
        return self.msg

    def get_line(self):
        return self.line


def check(file):
    if os.path.isdir(file) and not os.path.islink(file):
        if verbose:
            print b'%r: listing directory' % (file,)
        names = os.listdir(file)
        for name in names:
            fullname = os.path.join(file, name)
            if os.path.isdir(fullname) and not os.path.islink(fullname) or os.path.normcase(name[-3:]) == b'.py':
                check(fullname)

        return
    try:
        f = open(file)
    except IOError as msg:
        errprint(b'%r: I/O Error: %s' % (file, msg))
        return

    if verbose > 1:
        print b'checking %r ...' % file
    try:
        process_tokens(tokenize.generate_tokens(f.readline))
    except tokenize.TokenError as msg:
        errprint(b'%r: Token Error: %s' % (file, msg))
        return
    except IndentationError as msg:
        errprint(b'%r: Indentation Error: %s' % (file, msg))
        return
    except NannyNag as nag:
        badline = nag.get_lineno()
        line = nag.get_line()
        if verbose:
            print b'%r: *** Line %d: trouble in tab city! ***' % (file, badline)
            print b'offending line: %r' % (line,)
            print nag.get_msg()
        elif b' ' in file:
            file = b'"' + file + b'"'
        if filename_only:
            print file
        else:
            print file, badline, repr(line)
        return

    if verbose:
        print b'%r: Clean bill of health.' % (file,)
    return


class Whitespace:
    S, T = b' \t'

    def __init__(self, ws):
        self.raw = ws
        S, T = Whitespace.S, Whitespace.T
        count = []
        b = n = nt = 0
        for ch in self.raw:
            if ch == S:
                n = n + 1
                b = b + 1
            elif ch == T:
                n = n + 1
                nt = nt + 1
                if b >= len(count):
                    count = count + [0] * (b - len(count) + 1)
                count[b] = count[b] + 1
                b = 0
            else:
                break

        self.n = n
        self.nt = nt
        self.norm = (tuple(count), b)
        self.is_simple = len(count) <= 1
        return

    def longest_run_of_spaces(self):
        count, trailing = self.norm
        return max(len(count) - 1, trailing)

    def indent_level(self, tabsize):
        count, trailing = self.norm
        il = 0
        for i in range(tabsize, len(count)):
            il = il + i / tabsize * count[i]

        return trailing + tabsize * (il + self.nt)

    def equal(self, other):
        return self.norm == other.norm

    def not_equal_witness(self, other):
        n = max(self.longest_run_of_spaces(), other.longest_run_of_spaces()) + 1
        a = []
        for ts in range(1, n + 1):
            if self.indent_level(ts) != other.indent_level(ts):
                a.append((ts,
                 self.indent_level(ts),
                 other.indent_level(ts)))

        return a

    def less(self, other):
        if self.n >= other.n:
            return False
        if self.is_simple and other.is_simple:
            return self.nt <= other.nt
        n = max(self.longest_run_of_spaces(), other.longest_run_of_spaces()) + 1
        for ts in range(2, n + 1):
            if self.indent_level(ts) >= other.indent_level(ts):
                return False

        return True

    def not_less_witness(self, other):
        n = max(self.longest_run_of_spaces(), other.longest_run_of_spaces()) + 1
        a = []
        for ts in range(1, n + 1):
            if self.indent_level(ts) >= other.indent_level(ts):
                a.append((ts,
                 self.indent_level(ts),
                 other.indent_level(ts)))

        return a


def format_witnesses(w):
    firsts = map((lambda tup: str(tup[0])), w)
    prefix = b'at tab size'
    if len(w) > 1:
        prefix = prefix + b's'
    return prefix + b' ' + (b', ').join(firsts)


def process_tokens(tokens):
    INDENT = tokenize.INDENT
    DEDENT = tokenize.DEDENT
    NEWLINE = tokenize.NEWLINE
    JUNK = (tokenize.COMMENT, tokenize.NL)
    indents = [Whitespace(b'')]
    check_equal = 0
    for type, token, start, end, line in tokens:
        if type == NEWLINE:
            check_equal = 1
        elif type == INDENT:
            check_equal = 0
            thisguy = Whitespace(token)
            if not indents[-1].less(thisguy):
                witness = indents[-1].not_less_witness(thisguy)
                msg = b'indent not greater e.g. ' + format_witnesses(witness)
                raise NannyNag(start[0], msg, line)
            indents.append(thisguy)
        elif type == DEDENT:
            check_equal = 1
            del indents[-1]
        elif check_equal and type not in JUNK:
            check_equal = 0
            thisguy = Whitespace(line)
            if not indents[-1].equal(thisguy):
                witness = indents[-1].not_equal_witness(thisguy)
                msg = b'indent not equal e.g. ' + format_witnesses(witness)
                raise NannyNag(start[0], msg, line)

    return


if __name__ == b'__main__':
    main()
