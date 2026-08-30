import _markupbase, re
__all__ = [
 b'SGMLParser', b'SGMLParseError']
interesting = re.compile(b'[&<]')
incomplete = re.compile(b'&([a-zA-Z][a-zA-Z0-9]*|#[0-9]*)?|<([a-zA-Z][^<>]*|/([a-zA-Z][^<>]*)?|![^<>]*)?')
entityref = re.compile(b'&([a-zA-Z][-.a-zA-Z0-9]*)[^a-zA-Z0-9]')
charref = re.compile(b'&#([0-9]+)[^0-9]')
starttagopen = re.compile(b'<[>a-zA-Z]')
shorttagopen = re.compile(b'<[a-zA-Z][-.a-zA-Z0-9]*/')
shorttag = re.compile(b'<([a-zA-Z][-.a-zA-Z0-9]*)/([^/]*)/')
piclose = re.compile(b'>')
endbracket = re.compile(b'[<>]')
tagfind = re.compile(b'[a-zA-Z][-_.a-zA-Z0-9]*')
attrfind = re.compile(b'\\s*([a-zA-Z_][-:.a-zA-Z_0-9]*)(\\s*=\\s*(\\\'[^\\\']*\\\'|"[^"]*"|[][\\-a-zA-Z0-9./,:;+*%?!&$\\(\\)_#=~\\\'"@]*))?')

class SGMLParseError(RuntimeError):
    pass


class SGMLParser(_markupbase.ParserBase):
    entity_or_charref = re.compile(b'&(?:([a-zA-Z][-.a-zA-Z0-9]*)|#([0-9]+))(;?)')

    def __init__(self, verbose=0):
        self.verbose = verbose
        self.reset()
        return

    def reset(self):
        self.__starttag_text = None
        self.rawdata = b''
        self.stack = []
        self.lasttag = b'???'
        self.nomoretags = 0
        self.literal = 0
        _markupbase.ParserBase.reset(self)
        return

    def setnomoretags(self):
        self.nomoretags = self.literal = 1
        return

    def setliteral(self, *args):
        self.literal = 1
        return

    def feed(self, data):
        self.rawdata = self.rawdata + data
        self.goahead(0)
        return

    def close(self):
        self.goahead(1)
        return

    def error(self, message):
        raise SGMLParseError(message)
        return

    def goahead(self, end):
        rawdata = self.rawdata
        i = 0
        n = len(rawdata)
        while i < n:
            if self.nomoretags:
                self.handle_data(rawdata[i:n])
                i = n
                break
            match = interesting.search(rawdata, i)
            if match:
                j = match.start()
            else:
                j = n
            if i < j:
                self.handle_data(rawdata[i:j])
            i = j
            if i == n:
                break
            if rawdata[i] == b'<':
                if starttagopen.match(rawdata, i):
                    if self.literal:
                        self.handle_data(rawdata[i])
                        i = i + 1
                        continue
                    k = self.parse_starttag(i)
                    if k < 0:
                        break
                    i = k
                    continue
                if rawdata.startswith(b'</', i):
                    k = self.parse_endtag(i)
                    if k < 0:
                        break
                    i = k
                    self.literal = 0
                    continue
                if self.literal:
                    if n > i + 1:
                        self.handle_data(b'<')
                        i = i + 1
                    else:
                        break
                    continue
                if rawdata.startswith(b'<!--', i):
                    k = self.parse_comment(i)
                    if k < 0:
                        break
                    i = k
                    continue
                if rawdata.startswith(b'<?', i):
                    k = self.parse_pi(i)
                    if k < 0:
                        break
                    i = i + k
                    continue
                if rawdata.startswith(b'<!', i):
                    k = self.parse_declaration(i)
                    if k < 0:
                        break
                    i = k
                    continue
            elif rawdata[i] == b'&':
                if self.literal:
                    self.handle_data(rawdata[i])
                    i = i + 1
                    continue
                match = charref.match(rawdata, i)
                if match:
                    name = match.group(1)
                    self.handle_charref(name)
                    i = match.end(0)
                    if rawdata[i - 1] != b';':
                        i = i - 1
                    continue
                match = entityref.match(rawdata, i)
                if match:
                    name = match.group(1)
                    self.handle_entityref(name)
                    i = match.end(0)
                    if rawdata[i - 1] != b';':
                        i = i - 1
                    continue
            else:
                self.error(b'neither < nor & ??')
            match = incomplete.match(rawdata, i)
            if not match:
                self.handle_data(rawdata[i])
                i = i + 1
                continue
            j = match.end(0)
            if j == n:
                break
            self.handle_data(rawdata[i:j])
            i = j

        if end and i < n:
            self.handle_data(rawdata[i:n])
            i = n
        self.rawdata = rawdata[i:]
        return

    _decl_otherchars = b'='

    def parse_pi(self, i):
        rawdata = self.rawdata
        if rawdata[i:i + 2] != b'<?':
            self.error(b'unexpected call to parse_pi()')
        match = piclose.search(rawdata, i + 2)
        if not match:
            return -1
        j = match.start(0)
        self.handle_pi(rawdata[i + 2:j])
        j = match.end(0)
        return j - i

    def get_starttag_text(self):
        return self.__starttag_text

    def parse_starttag(self, i):
        self.__starttag_text = None
        start_pos = i
        rawdata = self.rawdata
        if shorttagopen.match(rawdata, i):
            match = shorttag.match(rawdata, i)
            if not match:
                return -1
            tag, data = match.group(1, 2)
            self.__starttag_text = b'<%s/' % tag
            tag = tag.lower()
            k = match.end(0)
            self.finish_shorttag(tag, data)
            self.__starttag_text = rawdata[start_pos:match.end(1) + 1]
            return k
        else:
            match = endbracket.search(rawdata, i + 1)
            if not match:
                return -1
            j = match.start(0)
            attrs = []
            if rawdata[i:i + 2] == b'<>':
                k = j
                tag = self.lasttag
            else:
                match = tagfind.match(rawdata, i + 1)
                if not match:
                    self.error(b'unexpected call to parse_starttag')
                k = match.end(0)
                tag = rawdata[i + 1:k].lower()
                self.lasttag = tag
            while k < j:
                match = attrfind.match(rawdata, k)
                if not match:
                    break
                attrname, rest, attrvalue = match.group(1, 2, 3)
                if not rest:
                    attrvalue = attrname
                elif attrvalue[:1] == b"'" == attrvalue[-1:] or attrvalue[:1] == b'"' == attrvalue[-1:]:
                    attrvalue = attrvalue[1:-1]
                attrvalue = self.entity_or_charref.sub(self._convert_ref, attrvalue)
                attrs.append((attrname.lower(), attrvalue))
                k = match.end(0)

            if rawdata[j] == b'>':
                j = j + 1
            self.__starttag_text = rawdata[start_pos:j]
            self.finish_starttag(tag, attrs)
            return j

    def _convert_ref(self, match):
        if match.group(2):
            return self.convert_charref(match.group(2)) or b'&#%s%s' % match.groups()[1:]
        else:
            if match.group(3):
                return self.convert_entityref(match.group(1)) or b'&%s;' % match.group(1)
            return b'&%s' % match.group(1)

        return

    def parse_endtag(self, i):
        rawdata = self.rawdata
        match = endbracket.search(rawdata, i + 1)
        if not match:
            return -1
        j = match.start(0)
        tag = rawdata[i + 2:j].strip().lower()
        if rawdata[j] == b'>':
            j = j + 1
        self.finish_endtag(tag)
        return j

    def finish_shorttag(self, tag, data):
        self.finish_starttag(tag, [])
        self.handle_data(data)
        self.finish_endtag(tag)
        return

    def finish_starttag(self, tag, attrs):
        try:
            method = getattr(self, b'start_' + tag)
        except AttributeError:
            try:
                method = getattr(self, b'do_' + tag)
            except AttributeError:
                self.unknown_starttag(tag, attrs)
                return -1

            self.handle_starttag(tag, method, attrs)
            return 0
        else:
            self.stack.append(tag)
            self.handle_starttag(tag, method, attrs)
            return 1

        return

    def finish_endtag(self, tag):
        if not tag:
            found = len(self.stack) - 1
            if found < 0:
                self.unknown_endtag(tag)
                return
        elif tag not in self.stack:
            try:
                method = getattr(self, b'end_' + tag)
            except AttributeError:
                self.unknown_endtag(tag)
            else:
                self.report_unbalanced(tag)

            return
        found = len(self.stack)
        for i in range(found):
            if self.stack[i] == tag:
                found = i

        while len(self.stack) > found:
            tag = self.stack[-1]
            try:
                method = getattr(self, b'end_' + tag)
            except AttributeError:
                method = None

            if method:
                self.handle_endtag(tag, method)
            else:
                self.unknown_endtag(tag)
            del self.stack[-1]

        return

    def handle_starttag(self, tag, method, attrs):
        method(attrs)
        return

    def handle_endtag(self, tag, method):
        method()
        return

    def report_unbalanced(self, tag):
        if self.verbose:
            print b'*** Unbalanced </' + tag + b'>'
            print (b'*** Stack:', self.stack)
        return

    def convert_charref(self, name):
        try:
            n = int(name)
        except ValueError:
            return

        if not 0 <= n <= 127:
            return
        return self.convert_codepoint(n)

    def convert_codepoint(self, codepoint):
        return chr(codepoint)

    def handle_charref(self, name):
        replacement = self.convert_charref(name)
        if replacement is None:
            self.unknown_charref(name)
        else:
            self.handle_data(replacement)
        return

    entitydefs = {b'lt': b'<', b'gt': b'>', b'amp': b'&', b'quot': b'"', b'apos': b"'"}

    def convert_entityref(self, name):
        table = self.entitydefs
        if name in table:
            return table[name]
        else:
            return

        return

    def handle_entityref(self, name):
        replacement = self.convert_entityref(name)
        if replacement is None:
            self.unknown_entityref(name)
        else:
            self.handle_data(replacement)
        return

    def handle_data(self, data):
        return

    def handle_comment(self, data):
        return

    def handle_decl(self, decl):
        return

    def handle_pi(self, data):
        return

    def unknown_starttag(self, tag, attrs):
        return

    def unknown_endtag(self, tag):
        return

    def unknown_charref(self, ref):
        return

    def unknown_entityref(self, ref):
        return
