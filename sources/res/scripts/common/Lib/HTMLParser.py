import markupbase, re
interesting_normal = re.compile(b'[&<]')
incomplete = re.compile(b'&[a-zA-Z#]')
entityref = re.compile(b'&([a-zA-Z][-.a-zA-Z0-9]*)[^a-zA-Z0-9]')
charref = re.compile(b'&#(?:[0-9]+|[xX][0-9a-fA-F]+)[^0-9a-fA-F]')
starttagopen = re.compile(b'<[a-zA-Z]')
piclose = re.compile(b'>')
commentclose = re.compile(b'--\\s*>')
tagfind = re.compile(b'([a-zA-Z][^\t\n\r\x0c />\x00]*)(?:\\s|/(?!>))*')
tagfind_tolerant = re.compile(b'[a-zA-Z][^\t\n\r\x0c />\x00]*')
attrfind = re.compile(b'((?<=[\\\'"\\s/])[^\\s/>][^\\s/=>]*)(\\s*=+\\s*(\\\'[^\\\']*\\\'|"[^"]*"|(?![\\\'"])[^>\\s]*))?(?:\\s|/(?!>))*')
locatestarttagend = re.compile(b'\n  <[a-zA-Z][^\\t\\n\\r\\f />\\x00]*       # tag name\n  (?:[\\s/]*                          # optional whitespace before attribute name\n    (?:(?<=[\'"\\s/])[^\\s/>][^\\s/=>]*  # attribute name\n      (?:\\s*=+\\s*                    # value indicator\n        (?:\'[^\']*\'                   # LITA-enclosed value\n          |"[^"]*"                   # LIT-enclosed value\n          |(?![\'"])[^>\\s]*           # bare value\n         )\n       )?(?:\\s|/(?!>))*\n     )*\n   )?\n  \\s*                                # trailing whitespace\n', re.VERBOSE)
endendtag = re.compile(b'>')
endtagfind = re.compile(b'</\\s*([a-zA-Z][-.a-zA-Z0-9:_]*)\\s*>')

class HTMLParseError(Exception):

    def __init__(self, msg, position=(None, None)):
        self.msg = msg
        self.lineno = position[0]
        self.offset = position[1]
        return

    def __str__(self):
        result = self.msg
        if self.lineno is not None:
            result = result + b', at line %d' % self.lineno
        if self.offset is not None:
            result = result + b', column %d' % (self.offset + 1)
        return result


class HTMLParser(markupbase.ParserBase):
    CDATA_CONTENT_ELEMENTS = (b'script', b'style')

    def __init__(self):
        self.reset()
        return

    def reset(self):
        self.rawdata = b''
        self.lasttag = b'???'
        self.interesting = interesting_normal
        self.cdata_elem = None
        markupbase.ParserBase.reset(self)
        return

    def feed(self, data):
        self.rawdata = self.rawdata + data
        self.goahead(0)
        return

    def close(self):
        self.goahead(1)
        return

    def error(self, message):
        raise HTMLParseError(message, self.getpos())
        return

    __starttag_text = None

    def get_starttag_text(self):
        return self.__starttag_text

    def set_cdata_mode(self, elem):
        self.cdata_elem = elem.lower()
        self.interesting = re.compile(b'</\\s*%s\\s*>' % self.cdata_elem, re.I)
        return

    def clear_cdata_mode(self):
        self.interesting = interesting_normal
        self.cdata_elem = None
        return

    def goahead(self, end):
        rawdata = self.rawdata
        i = 0
        n = len(rawdata)
        while i < n:
            match = self.interesting.search(rawdata, i)
            if match:
                j = match.start()
            elif self.cdata_elem:
                break
            j = n
            if i < j:
                self.handle_data(rawdata[i:j])
            i = self.updatepos(i, j)
            if i == n:
                break
            startswith = rawdata.startswith
            if startswith(b'<', i):
                if starttagopen.match(rawdata, i):
                    k = self.parse_starttag(i)
                elif startswith(b'</', i):
                    k = self.parse_endtag(i)
                elif startswith(b'<!--', i):
                    k = self.parse_comment(i)
                elif startswith(b'<?', i):
                    k = self.parse_pi(i)
                elif startswith(b'<!', i):
                    k = self.parse_html_declaration(i)
                elif i + 1 < n:
                    self.handle_data(b'<')
                    k = i + 1
                else:
                    break
                if k < 0:
                    if not end:
                        break
                    k = rawdata.find(b'>', i + 1)
                    if k < 0:
                        k = rawdata.find(b'<', i + 1)
                        if k < 0:
                            k = i + 1
                    else:
                        k += 1
                    self.handle_data(rawdata[i:k])
                i = self.updatepos(i, k)
            elif startswith(b'&#', i):
                match = charref.match(rawdata, i)
                if match:
                    name = match.group()[2:-1]
                    self.handle_charref(name)
                    k = match.end()
                    if not startswith(b';', k - 1):
                        k = k - 1
                    i = self.updatepos(i, k)
                    continue
                elif b';' in rawdata[i:]:
                    self.handle_data(rawdata[i:i + 2])
                    i = self.updatepos(i, i + 2)
                break
            elif startswith(b'&', i):
                match = entityref.match(rawdata, i)
                if match:
                    name = match.group(1)
                    self.handle_entityref(name)
                    k = match.end()
                    if not startswith(b';', k - 1):
                        k = k - 1
                    i = self.updatepos(i, k)
                    continue
                match = incomplete.match(rawdata, i)
                if match:
                    if end and match.group() == rawdata[i:]:
                        self.error(b'EOF in middle of entity or char ref')
                    break
                elif i + 1 < n:
                    self.handle_data(b'&')
                    i = self.updatepos(i, i + 1)
                else:
                    break

        if end and i < n and not self.cdata_elem:
            self.handle_data(rawdata[i:n])
            i = self.updatepos(i, n)
        self.rawdata = rawdata[i:]
        return

    def parse_html_declaration(self, i):
        rawdata = self.rawdata
        if rawdata[i:i + 2] != b'<!':
            self.error(b'unexpected call to parse_html_declaration()')
        if rawdata[i:i + 4] == b'<!--':
            return self.parse_comment(i)
        else:
            if rawdata[i:i + 3] == b'<![':
                return self.parse_marked_section(i)
            if rawdata[i:i + 9].lower() == b'<!doctype':
                gtpos = rawdata.find(b'>', i + 9)
                if gtpos == -1:
                    return -1
                self.handle_decl(rawdata[i + 2:gtpos])
                return gtpos + 1
            return self.parse_bogus_comment(i)

        return

    def parse_bogus_comment(self, i, report=1):
        rawdata = self.rawdata
        if rawdata[i:i + 2] not in (b'<!', b'</'):
            self.error(b'unexpected call to parse_comment()')
        pos = rawdata.find(b'>', i + 2)
        if pos == -1:
            return -1
        if report:
            self.handle_comment(rawdata[i + 2:pos])
        return pos + 1

    def parse_pi(self, i):
        rawdata = self.rawdata
        match = piclose.search(rawdata, i + 2)
        if not match:
            return -1
        j = match.start()
        self.handle_pi(rawdata[i + 2:j])
        j = match.end()
        return j

    def parse_starttag(self, i):
        self.__starttag_text = None
        endpos = self.check_for_whole_start_tag(i)
        if endpos < 0:
            return endpos
        else:
            rawdata = self.rawdata
            self.__starttag_text = rawdata[i:endpos]
            attrs = []
            match = tagfind.match(rawdata, i + 1)
            k = match.end()
            self.lasttag = tag = match.group(1).lower()
            while k < endpos:
                m = attrfind.match(rawdata, k)
                if not m:
                    break
                attrname, rest, attrvalue = m.group(1, 2, 3)
                if not rest:
                    attrvalue = None
                elif attrvalue[:1] == b"'" == attrvalue[-1:] or attrvalue[:1] == b'"' == attrvalue[-1:]:
                    attrvalue = attrvalue[1:-1]
                if attrvalue:
                    attrvalue = self.unescape(attrvalue)
                attrs.append((attrname.lower(), attrvalue))
                k = m.end()

            end = rawdata[k:endpos].strip()
            if end not in (b'>', b'/>'):
                lineno, offset = self.getpos()
                if b'\n' in self.__starttag_text:
                    lineno = lineno + self.__starttag_text.count(b'\n')
                    offset = len(self.__starttag_text) - self.__starttag_text.rfind(b'\n')
                else:
                    offset = offset + len(self.__starttag_text)
                self.handle_data(rawdata[i:endpos])
                return endpos
            if end.endswith(b'/>'):
                self.handle_startendtag(tag, attrs)
            else:
                self.handle_starttag(tag, attrs)
                if tag in self.CDATA_CONTENT_ELEMENTS:
                    self.set_cdata_mode(tag)
            return endpos

    def check_for_whole_start_tag(self, i):
        rawdata = self.rawdata
        m = locatestarttagend.match(rawdata, i)
        if m:
            j = m.end()
            next = rawdata[j:j + 1]
            if next == b'>':
                return j + 1
            if next == b'/':
                if rawdata.startswith(b'/>', j):
                    return j + 2
                if rawdata.startswith(b'/', j):
                    return -1
                self.updatepos(i, j + 1)
                self.error(b'malformed empty start tag')
            if next == b'':
                return -1
            if next in b'abcdefghijklmnopqrstuvwxyz=/ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                return -1
            if j > i:
                return j
            return i + 1
        raise AssertionError(b'we should not get here!')
        return

    def parse_endtag(self, i):
        rawdata = self.rawdata
        match = endendtag.search(rawdata, i + 1)
        if not match:
            return -1
        else:
            gtpos = match.end()
            match = endtagfind.match(rawdata, i)
            if not match:
                if self.cdata_elem is not None:
                    self.handle_data(rawdata[i:gtpos])
                    return gtpos
                namematch = tagfind.match(rawdata, i + 2)
                if not namematch:
                    if rawdata[i:i + 3] == b'</>':
                        return i + 3
                    else:
                        return self.parse_bogus_comment(i)

                tagname = namematch.group(1).lower()
                gtpos = rawdata.find(b'>', namematch.end())
                self.handle_endtag(tagname)
                return gtpos + 1
            elem = match.group(1).lower()
            if self.cdata_elem is not None:
                if elem != self.cdata_elem:
                    self.handle_data(rawdata[i:gtpos])
                    return gtpos
            self.handle_endtag(elem)
            self.clear_cdata_mode()
            return gtpos

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)
        return

    def handle_starttag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        return

    def handle_charref(self, name):
        return

    def handle_entityref(self, name):
        return

    def handle_data(self, data):
        return

    def handle_comment(self, data):
        return

    def handle_decl(self, decl):
        return

    def handle_pi(self, data):
        return

    def unknown_decl(self, data):
        return

    entitydefs = None

    def unescape(self, s):
        if b'&' not in s:
            return s

        def replaceEntities(s):
            s = s.groups()[0]
            try:
                if s[0] == b'#':
                    s = s[1:]
                    if s[0] in (b'x', b'X'):
                        c = int(s[1:], 16)
                    else:
                        c = int(s)
                    return unichr(c)
            except ValueError:
                return b'&#' + s + b';'

            if HTMLParser.entitydefs is None:
                import htmlentitydefs
                entitydefs = {b'apos': u"'"}
                for k, v in htmlentitydefs.name2codepoint.iteritems():
                    entitydefs[k] = unichr(v)

                HTMLParser.entitydefs = entitydefs
            try:
                return self.entitydefs[s]
            except KeyError:
                return b'&' + s + b';'

            return

        return re.sub(b'&(#?[xX]?(?:[0-9a-fA-F]+|\\w{1,8}));', replaceEntities, s)
