__all__ = [
 b'FeedParser']
import re
from email import errors
from email import message
NLCRE = re.compile(b'\r\n|\r|\n')
NLCRE_bol = re.compile(b'(\r\n|\r|\n)')
NLCRE_eol = re.compile(b'(\r\n|\r|\n)\\Z')
NLCRE_crack = re.compile(b'(\r\n|\r|\n)')
headerRE = re.compile(b'^(From |[\\041-\\071\\073-\\176]{1,}:|[\\t ])')
EMPTYSTRING = b''
NL = b'\n'
NeedMoreData = object()

class BufferedSubFile(object):

    def __init__(self):
        self._partial = []
        self._lines = []
        self._eofstack = []
        self._closed = False
        return

    def push_eof_matcher(self, pred):
        self._eofstack.append(pred)
        return

    def pop_eof_matcher(self):
        return self._eofstack.pop()

    def close(self):
        self.pushlines((b'').join(self._partial).splitlines(True))
        self._partial = []
        self._closed = True
        return

    def readline(self):
        if not self._lines:
            if self._closed:
                return b''
            return NeedMoreData
        line = self._lines.pop()
        for ateof in self._eofstack[::-1]:
            if ateof(line):
                self._lines.append(line)
                return b''

        return line

    def unreadline(self, line):
        self._lines.append(line)
        return

    def push(self, data):
        parts = data.splitlines(True)
        if not parts or not parts[0].endswith((b'\n', b'\r')):
            self._partial += parts
            return
        if self._partial:
            self._partial.append(parts[0])
            parts[0:1] = (b'').join(self._partial).splitlines(True)
            del self._partial[:]
        if not parts[-1].endswith(b'\n'):
            self._partial = [
             parts.pop()]
        self.pushlines(parts)
        return

    def pushlines(self, lines):
        self._lines[:0] = lines[::-1]
        return

    def is_closed(self):
        return self._closed

    def __iter__(self):
        return self

    def next(self):
        line = self.readline()
        if line == b'':
            raise StopIteration
        return line


class FeedParser:

    def __init__(self, _factory=message.Message):
        self._factory = _factory
        self._input = BufferedSubFile()
        self._msgstack = []
        self._parse = self._parsegen().next
        self._cur = None
        self._last = None
        self._headersonly = False
        return

    def _set_headersonly(self):
        self._headersonly = True
        return

    def feed(self, data):
        self._input.push(data)
        self._call_parse()
        return

    def _call_parse(self):
        try:
            self._parse()
        except StopIteration:
            pass

        return

    def close(self):
        self._input.close()
        self._call_parse()
        root = self._pop_message()
        if root.get_content_maintype() == b'multipart' and not root.is_multipart():
            root.defects.append(errors.MultipartInvariantViolationDefect())
        return root

    def _new_message(self):
        msg = self._factory()
        if self._cur and self._cur.get_content_type() == b'multipart/digest':
            msg.set_default_type(b'message/rfc822')
        if self._msgstack:
            self._msgstack[-1].attach(msg)
        self._msgstack.append(msg)
        self._cur = msg
        self._last = msg
        return

    def _pop_message(self):
        retval = self._msgstack.pop()
        if self._msgstack:
            self._cur = self._msgstack[-1]
        else:
            self._cur = None
        return retval

    def _parsegen(self):
        self._new_message()
        headers = []
        for line in self._input:
            if line is NeedMoreData:
                yield NeedMoreData
                continue
            if not headerRE.match(line):
                if not NLCRE.match(line):
                    self._input.unreadline(line)
                break
            headers.append(line)

        self._parse_headers(headers)
        if self._headersonly:
            lines = []
            while True:
                line = self._input.readline()
                if line is NeedMoreData:
                    yield NeedMoreData
                    continue
                if line == b'':
                    break
                lines.append(line)

            self._cur.set_payload(EMPTYSTRING.join(lines))
            return
        else:
            if self._cur.get_content_type() == b'message/delivery-status':
                while True:
                    self._input.push_eof_matcher(NLCRE.match)
                    for retval in self._parsegen():
                        if retval is NeedMoreData:
                            yield NeedMoreData
                            continue
                        break

                    msg = self._pop_message()
                    self._input.pop_eof_matcher()
                    while True:
                        line = self._input.readline()
                        if line is NeedMoreData:
                            yield NeedMoreData
                            continue
                        break

                    while True:
                        line = self._input.readline()
                        if line is NeedMoreData:
                            yield NeedMoreData
                            continue
                        break

                    if line == b'':
                        break
                    self._input.unreadline(line)

                return
            if self._cur.get_content_maintype() == b'message':
                for retval in self._parsegen():
                    if retval is NeedMoreData:
                        yield NeedMoreData
                        continue
                    break

                self._pop_message()
                return
            if self._cur.get_content_maintype() == b'multipart':
                boundary = self._cur.get_boundary()
                if boundary is None:
                    self._cur.defects.append(errors.NoBoundaryInMultipartDefect())
                    lines = []
                    for line in self._input:
                        if line is NeedMoreData:
                            yield NeedMoreData
                            continue
                        lines.append(line)

                    self._cur.set_payload(EMPTYSTRING.join(lines))
                    return
                separator = b'--' + boundary
                boundaryre = re.compile(b'(?P<sep>' + re.escape(separator) + b')(?P<end>--)?(?P<ws>[ \\t]*)(?P<linesep>\\r\\n|\\r|\\n)?$')
                capturing_preamble = True
                preamble = []
                linesep = False
                while True:
                    line = self._input.readline()
                    if line is NeedMoreData:
                        yield NeedMoreData
                        continue
                    if line == b'':
                        break
                    mo = boundaryre.match(line)
                    if mo:
                        if mo.group(b'end'):
                            linesep = mo.group(b'linesep')
                            break
                        if capturing_preamble:
                            if preamble:
                                lastline = preamble[-1]
                                eolmo = NLCRE_eol.search(lastline)
                                if eolmo:
                                    preamble[-1] = lastline[:-len(eolmo.group(0))]
                                self._cur.preamble = EMPTYSTRING.join(preamble)
                            capturing_preamble = False
                            self._input.unreadline(line)
                            continue
                        while True:
                            line = self._input.readline()
                            if line is NeedMoreData:
                                yield NeedMoreData
                                continue
                            mo = boundaryre.match(line)
                            if not mo:
                                self._input.unreadline(line)
                                break

                        self._input.push_eof_matcher(boundaryre.match)
                        for retval in self._parsegen():
                            if retval is NeedMoreData:
                                yield NeedMoreData
                                continue
                            break

                        if self._last.get_content_maintype() == b'multipart':
                            epilogue = self._last.epilogue
                            if epilogue == b'':
                                self._last.epilogue = None
                            elif epilogue is not None:
                                mo = NLCRE_eol.search(epilogue)
                                if mo:
                                    end = len(mo.group(0))
                                    self._last.epilogue = epilogue[:-end]
                        else:
                            payload = self._last.get_payload()
                            if isinstance(payload, basestring):
                                mo = NLCRE_eol.search(payload)
                                if mo:
                                    payload = payload[:-len(mo.group(0))]
                                    self._last.set_payload(payload)
                        self._input.pop_eof_matcher()
                        self._pop_message()
                        self._last = self._cur
                    else:
                        preamble.append(line)

                if capturing_preamble:
                    self._cur.defects.append(errors.StartBoundaryNotFoundDefect())
                    self._cur.set_payload(EMPTYSTRING.join(preamble))
                    epilogue = []
                    for line in self._input:
                        if line is NeedMoreData:
                            yield NeedMoreData
                            continue

                    self._cur.epilogue = EMPTYSTRING.join(epilogue)
                    return
                if linesep:
                    epilogue = [
                     b'']
                else:
                    epilogue = []
                for line in self._input:
                    if line is NeedMoreData:
                        yield NeedMoreData
                        continue
                    epilogue.append(line)

                if epilogue:
                    firstline = epilogue[0]
                    bolmo = NLCRE_bol.match(firstline)
                    if bolmo:
                        epilogue[0] = firstline[len(bolmo.group(0)):]
                self._cur.epilogue = EMPTYSTRING.join(epilogue)
                return
            lines = []
            for line in self._input:
                if line is NeedMoreData:
                    yield NeedMoreData
                    continue
                lines.append(line)

            self._cur.set_payload(EMPTYSTRING.join(lines))
            return

    def _parse_headers(self, lines):
        lastheader = b''
        lastvalue = []
        for lineno, line in enumerate(lines):
            if line[0] in b' \t':
                if not lastheader:
                    defect = errors.FirstHeaderLineIsContinuationDefect(line)
                    self._cur.defects.append(defect)
                    continue
                lastvalue.append(line)
                continue
            if lastheader:
                lhdr = EMPTYSTRING.join(lastvalue)[:-1].rstrip(b'\r\n')
                self._cur[lastheader] = lhdr
                lastheader, lastvalue = b'', []
            if line.startswith(b'From '):
                if lineno == 0:
                    mo = NLCRE_eol.search(line)
                    if mo:
                        line = line[:-len(mo.group(0))]
                    self._cur.set_unixfrom(line)
                    continue
                elif lineno == len(lines) - 1:
                    self._input.unreadline(line)
                    return
                defect = errors.MisplacedEnvelopeHeaderDefect(line)
                self._cur.defects.append(defect)
                continue
            i = line.find(b':')
            if i < 0:
                defect = errors.MalformedHeaderDefect(line)
                self._cur.defects.append(defect)
                continue
            lastheader = line[:i]
            lastvalue = [line[i + 1:].lstrip()]

        if lastheader:
            self._cur[lastheader] = EMPTYSTRING.join(lastvalue).rstrip(b'\r\n')
        return
