import sys
from sre_constants import *
SPECIAL_CHARS = b'.\\[{()*+?^$|'
REPEAT_CHARS = b'*+?{'
DIGITS = set(b'0123456789')
OCTDIGITS = set(b'01234567')
HEXDIGITS = set(b'0123456789abcdefABCDEF')
ASCIILETTERS = set(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
WHITESPACE = set(b' \t\n\r\x0b\x0c')
ESCAPES = {b'\\a': (
          LITERAL, ord(b'\x07')), 
   b'\\b': (
          LITERAL, ord(b'\x08')), 
   b'\\f': (
          LITERAL, ord(b'\x0c')), 
   b'\\n': (
          LITERAL, ord(b'\n')), 
   b'\\r': (
          LITERAL, ord(b'\r')), 
   b'\\t': (
          LITERAL, ord(b'\t')), 
   b'\\v': (
          LITERAL, ord(b'\x0b')), 
   b'\\\\': (
           LITERAL, ord(b'\\'))}
CATEGORIES = {b'\\A': (
          AT, AT_BEGINNING_STRING), 
   b'\\b': (
          AT, AT_BOUNDARY), 
   b'\\B': (
          AT, AT_NON_BOUNDARY), 
   b'\\d': (
          IN, [(CATEGORY, CATEGORY_DIGIT)]), 
   b'\\D': (
          IN, [(CATEGORY, CATEGORY_NOT_DIGIT)]), 
   b'\\s': (
          IN, [(CATEGORY, CATEGORY_SPACE)]), 
   b'\\S': (
          IN, [(CATEGORY, CATEGORY_NOT_SPACE)]), 
   b'\\w': (
          IN, [(CATEGORY, CATEGORY_WORD)]), 
   b'\\W': (
          IN, [(CATEGORY, CATEGORY_NOT_WORD)]), 
   b'\\Z': (
          AT, AT_END_STRING)}
FLAGS = {b'i': SRE_FLAG_IGNORECASE, 
   b'L': SRE_FLAG_LOCALE, 
   b'm': SRE_FLAG_MULTILINE, 
   b's': SRE_FLAG_DOTALL, 
   b'x': SRE_FLAG_VERBOSE, 
   b't': SRE_FLAG_TEMPLATE, 
   b'u': SRE_FLAG_UNICODE}

class Pattern():

    def __init__(self):
        self.flags = 0
        self.open = []
        self.groups = 1
        self.groupdict = {}
        self.lookbehind = 0
        return

    def opengroup(self, name=None):
        gid = self.groups
        self.groups = gid + 1
        if name is not None:
            ogid = self.groupdict.get(name, None)
            if ogid is not None:
                raise error, b'redefinition of group name %s as group %d; was group %d' % (
                 repr(name), gid, ogid)
            self.groupdict[name] = gid
        self.open.append(gid)
        return gid

    def closegroup(self, gid):
        self.open.remove(gid)
        return

    def checkgroup(self, gid):
        return gid < self.groups and gid not in self.open


class SubPattern():

    def __init__(self, pattern, data=None):
        self.pattern = pattern
        if data is None:
            data = []
        self.data = data
        self.width = None
        return

    def dump(self, level=0):
        seqtypes = (tuple, list)
        for op, av in self.data:
            print level * b'  ' + op,
            if op == IN:
                print
                for op, a in av:
                    print (level + 1) * b'  ' + op, a

            elif op == BRANCH:
                print
                for i, a in enumerate(av[1]):
                    if i:
                        print level * b'  ' + b'or'
                    a.dump(level + 1)

            elif op == GROUPREF_EXISTS:
                condgroup, item_yes, item_no = av
                print condgroup
                item_yes.dump(level + 1)
                if item_no:
                    print level * b'  ' + b'else'
                    item_no.dump(level + 1)
            elif isinstance(av, seqtypes):
                nl = 0
                for a in av:
                    if isinstance(a, SubPattern):
                        if not nl:
                            print
                        a.dump(level + 1)
                        nl = 1
                    else:
                        print a,
                        nl = 0

                if not nl:
                    print
            else:
                print av

        return

    def __repr__(self):
        return repr(self.data)

    def __len__(self):
        return len(self.data)

    def __delitem__(self, index):
        del self.data[index]
        return

    def __getitem__(self, index):
        if isinstance(index, slice):
            return SubPattern(self.pattern, self.data[index])
        return self.data[index]

    def __setitem__(self, index, code):
        self.data[index] = code
        return

    def insert(self, index, code):
        self.data.insert(index, code)
        return

    def append(self, code):
        self.data.append(code)
        return

    def getwidth(self):
        if self.width:
            return self.width
        lo = hi = 0
        UNITCODES = (ANY, RANGE, IN, LITERAL, NOT_LITERAL, CATEGORY)
        REPEATCODES = (MIN_REPEAT, MAX_REPEAT)
        for op, av in self.data:
            if op is BRANCH:
                i = MAXREPEAT - 1
                j = 0
                for av in av[1]:
                    l, h = av.getwidth()
                    i = min(i, l)
                    j = max(j, h)

                lo = lo + i
                hi = hi + j
            elif op is CALL:
                i, j = av.getwidth()
                lo = lo + i
                hi = hi + j
            elif op is SUBPATTERN:
                i, j = av[1].getwidth()
                lo = lo + i
                hi = hi + j
            elif op in REPEATCODES:
                i, j = av[2].getwidth()
                lo = lo + i * av[0]
                hi = hi + j * av[1]
            elif op in UNITCODES:
                lo = lo + 1
                hi = hi + 1
            elif op == SUCCESS:
                break

        self.width = (
         min(lo, MAXREPEAT - 1), min(hi, MAXREPEAT))
        return self.width


class Tokenizer():

    def __init__(self, string):
        self.string = string
        self.index = 0
        self.__next()
        return

    def __next(self):
        if self.index >= len(self.string):
            self.next = None
            return
        else:
            char = self.string[self.index]
            if char[0] == b'\\':
                try:
                    c = self.string[self.index + 1]
                except IndexError:
                    raise error, b'bogus escape (end of line)'

                char = char + c
            self.index = self.index + len(char)
            self.next = char
            return

    def match(self, char, skip=1):
        if char == self.next:
            if skip:
                self.__next()
            return 1
        return 0

    def get(self):
        this = self.next
        self.__next()
        return this

    def tell(self):
        return (self.index, self.next)

    def seek(self, index):
        self.index, self.next = index
        return


def isident(char):
    return b'a' <= char <= b'z' or b'A' <= char <= b'Z' or char == b'_'


def isdigit(char):
    return b'0' <= char <= b'9'


def isname(name):
    if not isident(name[0]):
        return False
    for char in name[1:]:
        if not isident(char) and not isdigit(char):
            return False

    return True


def _class_escape(source, escape, nested):
    code = ESCAPES.get(escape)
    if code:
        return code
    code = CATEGORIES.get(escape)
    if code and code[0] == IN:
        return code
    try:
        c = escape[1:2]
        if c == b'x':
            while source.next in HEXDIGITS and len(escape) < 4:
                escape = escape + source.get()

            escape = escape[2:]
            if len(escape) != 2:
                raise error, b'bogus escape: %s' % repr(b'\\' + escape)
            return (LITERAL, int(escape, 16) & 255)
        if c in OCTDIGITS:
            while source.next in OCTDIGITS and len(escape) < 4:
                escape = escape + source.get()

            escape = escape[1:]
            return (
             LITERAL, int(escape, 8) & 255)
        if c in DIGITS:
            raise error, b'bogus escape: %s' % repr(escape)
        if len(escape) == 2:
            if sys.py3kwarning and c in ASCIILETTERS:
                import warnings
                if c in b'Uu':
                    warnings.warn(b'bad escape %s; Unicode escapes are supported only since Python 3.3' % escape, FutureWarning, stacklevel=nested + 6)
                else:
                    warnings.warnpy3k(b'bad escape %s' % escape, DeprecationWarning, stacklevel=nested + 6)
            return (
             LITERAL, ord(escape[1]))
    except ValueError:
        pass

    raise error, b'bogus escape: %s' % repr(escape)
    return


def _escape(source, escape, state, nested):
    code = CATEGORIES.get(escape)
    if code:
        return code
    code = ESCAPES.get(escape)
    if code:
        return code
    try:
        c = escape[1:2]
        if c == b'x':
            while source.next in HEXDIGITS and len(escape) < 4:
                escape = escape + source.get()

            if len(escape) != 4:
                raise ValueError
            return (LITERAL, int(escape[2:], 16) & 255)
        if c == b'0':
            while source.next in OCTDIGITS and len(escape) < 4:
                escape = escape + source.get()

            return (LITERAL, int(escape[1:], 8) & 255)
        if c in DIGITS:
            if source.next in DIGITS:
                escape = escape + source.get()
                if escape[1] in OCTDIGITS and escape[2] in OCTDIGITS and source.next in OCTDIGITS:
                    escape = escape + source.get()
                    return (
                     LITERAL, int(escape[1:], 8) & 255)
            group = int(escape[1:])
            if group < state.groups:
                if not state.checkgroup(group):
                    raise error, b'cannot refer to open group'
                if state.lookbehind:
                    import warnings
                    warnings.warn(b'group references in lookbehind assertions are not supported', RuntimeWarning, stacklevel=nested + 6)
                return (GROUPREF, group)
            raise ValueError
        if len(escape) == 2:
            if sys.py3kwarning and c in ASCIILETTERS:
                import warnings
                if c in b'Uu':
                    warnings.warn(b'bad escape %s; Unicode escapes are supported only since Python 3.3' % escape, FutureWarning, stacklevel=nested + 6)
                else:
                    warnings.warnpy3k(b'bad escape %s' % escape, DeprecationWarning, stacklevel=nested + 6)
            return (
             LITERAL, ord(escape[1]))
    except ValueError:
        pass

    raise error, b'bogus escape: %s' % repr(escape)
    return


def _parse_sub(source, state, nested):
    items = []
    itemsappend = items.append
    sourcematch = source.match
    while 1:
        itemsappend(_parse(source, state, nested + 1))
        if sourcematch(b'|'):
            continue
        if not nested:
            break
        if not source.next or sourcematch(b')', 0):
            break
        else:
            raise error, b'pattern not properly closed'

    if len(items) == 1:
        return items[0]
    else:
        subpattern = SubPattern(state)
        subpatternappend = subpattern.append
        while 1:
            prefix = None
            for item in items:
                if not item:
                    break
                if prefix is None:
                    prefix = item[0]
                elif item[0] != prefix:
                    break
            else:
                for item in items:
                    del item[0]

                subpatternappend(prefix)
                continue

            break

        for item in items:
            if len(item) != 1 or item[0][0] != LITERAL:
                break
        else:
            set = []
            setappend = set.append
            for item in items:
                setappend(item[0])

            subpatternappend((IN, set))
            return subpattern

        subpattern.append((BRANCH, (None, items)))
        return subpattern


def _parse_sub_cond(source, state, condgroup, nested):
    item_yes = _parse(source, state, nested + 1)
    if source.match(b'|'):
        item_no = _parse(source, state, nested + 1)
        if source.match(b'|'):
            raise error, b'conditional backref with more than two branches'
    else:
        item_no = None
    if source.next and not source.match(b')', 0):
        raise error, b'pattern not properly closed'
    subpattern = SubPattern(state)
    subpattern.append((GROUPREF_EXISTS, (condgroup, item_yes, item_no)))
    return subpattern


_PATTERNENDERS = set(b'|)')
_ASSERTCHARS = set(b'=!<')
_LOOKBEHINDASSERTCHARS = set(b'=!')
_REPEATCODES = set([MIN_REPEAT, MAX_REPEAT])

def _parse(source, state, nested):
    subpattern = SubPattern(state)
    subpatternappend = subpattern.append
    sourceget = source.get
    sourcematch = source.match
    _len = len
    PATTERNENDERS = _PATTERNENDERS
    ASSERTCHARS = _ASSERTCHARS
    LOOKBEHINDASSERTCHARS = _LOOKBEHINDASSERTCHARS
    REPEATCODES = _REPEATCODES
    while 1:
        if source.next in PATTERNENDERS:
            break
        this = sourceget()
        if this is None:
            break
        if state.flags & SRE_FLAG_VERBOSE:
            if this in WHITESPACE:
                continue
            if this == b'#':
                while 1:
                    this = sourceget()
                    if this in (None, b'\n'):
                        break

                continue
        if this and this[0] not in SPECIAL_CHARS:
            subpatternappend((LITERAL, ord(this)))
        elif this == b'[':
            set = []
            setappend = set.append
            if sourcematch(b'^'):
                setappend((NEGATE, None))
            start = set[:]
            while 1:
                this = sourceget()
                if this == b']' and set != start:
                    break
                elif this and this[0] == b'\\':
                    code1 = _class_escape(source, this, nested + 1)
                elif this:
                    code1 = (
                     LITERAL, ord(this))
                else:
                    raise error, b'unexpected end of regular expression'
                if sourcematch(b'-'):
                    this = sourceget()
                    if this == b']':
                        if code1[0] is IN:
                            code1 = code1[1][0]
                        setappend(code1)
                        setappend((LITERAL, ord(b'-')))
                        break
                    elif this:
                        if this[0] == b'\\':
                            code2 = _class_escape(source, this, nested + 1)
                        else:
                            code2 = (
                             LITERAL, ord(this))
                        if code1[0] != LITERAL or code2[0] != LITERAL:
                            raise error, b'bad character range'
                        lo = code1[1]
                        hi = code2[1]
                        if hi < lo:
                            raise error, b'bad character range'
                        setappend((RANGE, (lo, hi)))
                    else:
                        raise error, b'unexpected end of regular expression'
                elif code1[0] is IN:
                    code1 = code1[1][0]
                setappend(code1)

            if _len(set) == 1 and set[0][0] is LITERAL:
                subpatternappend(set[0])
            elif _len(set) == 2 and set[0][0] is NEGATE and set[1][0] is LITERAL:
                subpatternappend((NOT_LITERAL, set[1][1]))
            else:
                subpatternappend((IN, set))
        elif this and this[0] in REPEAT_CHARS:
            if this == b'?':
                min, max = (0, 1)
            elif this == b'*':
                min, max = 0, MAXREPEAT
            elif this == b'+':
                min, max = 1, MAXREPEAT
            elif this == b'{':
                if source.next == b'}':
                    subpatternappend((LITERAL, ord(this)))
                    continue
                here = source.tell()
                min, max = 0, MAXREPEAT
                lo = hi = b''
                while source.next in DIGITS:
                    lo = lo + source.get()

                if sourcematch(b','):
                    while source.next in DIGITS:
                        hi = hi + sourceget()

                else:
                    hi = lo
                if not sourcematch(b'}'):
                    subpatternappend((LITERAL, ord(this)))
                    source.seek(here)
                    continue
                if lo:
                    min = int(lo)
                    if min >= MAXREPEAT:
                        raise OverflowError(b'the repetition number is too large')
                if hi:
                    max = int(hi)
                    if max >= MAXREPEAT:
                        raise OverflowError(b'the repetition number is too large')
                    if max < min:
                        raise error(b'bad repeat interval')
            else:
                raise error, b'not supported'
            if subpattern:
                item = subpattern[-1:]
            else:
                item = None
            if not item or _len(item) == 1 and item[0][0] == AT:
                raise error, b'nothing to repeat'
            if item[0][0] in REPEATCODES:
                raise error, b'multiple repeat'
            if sourcematch(b'?'):
                subpattern[-1] = (
                 MIN_REPEAT, (min, max, item))
            else:
                subpattern[-1] = (
                 MAX_REPEAT, (min, max, item))
        elif this == b'.':
            subpatternappend((ANY, None))
        elif this == b'(':
            group = 1
            name = None
            condgroup = None
            if sourcematch(b'?'):
                group = 0
                if sourcematch(b'P'):
                    if sourcematch(b'<'):
                        name = b''
                        while 1:
                            char = sourceget()
                            if char is None:
                                raise error, b'unterminated name'
                            if char == b'>':
                                break
                            name = name + char

                        group = 1
                        if not name:
                            raise error(b'missing group name')
                        if not isname(name):
                            raise error(b'bad character in group name %r' % name)
                    elif sourcematch(b'='):
                        name = b''
                        while 1:
                            char = sourceget()
                            if char is None:
                                raise error, b'unterminated name'
                            if char == b')':
                                break
                            name = name + char

                        if not name:
                            raise error(b'missing group name')
                        if not isname(name):
                            raise error(b'bad character in backref group name %r' % name)
                        gid = state.groupdict.get(name)
                        if gid is None:
                            msg = (b'unknown group name: {0!r}').format(name)
                            raise error(msg)
                        if state.lookbehind:
                            import warnings
                            warnings.warn(b'group references in lookbehind assertions are not supported', RuntimeWarning, stacklevel=nested + 6)
                        subpatternappend((GROUPREF, gid))
                        continue
                    else:
                        char = sourceget()
                        if char is None:
                            raise error, b'unexpected end of pattern'
                        raise error, b'unknown specifier: ?P%s' % char
                elif sourcematch(b':'):
                    group = 2
                elif sourcematch(b'#'):
                    while 1:
                        if source.next is None or source.next == b')':
                            break
                        sourceget()

                    if not sourcematch(b')'):
                        raise error, b'unbalanced parenthesis'
                    continue
                if source.next in ASSERTCHARS:
                    char = sourceget()
                    dir = 1
                    if char == b'<':
                        if source.next not in LOOKBEHINDASSERTCHARS:
                            raise error, b'syntax error'
                        dir = -1
                        char = sourceget()
                        state.lookbehind += 1
                    p = _parse_sub(source, state, nested + 1)
                    if dir < 0:
                        state.lookbehind -= 1
                    if not sourcematch(b')'):
                        raise error, b'unbalanced parenthesis'
                    if char == b'=':
                        subpatternappend((ASSERT, (dir, p)))
                    else:
                        subpatternappend((ASSERT_NOT, (dir, p)))
                    continue
                elif sourcematch(b'('):
                    condname = b''
                    while 1:
                        char = sourceget()
                        if char is None:
                            raise error, b'unterminated name'
                        if char == b')':
                            break
                        condname = condname + char

                    group = 2
                    if not condname:
                        raise error(b'missing group name')
                    if isname(condname):
                        condgroup = state.groupdict.get(condname)
                        if condgroup is None:
                            msg = (b'unknown group name: {0!r}').format(condname)
                            raise error(msg)
                    else:
                        try:
                            condgroup = int(condname)
                        except ValueError:
                            raise error, b'bad character in group name'

                    if state.lookbehind:
                        import warnings
                        warnings.warn(b'group references in lookbehind assertions are not supported', RuntimeWarning, stacklevel=nested + 6)
                elif source.next not in FLAGS:
                    raise error, b'unexpected end of pattern'
                while source.next in FLAGS:
                    state.flags = state.flags | FLAGS[sourceget()]

            if group:
                if group == 2:
                    group = None
                else:
                    group = state.opengroup(name)
                if condgroup:
                    p = _parse_sub_cond(source, state, condgroup, nested + 1)
                else:
                    p = _parse_sub(source, state, nested + 1)
                if not sourcematch(b')'):
                    raise error, b'unbalanced parenthesis'
                if group is not None:
                    state.closegroup(group)
                subpatternappend((SUBPATTERN, (group, p)))
            else:
                while 1:
                    char = sourceget()
                    if char is None:
                        raise error, b'unexpected end of pattern'
                    if char == b')':
                        break
                    raise error, b'unknown extension'

        elif this == b'^':
            subpatternappend((AT, AT_BEGINNING))
        elif this == b'$':
            subpattern.append((AT, AT_END))
        elif this and this[0] == b'\\':
            code = _escape(source, this, state, nested + 1)
            subpatternappend(code)
        else:
            raise error, b'parser error'

    return subpattern


def parse(str, flags=0, pattern=None):
    source = Tokenizer(str)
    if pattern is None:
        pattern = Pattern()
    pattern.flags = flags
    pattern.str = str
    p = _parse_sub(source, pattern, 0)
    if sys.py3kwarning and p.pattern.flags & SRE_FLAG_LOCALE and p.pattern.flags & SRE_FLAG_UNICODE:
        import warnings
        warnings.warnpy3k(b'LOCALE and UNICODE flags are incompatible', DeprecationWarning, stacklevel=5)
    tail = source.get()
    if tail == b')':
        raise error, b'unbalanced parenthesis'
    elif tail:
        raise error, b'bogus characters at end of regular expression'
    if not flags & SRE_FLAG_VERBOSE and p.pattern.flags & SRE_FLAG_VERBOSE:
        return parse(str, p.pattern.flags)
    else:
        if flags & SRE_FLAG_DEBUG:
            p.dump()
        return p


def parse_template(source, pattern):
    s = Tokenizer(source)
    sget = s.get
    p = []
    a = p.append

    def literal(literal, p=p, pappend=a):
        if p and p[-1][0] is LITERAL:
            p[-1] = (
             LITERAL, p[-1][1] + literal)
        else:
            pappend((LITERAL, literal))
        return

    sep = source[:0]
    if type(sep) is type(b''):
        makechar = chr
    else:
        makechar = unichr
    while 1:
        this = sget()
        if this is None:
            break
        if this and this[0] == b'\\':
            c = this[1:2]
            if c == b'g':
                name = b''
                if s.match(b'<'):
                    while 1:
                        char = sget()
                        if char is None:
                            raise error, b'unterminated group name'
                        if char == b'>':
                            break
                        name = name + char

                if not name:
                    raise error, b'missing group name'
                try:
                    index = int(name)
                    if index < 0:
                        raise error, b'negative group number'
                except ValueError:
                    if not isname(name):
                        raise error, b'bad character in group name'
                    try:
                        index = pattern.groupindex[name]
                    except KeyError:
                        msg = (b'unknown group name: {0!r}').format(name)
                        raise IndexError(msg)

                a((MARK, index))
            elif c == b'0':
                if s.next in OCTDIGITS:
                    this = this + sget()
                    if s.next in OCTDIGITS:
                        this = this + sget()
                literal(makechar(int(this[1:], 8) & 255))
            elif c in DIGITS:
                isoctal = False
                if s.next in DIGITS:
                    this = this + sget()
                    if c in OCTDIGITS and this[2] in OCTDIGITS and s.next in OCTDIGITS:
                        this = this + sget()
                        isoctal = True
                        literal(makechar(int(this[1:], 8) & 255))
                if not isoctal:
                    a((MARK, int(this[1:])))
            else:
                try:
                    this = makechar(ESCAPES[this][1])
                except KeyError:
                    if sys.py3kwarning and c in ASCIILETTERS:
                        import warnings
                        warnings.warnpy3k(b'bad escape %s' % this, DeprecationWarning, stacklevel=4)

                literal(this)
        else:
            literal(this)

    i = 0
    groups = []
    groupsappend = groups.append
    literals = [None] * len(p)
    for c, s in p:
        if c is MARK:
            groupsappend((i, s))
        else:
            literals[i] = s
        i = i + 1

    return (
     groups, literals)


def expand_template(template, match):
    g = match.group
    sep = match.string[:0]
    groups, literals = template
    literals = literals[:]
    try:
        for index, group in groups:
            literals[index] = s = g(group)
            if s is None:
                raise error, b'unmatched group'

    except IndexError:
        raise error, b'invalid group reference'

    return sep.join(literals)
