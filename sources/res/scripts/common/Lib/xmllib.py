import re, string, warnings
warnings.warn(b'The xmllib module is obsolete.  Use xml.sax instead.', DeprecationWarning, 2)
del warnings
version = b'0.3'

class Error(RuntimeError):
    pass


_S = b'[ \t\r\n]+'
_opS = b'[ \t\r\n]*'
_Name = b'[a-zA-Z_:][-a-zA-Z0-9._:]*'
_QStr = b'(?:\'[^\']*\'|"[^"]*")'
illegal = re.compile(b'[^\t\r\n -~\xa0-\xff]')
interesting = re.compile(b'[]&<]')
amp = re.compile(b'&')
ref = re.compile(b'&(' + _Name + b'|#[0-9]+|#x[0-9a-fA-F]+)[^-a-zA-Z0-9._:]')
entityref = re.compile(b'&(?P<name>' + _Name + b')[^-a-zA-Z0-9._:]')
charref = re.compile(b'&#(?P<char>[0-9]+[^0-9]|x[0-9a-fA-F]+[^0-9a-fA-F])')
space = re.compile(_S + b'$')
newline = re.compile(b'\n')
attrfind = re.compile(_S + b'(?P<name>' + _Name + b')(' + _opS + b'=' + _opS + b'(?P<value>' + _QStr + b'|[-a-zA-Z0-9.:+*%?!\\(\\)_#=~]+))?')
starttagopen = re.compile(b'<' + _Name)
starttagend = re.compile(_opS + b'(?P<slash>/?)>')
starttagmatch = re.compile(b'<(?P<tagname>' + _Name + b')(?P<attrs>(?:' + attrfind.pattern + b')*)' + starttagend.pattern)
endtagopen = re.compile(b'</')
endbracket = re.compile(_opS + b'>')
endbracketfind = re.compile(b'(?:[^>\'"]|' + _QStr + b')*>')
tagfind = re.compile(_Name)
cdataopen = re.compile(b'<!\\[CDATA\\[')
cdataclose = re.compile(b'\\]\\]>')
_SystemLiteral = b'(?P<%s>' + _QStr + b')'
_PublicLiteral = b'(?P<%s>"[-\'\\(\\)+,./:=?;!*#@$_%% \n\ra-zA-Z0-9]*"|\'[-\\(\\)+,./:=?;!*#@$_%% \n\ra-zA-Z0-9]*\')'
_ExternalId = b'(?:SYSTEM|PUBLIC' + _S + _PublicLiteral % b'pubid' + b')' + _S + _SystemLiteral % b'syslit'
doctype = re.compile(b'<!DOCTYPE' + _S + b'(?P<name>' + _Name + b')(?:' + _S + _ExternalId + b')?' + _opS)
xmldecl = re.compile(b'<\\?xml' + _S + b'version' + _opS + b'=' + _opS + b'(?P<version>' + _QStr + b')' + b'(?:' + _S + b'encoding' + _opS + b'=' + _opS + b'(?P<encoding>\'[A-Za-z][-A-Za-z0-9._]*\'|"[A-Za-z][-A-Za-z0-9._]*"))?(?:' + _S + b'standalone' + _opS + b'=' + _opS + b'(?P<standalone>\'(?:yes|no)\'|"(?:yes|no)"))?' + _opS + b'\\?>')
procopen = re.compile(b'<\\?(?P<proc>' + _Name + b')' + _opS)
procclose = re.compile(_opS + b'\\?>')
commentopen = re.compile(b'<!--')
commentclose = re.compile(b'-->')
doubledash = re.compile(b'--')
attrtrans = string.maketrans(b' \r\n\t', b'    ')
_NCName = b'[a-zA-Z_][-a-zA-Z0-9._]*'
ncname = re.compile(_NCName + b'$')
qname = re.compile(b'(?:(?P<prefix>' + _NCName + b'):)?(?P<local>' + _NCName + b')$')
xmlns = re.compile(b'xmlns(?::(?P<ncname>' + _NCName + b'))?$')

class XMLParser():
    attributes = {}
    elements = {}
    __accept_unquoted_attributes = 0
    __accept_missing_endtag_name = 0
    __map_case = 0
    __accept_utf8 = 0
    __translate_attribute_references = 1

    def __init__(self, **kw):
        self.__fixed = 0
        if b'accept_unquoted_attributes' in kw:
            self.__accept_unquoted_attributes = kw[b'accept_unquoted_attributes']
        if b'accept_missing_endtag_name' in kw:
            self.__accept_missing_endtag_name = kw[b'accept_missing_endtag_name']
        if b'map_case' in kw:
            self.__map_case = kw[b'map_case']
        if b'accept_utf8' in kw:
            self.__accept_utf8 = kw[b'accept_utf8']
        if b'translate_attribute_references' in kw:
            self.__translate_attribute_references = kw[b'translate_attribute_references']
        self.reset()
        return

    def __fixelements(self):
        self.__fixed = 1
        self.elements = {}
        self.__fixdict(self.__dict__)
        self.__fixclass(self.__class__)
        return

    def __fixclass(self, kl):
        self.__fixdict(kl.__dict__)
        for k in kl.__bases__:
            self.__fixclass(k)

        return

    def __fixdict(self, dict):
        for key in dict.keys():
            if key[:6] == b'start_':
                tag = key[6:]
                start, end = self.elements.get(tag, (None, None))
                if start is None:
                    self.elements[tag] = (
                     getattr(self, key), end)
            elif key[:4] == b'end_':
                tag = key[4:]
                start, end = self.elements.get(tag, (None, None))
                if end is None:
                    self.elements[tag] = (
                     start, getattr(self, key))

        return

    def reset(self):
        self.rawdata = b''
        self.stack = []
        self.nomoretags = 0
        self.literal = 0
        self.lineno = 1
        self.__at_start = 1
        self.__seen_doctype = None
        self.__seen_starttag = 0
        self.__use_namespaces = 0
        self.__namespaces = {b'xml': None}
        if self.elements is XMLParser.elements:
            self.__fixelements()
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
        if self.__fixed:
            self.__fixed = 0
            del self.elements
        return

    def translate_references(self, data, all=1):
        if not self.__translate_attribute_references:
            return data
        else:
            i = 0
            while 1:
                res = amp.search(data, i)
                if res is None:
                    return data
                s = res.start(0)
                res = ref.match(data, s)
                if res is None:
                    self.syntax_error(b"bogus `&'")
                    i = s + 1
                    continue
                i = res.end(0)
                str = res.group(1)
                rescan = 0
                if str[0] == b'#':
                    if str[1] == b'x':
                        str = chr(int(str[2:], 16))
                    else:
                        str = chr(int(str[1:]))
                    if data[i - 1] != b';':
                        self.syntax_error(b"`;' missing after char reference")
                        i = i - 1
                elif all:
                    if str in self.entitydefs:
                        str = self.entitydefs[str]
                        rescan = 1
                    elif data[i - 1] != b';':
                        self.syntax_error(b"bogus `&'")
                        i = s + 1
                        continue
                    else:
                        self.syntax_error(b"reference to unknown entity `&%s;'" % str)
                        str = b'&' + str + b';'
                elif data[i - 1] != b';':
                    self.syntax_error(b"bogus `&'")
                    i = s + 1
                    continue
                data = data[:s] + str + data[i:]
                if rescan:
                    i = s
                else:
                    i = s + len(str)

            return

    def getnamespace(self):
        nsdict = {}
        for t, d, nst in self.stack:
            nsdict.update(d)

        return nsdict

    def goahead(self, end):
        rawdata = self.rawdata
        i = 0
        n = len(rawdata)
        while i < n:
            if i > 0:
                self.__at_start = 0
            if self.nomoretags:
                data = rawdata[i:n]
                self.handle_data(data)
                self.lineno = self.lineno + data.count(b'\n')
                i = n
                break
            res = interesting.search(rawdata, i)
            if res:
                j = res.start(0)
            else:
                j = n
            if i < j:
                data = rawdata[i:j]
                if self.__at_start and space.match(data) is None:
                    self.syntax_error(b'illegal data at start of file')
                self.__at_start = 0
                if not self.stack and space.match(data) is None:
                    self.syntax_error(b'data not in content')
                if not self.__accept_utf8 and illegal.search(data):
                    self.syntax_error(b'illegal character in content')
                self.handle_data(data)
                self.lineno = self.lineno + data.count(b'\n')
            i = j
            if i == n:
                break
            if rawdata[i] == b'<':
                if starttagopen.match(rawdata, i):
                    if self.literal:
                        data = rawdata[i]
                        self.handle_data(data)
                        self.lineno = self.lineno + data.count(b'\n')
                        i = i + 1
                        continue
                    k = self.parse_starttag(i)
                    if k < 0:
                        break
                    self.__seen_starttag = 1
                    self.lineno = self.lineno + rawdata[i:k].count(b'\n')
                    i = k
                    continue
                if endtagopen.match(rawdata, i):
                    k = self.parse_endtag(i)
                    if k < 0:
                        break
                    self.lineno = self.lineno + rawdata[i:k].count(b'\n')
                    i = k
                    continue
                if commentopen.match(rawdata, i):
                    if self.literal:
                        data = rawdata[i]
                        self.handle_data(data)
                        self.lineno = self.lineno + data.count(b'\n')
                        i = i + 1
                        continue
                    k = self.parse_comment(i)
                    if k < 0:
                        break
                    self.lineno = self.lineno + rawdata[i:k].count(b'\n')
                    i = k
                    continue
                if cdataopen.match(rawdata, i):
                    k = self.parse_cdata(i)
                    if k < 0:
                        break
                    self.lineno = self.lineno + rawdata[i:k].count(b'\n')
                    i = k
                    continue
                res = xmldecl.match(rawdata, i)
                if res:
                    if not self.__at_start:
                        self.syntax_error(b'<?xml?> declaration not at start of document')
                    version, encoding, standalone = res.group(b'version', b'encoding', b'standalone')
                    if version[1:-1] != b'1.0':
                        raise Error(b'only XML version 1.0 supported')
                    if encoding:
                        encoding = encoding[1:-1]
                    if standalone:
                        standalone = standalone[1:-1]
                    self.handle_xml(encoding, standalone)
                    i = res.end(0)
                    continue
                res = procopen.match(rawdata, i)
                if res:
                    k = self.parse_proc(i)
                    if k < 0:
                        break
                    self.lineno = self.lineno + rawdata[i:k].count(b'\n')
                    i = k
                    continue
                res = doctype.match(rawdata, i)
                if res:
                    if self.literal:
                        data = rawdata[i]
                        self.handle_data(data)
                        self.lineno = self.lineno + data.count(b'\n')
                        i = i + 1
                        continue
                    if self.__seen_doctype:
                        self.syntax_error(b'multiple DOCTYPE elements')
                    if self.__seen_starttag:
                        self.syntax_error(b'DOCTYPE not at beginning of document')
                    k = self.parse_doctype(res)
                    if k < 0:
                        break
                    self.__seen_doctype = res.group(b'name')
                    if self.__map_case:
                        self.__seen_doctype = self.__seen_doctype.lower()
                    self.lineno = self.lineno + rawdata[i:k].count(b'\n')
                    i = k
                    continue
            elif rawdata[i] == b'&':
                if self.literal:
                    data = rawdata[i]
                    self.handle_data(data)
                    i = i + 1
                    continue
                res = charref.match(rawdata, i)
                if res is not None:
                    i = res.end(0)
                    if rawdata[i - 1] != b';':
                        self.syntax_error(b"`;' missing in charref")
                        i = i - 1
                    if not self.stack:
                        self.syntax_error(b'data not in content')
                    self.handle_charref(res.group(b'char')[:-1])
                    self.lineno = self.lineno + res.group(0).count(b'\n')
                    continue
                res = entityref.match(rawdata, i)
                if res is not None:
                    i = res.end(0)
                    if rawdata[i - 1] != b';':
                        self.syntax_error(b"`;' missing in entityref")
                        i = i - 1
                    name = res.group(b'name')
                    if self.__map_case:
                        name = name.lower()
                    if name in self.entitydefs:
                        self.rawdata = rawdata = rawdata[:res.start(0)] + self.entitydefs[name] + rawdata[i:]
                        n = len(rawdata)
                        i = res.start(0)
                    else:
                        self.unknown_entityref(name)
                    self.lineno = self.lineno + res.group(0).count(b'\n')
                    continue
            elif rawdata[i] == b']':
                if self.literal:
                    data = rawdata[i]
                    self.handle_data(data)
                    i = i + 1
                    continue
                if n - i < 3:
                    break
                if cdataclose.match(rawdata, i):
                    self.syntax_error(b"bogus `]]>'")
                self.handle_data(rawdata[i])
                i = i + 1
                continue
            else:
                raise Error(b'neither < nor & ??')
            break

        if i > 0:
            self.__at_start = 0
        if end and i < n:
            data = rawdata[i]
            self.syntax_error(b"bogus `%s'" % data)
            if not self.__accept_utf8 and illegal.search(data):
                self.syntax_error(b'illegal character in content')
            self.handle_data(data)
            self.lineno = self.lineno + data.count(b'\n')
            self.rawdata = rawdata[i + 1:]
            return self.goahead(end)
        else:
            self.rawdata = rawdata[i:]
            if end:
                if not self.__seen_starttag:
                    self.syntax_error(b'no elements in file')
                if self.stack:
                    self.syntax_error(b'missing end tags')
                    while self.stack:
                        self.finish_endtag(self.stack[-1][0])

            return

    def parse_comment(self, i):
        rawdata = self.rawdata
        if rawdata[i:i + 4] != b'<!--':
            raise Error(b'unexpected call to handle_comment')
        res = commentclose.search(rawdata, i + 4)
        if res is None:
            return -1
        else:
            if doubledash.search(rawdata, i + 4, res.start(0)):
                self.syntax_error(b"`--' inside comment")
            if rawdata[res.start(0) - 1] == b'-':
                self.syntax_error(b'comment cannot end in three dashes')
            if not self.__accept_utf8 and illegal.search(rawdata, i + 4, res.start(0)):
                self.syntax_error(b'illegal character in comment')
            self.handle_comment(rawdata[i + 4:res.start(0)])
            return res.end(0)

    def parse_doctype(self, res):
        rawdata = self.rawdata
        n = len(rawdata)
        name = res.group(b'name')
        if self.__map_case:
            name = name.lower()
        pubid, syslit = res.group(b'pubid', b'syslit')
        if pubid is not None:
            pubid = pubid[1:-1]
            pubid = (b' ').join(pubid.split())
        if syslit is not None:
            syslit = syslit[1:-1]
        j = k = res.end(0)
        if k >= n:
            return -1
        else:
            if rawdata[k] == b'[':
                level = 0
                k = k + 1
                dq = sq = 0
                while k < n:
                    c = rawdata[k]
                    if not sq and c == b'"':
                        dq = not dq
                    elif not dq and c == b"'":
                        sq = not sq
                    elif sq or dq:
                        pass
                    elif level <= 0 and c == b']':
                        res = endbracket.match(rawdata, k + 1)
                        if res is None:
                            return -1
                        self.handle_doctype(name, pubid, syslit, rawdata[j + 1:k])
                        return res.end(0)
                    if c == b'<':
                        level = level + 1
                    elif c == b'>':
                        level = level - 1
                        if level < 0:
                            self.syntax_error(b"bogus `>' in DOCTYPE")
                    k = k + 1

            res = endbracketfind.match(rawdata, k)
            if res is None:
                return -1
            if endbracket.match(rawdata, k) is None:
                self.syntax_error(b'garbage in DOCTYPE')
            self.handle_doctype(name, pubid, syslit, None)
            return res.end(0)

    def parse_cdata(self, i):
        rawdata = self.rawdata
        if rawdata[i:i + 9] != b'<![CDATA[':
            raise Error(b'unexpected call to parse_cdata')
        res = cdataclose.search(rawdata, i + 9)
        if res is None:
            return -1
        else:
            if not self.__accept_utf8 and illegal.search(rawdata, i + 9, res.start(0)):
                self.syntax_error(b'illegal character in CDATA')
            if not self.stack:
                self.syntax_error(b'CDATA not in content')
            self.handle_cdata(rawdata[i + 9:res.start(0)])
            return res.end(0)

    __xml_namespace_attributes = {b'ns': None, b'src': None, b'prefix': None}

    def parse_proc(self, i):
        rawdata = self.rawdata
        end = procclose.search(rawdata, i)
        if end is None:
            return -1
        else:
            j = end.start(0)
            if not self.__accept_utf8 and illegal.search(rawdata, i + 2, j):
                self.syntax_error(b'illegal character in processing instruction')
            res = tagfind.match(rawdata, i + 2)
            if res is None:
                raise Error(b'unexpected call to parse_proc')
            k = res.end(0)
            name = res.group(0)
            if self.__map_case:
                name = name.lower()
            if name == b'xml:namespace':
                self.syntax_error(b'old-fashioned namespace declaration')
                self.__use_namespaces = -1
                if self.__seen_doctype or self.__seen_starttag:
                    self.syntax_error(b'xml:namespace declaration too late in document')
                attrdict, namespace, k = self.parse_attributes(name, k, j)
                if namespace:
                    self.syntax_error(b'namespace declaration inside namespace declaration')
                for attrname in attrdict.keys():
                    if attrname not in self.__xml_namespace_attributes:
                        self.syntax_error(b"unknown attribute `%s' in xml:namespace tag" % attrname)

                if b'ns' not in attrdict or b'prefix' not in attrdict:
                    self.syntax_error(b'xml:namespace without required attributes')
                prefix = attrdict.get(b'prefix')
                if ncname.match(prefix) is None:
                    self.syntax_error(b'xml:namespace illegal prefix value')
                    return end.end(0)
                if prefix in self.__namespaces:
                    self.syntax_error(b'xml:namespace prefix not unique')
                self.__namespaces[prefix] = attrdict[b'ns']
            elif name.lower() == b'xml':
                self.syntax_error(b'illegal processing instruction target name')
            self.handle_proc(name, rawdata[k:j])
            return end.end(0)

    def parse_attributes(self, tag, i, j):
        rawdata = self.rawdata
        attrdict = {}
        namespace = {}
        while i < j:
            res = attrfind.match(rawdata, i)
            if res is None:
                break
            attrname, attrvalue = res.group(b'name', b'value')
            if self.__map_case:
                attrname = attrname.lower()
            i = res.end(0)
            if attrvalue is None:
                self.syntax_error(b"no value specified for attribute `%s'" % attrname)
                attrvalue = attrname
            elif attrvalue[:1] == b"'" == attrvalue[-1:] or attrvalue[:1] == b'"' == attrvalue[-1:]:
                attrvalue = attrvalue[1:-1]
            elif not self.__accept_unquoted_attributes:
                self.syntax_error(b"attribute `%s' value not quoted" % attrname)
            res = xmlns.match(attrname)
            if res is not None:
                ncname = res.group(b'ncname')
                namespace[ncname or b''] = attrvalue or None
                if not self.__use_namespaces:
                    self.__use_namespaces = len(self.stack) + 1
                continue
            if b'<' in attrvalue:
                self.syntax_error(b"`<' illegal in attribute value")
            if attrname in attrdict:
                self.syntax_error(b"attribute `%s' specified twice" % attrname)
            attrvalue = attrvalue.translate(attrtrans)
            attrdict[attrname] = self.translate_references(attrvalue)

        return (
         attrdict, namespace, i)

    def parse_starttag(self, i):
        rawdata = self.rawdata
        end = endbracketfind.match(rawdata, i + 1)
        if end is None:
            return -1
        else:
            tag = starttagmatch.match(rawdata, i)
            if tag is None or tag.end(0) != end.end(0):
                self.syntax_error(b'garbage in starttag')
                return end.end(0)
            nstag = tagname = tag.group(b'tagname')
            if self.__map_case:
                nstag = tagname = nstag.lower()
            if not self.__seen_starttag and self.__seen_doctype and tagname != self.__seen_doctype:
                self.syntax_error(b'starttag does not match DOCTYPE')
            if self.__seen_starttag and not self.stack:
                self.syntax_error(b'multiple elements on top level')
            k, j = tag.span(b'attrs')
            attrdict, nsdict, k = self.parse_attributes(tagname, k, j)
            self.stack.append((tagname, nsdict, nstag))
            if self.__use_namespaces:
                res = qname.match(tagname)
            else:
                res = None
            if res is not None:
                prefix, nstag = res.group(b'prefix', b'local')
                if prefix is None:
                    prefix = b''
                ns = None
                for t, d, nst in self.stack:
                    if prefix in d:
                        ns = d[prefix]

                if ns is None and prefix != b'':
                    ns = self.__namespaces.get(prefix)
                if ns is not None:
                    nstag = ns + b' ' + nstag
                elif prefix != b'':
                    nstag = prefix + b':' + nstag
                self.stack[-1] = (
                 tagname, nsdict, nstag)
            attrnamemap = {}
            for key in attrdict.keys():
                attrnamemap[key] = key

            if self.__use_namespaces:
                nattrdict = {}
                for key, val in attrdict.items():
                    okey = key
                    res = qname.match(key)
                    if res is not None:
                        aprefix, key = res.group(b'prefix', b'local')
                        if self.__map_case:
                            key = key.lower()
                        if aprefix is not None:
                            ans = None
                            for t, d, nst in self.stack:
                                if aprefix in d:
                                    ans = d[aprefix]

                            if ans is None:
                                ans = self.__namespaces.get(aprefix)
                            if ans is not None:
                                key = ans + b' ' + key
                            else:
                                key = aprefix + b':' + key
                    nattrdict[key] = val
                    attrnamemap[key] = okey

                attrdict = nattrdict
            attributes = self.attributes.get(nstag)
            if attributes is not None:
                for key in attrdict.keys():
                    if key not in attributes:
                        self.syntax_error(b"unknown attribute `%s' in tag `%s'" % (attrnamemap[key], tagname))

                for key, val in attributes.items():
                    if val is not None and key not in attrdict:
                        attrdict[key] = val

            method = self.elements.get(nstag, (None, None))[0]
            self.finish_starttag(nstag, attrdict, method)
            if tag.group(b'slash') == b'/':
                self.finish_endtag(tagname)
            return tag.end(0)

    def parse_endtag(self, i):
        rawdata = self.rawdata
        end = endbracketfind.match(rawdata, i + 1)
        if end is None:
            return -1
        else:
            res = tagfind.match(rawdata, i + 2)
            if res is None:
                if self.literal:
                    self.handle_data(rawdata[i])
                    return i + 1
                if not self.__accept_missing_endtag_name:
                    self.syntax_error(b'no name specified in end tag')
                tag = self.stack[-1][0]
                k = i + 2
            else:
                tag = res.group(0)
                if self.__map_case:
                    tag = tag.lower()
                if self.literal:
                    if not self.stack or tag != self.stack[-1][0]:
                        self.handle_data(rawdata[i])
                        return i + 1
                k = res.end(0)
            if endbracket.match(rawdata, k) is None:
                self.syntax_error(b'garbage in end tag')
            self.finish_endtag(tag)
            return end.end(0)

    def finish_starttag(self, tagname, attrdict, method):
        if method is not None:
            self.handle_starttag(tagname, method, attrdict)
        else:
            self.unknown_starttag(tagname, attrdict)
        return

    def finish_endtag(self, tag):
        self.literal = 0
        if not tag:
            self.syntax_error(b'name-less end tag')
            found = len(self.stack) - 1
            if found < 0:
                self.unknown_endtag(tag)
                return
        else:
            found = -1
            for i in range(len(self.stack)):
                if tag == self.stack[i][0]:
                    found = i

            if found == -1:
                self.syntax_error(b'unopened end tag')
                return
        while len(self.stack) > found:
            if found < len(self.stack) - 1:
                self.syntax_error(b'missing close tag for %s' % self.stack[-1][2])
            nstag = self.stack[-1][2]
            method = self.elements.get(nstag, (None, None))[1]
            if method is not None:
                self.handle_endtag(nstag, method)
            else:
                self.unknown_endtag(nstag)
            if self.__use_namespaces == len(self.stack):
                self.__use_namespaces = 0
            del self.stack[-1]

        return

    def handle_xml(self, encoding, standalone):
        return

    def handle_doctype(self, tag, pubid, syslit, data):
        return

    def handle_starttag(self, tag, method, attrs):
        method(attrs)
        return

    def handle_endtag(self, tag, method):
        method()
        return

    def handle_charref(self, name):
        try:
            if name[0] == b'x':
                n = int(name[1:], 16)
            else:
                n = int(name)
        except ValueError:
            self.unknown_charref(name)
            return

        if not 0 <= n <= 255:
            self.unknown_charref(name)
            return
        self.handle_data(chr(n))
        return

    entitydefs = {b'lt': b'&#60;', b'gt': b'&#62;', 
       b'amp': b'&#38;', 
       b'quot': b'&#34;', 
       b'apos': b'&#39;'}

    def handle_data(self, data):
        return

    def handle_cdata(self, data):
        return

    def handle_comment(self, data):
        return

    def handle_proc(self, name, data):
        return

    def syntax_error(self, message):
        raise Error(b'Syntax error at line %d: %s' % (self.lineno, message))
        return

    def unknown_starttag(self, tag, attrs):
        return

    def unknown_endtag(self, tag):
        return

    def unknown_charref(self, ref):
        return

    def unknown_entityref(self, name):
        self.syntax_error(b"reference to unknown entity `&%s;'" % name)
        return


class TestXMLParser(XMLParser):

    def __init__(self, **kw):
        self.testdata = b''
        XMLParser.__init__(self, **kw)
        return

    def handle_xml(self, encoding, standalone):
        self.flush()
        print b'xml: encoding =', encoding, b'standalone =', standalone
        return

    def handle_doctype(self, tag, pubid, syslit, data):
        self.flush()
        print b'DOCTYPE:', tag, repr(data)
        return

    def handle_data(self, data):
        self.testdata = self.testdata + data
        if len(repr(self.testdata)) >= 70:
            self.flush()
        return

    def flush(self):
        data = self.testdata
        if data:
            self.testdata = b''
            print b'data:', repr(data)
        return

    def handle_cdata(self, data):
        self.flush()
        print b'cdata:', repr(data)
        return

    def handle_proc(self, name, data):
        self.flush()
        print b'processing:', name, repr(data)
        return

    def handle_comment(self, data):
        self.flush()
        r = repr(data)
        if len(r) > 68:
            r = r[:32] + b'...' + r[-32:]
        print b'comment:', r
        return

    def syntax_error(self, message):
        print b'error at line %d:' % self.lineno, message
        return

    def unknown_starttag(self, tag, attrs):
        self.flush()
        if not attrs:
            print b'start tag: <' + tag + b'>'
        else:
            print b'start tag: <' + tag,
            for name, value in attrs.items():
                print name + b'=' + b'"' + value + b'"',

            print b'>'
        return

    def unknown_endtag(self, tag):
        self.flush()
        print b'end tag: </' + tag + b'>'
        return

    def unknown_entityref(self, ref):
        self.flush()
        print b'*** unknown entity ref: &' + ref + b';'
        return

    def unknown_charref(self, ref):
        self.flush()
        print b'*** unknown char ref: &#' + ref + b';'
        return

    def close(self):
        XMLParser.close(self)
        self.flush()
        return


def test(args=None):
    import sys, getopt
    from time import time
    if not args:
        args = sys.argv[1:]
    opts, args = getopt.getopt(args, b'st')
    klass = TestXMLParser
    do_time = 0
    for o, a in opts:
        if o == b'-s':
            klass = XMLParser
        elif o == b'-t':
            do_time = 1

    if args:
        file = args[0]
    else:
        file = b'test.xml'
    if file == b'-':
        f = sys.stdin
    else:
        try:
            f = open(file, b'r')
        except IOError as msg:
            print file, b':', msg
            sys.exit(1)

    data = f.read()
    if f is not sys.stdin:
        f.close()
    x = klass()
    t0 = time()
    try:
        if do_time:
            x.feed(data)
            x.close()
        else:
            for c in data:
                x.feed(c)

            x.close()
    except Error as msg:
        t1 = time()
        print msg
        if do_time:
            print b'total time: %g' % (t1 - t0)
        sys.exit(1)

    t1 = time()
    if do_time:
        print b'total time: %g' % (t1 - t0)
    return


if __name__ == b'__main__':
    test()
