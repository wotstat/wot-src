import time
from warnings import warnpy3k
warnpy3k(b'in 3.x, rfc822 has been removed in favor of the email package', stacklevel=2)
__all__ = [
 6, 7, 8, 9, 10]
_blanklines = (
 b'\r\n', b'\n')

class Message():

    def __init__(self, fp, seekable=1):
        if seekable == 1:
            try:
                fp.tell()
            except (AttributeError, IOError):
                seekable = 0

        self.fp = fp
        self.seekable = seekable
        self.startofheaders = None
        self.startofbody = None
        if self.seekable:
            try:
                self.startofheaders = self.fp.tell()
            except IOError:
                self.seekable = 0

        self.readheaders()
        if self.seekable:
            try:
                self.startofbody = self.fp.tell()
            except IOError:
                self.seekable = 0

        return

    def rewindbody(self):
        if not self.seekable:
            raise IOError, b'unseekable file'
        self.fp.seek(self.startofbody)
        return

    def readheaders(self):
        self.dict = {}
        self.unixfrom = b''
        self.headers = lst = []
        self.status = b''
        headerseen = b''
        firstline = 1
        startofline = unread = tell = None
        if hasattr(self.fp, b'unread'):
            unread = self.fp.unread
        elif self.seekable:
            tell = self.fp.tell
        while 1:
            if tell:
                try:
                    startofline = tell()
                except IOError:
                    startofline = tell = None
                    self.seekable = 0

            line = self.fp.readline()
            if not line:
                self.status = b'EOF in headers'
                break
            if firstline and line.startswith(b'From '):
                self.unixfrom = self.unixfrom + line
                continue
            firstline = 0
            if headerseen and line[0] in b' \t':
                lst.append(line)
                x = self.dict[headerseen] + b'\n ' + line.strip()
                self.dict[headerseen] = x.strip()
                continue
            elif self.iscomment(line):
                continue
            elif self.islast(line):
                break
            headerseen = self.isheader(line)
            if headerseen:
                lst.append(line)
                self.dict[headerseen] = line[len(headerseen) + 1:].strip()
                continue
            elif headerseen is not None:
                continue
            else:
                if not self.dict:
                    self.status = b'No headers'
                else:
                    self.status = b'Non-header line where header expected'
                if unread:
                    unread(line)
                elif tell:
                    self.fp.seek(startofline)
                else:
                    self.status = self.status + b'; bad seek'
                break

        return

    def isheader(self, line):
        i = line.find(b':')
        if i > -1:
            return line[:i].lower()
        else:
            return

    def islast(self, line):
        return line in _blanklines

    def iscomment(self, line):
        return False

    def getallmatchingheaders(self, name):
        name = name.lower() + b':'
        n = len(name)
        lst = []
        hit = 0
        for line in self.headers:
            if line[:n].lower() == name:
                hit = 1
            elif not line[:1].isspace():
                hit = 0
            if hit:
                lst.append(line)

        return lst

    def getfirstmatchingheader(self, name):
        name = name.lower() + b':'
        n = len(name)
        lst = []
        hit = 0
        for line in self.headers:
            if hit:
                if not line[:1].isspace():
                    break
            elif line[:n].lower() == name:
                hit = 1
            if hit:
                lst.append(line)

        return lst

    def getrawheader(self, name):
        lst = self.getfirstmatchingheader(name)
        if not lst:
            return None
        else:
            lst[0] = lst[0][len(name) + 1:]
            return (b'').join(lst)

    def getheader(self, name, default=None):
        return self.dict.get(name.lower(), default)

    get = getheader

    def getheaders(self, name):
        result = []
        current = b''
        have_header = 0
        for s in self.getallmatchingheaders(name):
            if s[0].isspace():
                if current:
                    current = b'%s\n %s' % (current, s.strip())
                else:
                    current = s.strip()
            elif have_header:
                result.append(current)
            current = s[s.find(b':') + 1:].strip()
            have_header = 1

        if have_header:
            result.append(current)
        return result

    def getaddr(self, name):
        alist = self.getaddrlist(name)
        if alist:
            return alist[0]
        else:
            return (None, None)
            return

    def getaddrlist(self, name):
        raw = []
        for h in self.getallmatchingheaders(name):
            if h[0] in b' \t':
                raw.append(h)
            elif raw:
                raw.append(b', ')
            i = h.find(b':')
            if i > 0:
                addr = h[i + 1:]
            raw.append(addr)

        alladdrs = (b'').join(raw)
        a = AddressList(alladdrs)
        return a.addresslist

    def getdate(self, name):
        try:
            data = self[name]
        except KeyError:
            return

        return parsedate(data)

    def getdate_tz(self, name):
        try:
            data = self[name]
        except KeyError:
            return

        return parsedate_tz(data)

    def __len__(self):
        return len(self.dict)

    def __getitem__(self, name):
        return self.dict[name.lower()]

    def __setitem__(self, name, value):
        del self[name]
        self.dict[name.lower()] = value
        text = name + b': ' + value
        for line in text.split(b'\n'):
            self.headers.append(line + b'\n')

        return

    def __delitem__(self, name):
        name = name.lower()
        if name not in self.dict:
            return
        del self.dict[name]
        name = name + b':'
        n = len(name)
        lst = []
        hit = 0
        for i in range(len(self.headers)):
            line = self.headers[i]
            if line[:n].lower() == name:
                hit = 1
            elif not line[:1].isspace():
                hit = 0
            if hit:
                lst.append(i)

        for i in reversed(lst):
            del self.headers[i]

        return

    def setdefault(self, name, default=b''):
        lowername = name.lower()
        if lowername in self.dict:
            return self.dict[lowername]
        else:
            text = name + b': ' + default
            for line in text.split(b'\n'):
                self.headers.append(line + b'\n')

            self.dict[lowername] = default
            return default

        return

    def has_key(self, name):
        return name.lower() in self.dict

    def __contains__(self, name):
        return name.lower() in self.dict

    def __iter__(self):
        return iter(self.dict)

    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def items(self):
        return self.dict.items()

    def __str__(self):
        return (b'').join(self.headers)


def unquote(s):
    if len(s) > 1:
        if s.startswith(b'"') and s.endswith(b'"'):
            return s[1:-1].replace(b'\\\\', b'\\').replace(b'\\"', b'"')
        if s.startswith(b'<') and s.endswith(b'>'):
            return s[1:-1]
    return s


def quote(s):
    return s.replace(b'\\', b'\\\\').replace(b'"', b'\\"')


def parseaddr(address):
    a = AddressList(address)
    lst = a.addresslist
    if not lst:
        return (None, None)
    else:
        return lst[0]


class AddrlistClass():

    def __init__(self, field):
        self.specials = b'()<>@,:;."[]'
        self.pos = 0
        self.LWS = b' \t'
        self.CR = b'\r\n'
        self.atomends = self.specials + self.LWS + self.CR
        self.phraseends = self.atomends.replace(b'.', b'')
        self.field = field
        self.commentlist = []
        return

    def gotonext(self):
        while self.pos < len(self.field):
            if self.field[self.pos] in self.LWS + b'\n\r':
                self.pos = self.pos + 1
            elif self.field[self.pos] == b'(':
                self.commentlist.append(self.getcomment())
            else:
                break

        return

    def getaddrlist(self):
        result = []
        ad = self.getaddress()
        while ad:
            result += ad
            ad = self.getaddress()

        return result

    def getaddress(self):
        self.commentlist = []
        self.gotonext()
        oldpos = self.pos
        oldcl = self.commentlist
        plist = self.getphraselist()
        self.gotonext()
        returnlist = []
        if self.pos >= len(self.field):
            if plist:
                returnlist = [
                 (
                  (b' ').join(self.commentlist), plist[0])]
        elif self.field[self.pos] in b'.@':
            self.pos = oldpos
            self.commentlist = oldcl
            addrspec = self.getaddrspec()
            returnlist = [((b' ').join(self.commentlist), addrspec)]
        elif self.field[self.pos] == b':':
            returnlist = []
            fieldlen = len(self.field)
            self.pos += 1
            while self.pos < len(self.field):
                self.gotonext()
                if self.pos < fieldlen and self.field[self.pos] == b';':
                    self.pos += 1
                    break
                returnlist = returnlist + self.getaddress()

        elif self.field[self.pos] == b'<':
            routeaddr = self.getrouteaddr()
            if self.commentlist:
                returnlist = [((b' ').join(plist) + b' (' + (b' ').join(self.commentlist) + b')', routeaddr)]
            else:
                returnlist = [
                 (
                  (b' ').join(plist), routeaddr)]
        elif plist:
            returnlist = [
             (
              (b' ').join(self.commentlist), plist[0])]
        elif self.field[self.pos] in self.specials:
            self.pos += 1
        self.gotonext()
        if self.pos < len(self.field) and self.field[self.pos] == b',':
            self.pos += 1
        return returnlist

    def getrouteaddr(self):
        if self.field[self.pos] != b'<':
            return
        expectroute = 0
        self.pos += 1
        self.gotonext()
        adlist = b''
        while self.pos < len(self.field):
            if expectroute:
                self.getdomain()
                expectroute = 0
            elif self.field[self.pos] == b'>':
                self.pos += 1
                break
            elif self.field[self.pos] == b'@':
                self.pos += 1
                expectroute = 1
            elif self.field[self.pos] == b':':
                self.pos += 1
            else:
                adlist = self.getaddrspec()
                self.pos += 1
                break
            self.gotonext()

        return adlist

    def getaddrspec(self):
        aslist = []
        self.gotonext()
        while self.pos < len(self.field):
            if self.field[self.pos] == b'.':
                aslist.append(b'.')
                self.pos += 1
            elif self.field[self.pos] == b'"':
                aslist.append(b'"%s"' % self.getquote())
            elif self.field[self.pos] in self.atomends:
                break
            else:
                aslist.append(self.getatom())
            self.gotonext()

        if self.pos >= len(self.field) or self.field[self.pos] != b'@':
            return (b'').join(aslist)
        aslist.append(b'@')
        self.pos += 1
        self.gotonext()
        return (b'').join(aslist) + self.getdomain()

    def getdomain(self):
        sdlist = []
        while self.pos < len(self.field):
            if self.field[self.pos] in self.LWS:
                self.pos += 1
            elif self.field[self.pos] == b'(':
                self.commentlist.append(self.getcomment())
            elif self.field[self.pos] == b'[':
                sdlist.append(self.getdomainliteral())
            elif self.field[self.pos] == b'.':
                self.pos += 1
                sdlist.append(b'.')
            elif self.field[self.pos] in self.atomends:
                break
            else:
                sdlist.append(self.getatom())

        return (b'').join(sdlist)

    def getdelimited(self, beginchar, endchars, allowcomments=1):
        if self.field[self.pos] != beginchar:
            return b''
        slist = [b'']
        quote = 0
        self.pos += 1
        while self.pos < len(self.field):
            if quote == 1:
                slist.append(self.field[self.pos])
                quote = 0
            elif self.field[self.pos] in endchars:
                self.pos += 1
                break
            elif allowcomments and self.field[self.pos] == b'(':
                slist.append(self.getcomment())
                continue
            elif self.field[self.pos] == b'\\':
                quote = 1
            else:
                slist.append(self.field[self.pos])
            self.pos += 1

        return (b'').join(slist)

    def getquote(self):
        return self.getdelimited(b'"', b'"\r', 0)

    def getcomment(self):
        return self.getdelimited(b'(', b')\r', 1)

    def getdomainliteral(self):
        return b'[%s]' % self.getdelimited(b'[', b']\r', 0)

    def getatom(self, atomends=None):
        atomlist = [
         b'']
        if atomends is None:
            atomends = self.atomends
        while self.pos < len(self.field):
            if self.field[self.pos] in atomends:
                break
            else:
                atomlist.append(self.field[self.pos])
            self.pos += 1

        return (b'').join(atomlist)

    def getphraselist(self):
        plist = []
        while self.pos < len(self.field):
            if self.field[self.pos] in self.LWS:
                self.pos += 1
            elif self.field[self.pos] == b'"':
                plist.append(self.getquote())
            elif self.field[self.pos] == b'(':
                self.commentlist.append(self.getcomment())
            elif self.field[self.pos] in self.phraseends:
                break
            else:
                plist.append(self.getatom(self.phraseends))

        return plist


class AddressList(AddrlistClass):

    def __init__(self, field):
        AddrlistClass.__init__(self, field)
        if field:
            self.addresslist = self.getaddrlist()
        else:
            self.addresslist = []
        return

    def __len__(self):
        return len(self.addresslist)

    def __str__(self):
        return (b', ').join(map(dump_address_pair, self.addresslist))

    def __add__(self, other):
        newaddr = AddressList(None)
        newaddr.addresslist = self.addresslist[:]
        for x in other.addresslist:
            if x not in self.addresslist:
                newaddr.addresslist.append(x)

        return newaddr

    def __iadd__(self, other):
        for x in other.addresslist:
            if x not in self.addresslist:
                self.addresslist.append(x)

        return self

    def __sub__(self, other):
        newaddr = AddressList(None)
        for x in self.addresslist:
            if x not in other.addresslist:
                newaddr.addresslist.append(x)

        return newaddr

    def __isub__(self, other):
        for x in other.addresslist:
            if x in self.addresslist:
                self.addresslist.remove(x)

        return self

    def __getitem__(self, index):
        return self.addresslist[index]


def dump_address_pair(pair):
    if pair[0]:
        return b'"' + pair[0] + b'" <' + pair[1] + b'>'
    else:
        return pair[1]

    return


_monthnames = [
 21, 22, 23, 24, 25, 26, 27, 
 28, 29, 30, 31, 32, 
 33, 34, 35, 
 36, 25, 37, 38, 
 39, 40, 41, 42, 43]
_daynames = [44, 45, 46, 47, 48, 49, 50]
_timezones = {b'UT': 0, b'UTC': 0, b'GMT': 0, b'Z': 0, b'AST': (-400), 
   b'ADT': (-300), b'EST': (-500), 
   b'EDT': (-400), b'CST': (-600), 
   b'CDT': (-500), b'MST': (-700), 
   b'MDT': (-600), b'PST': (-800), 
   b'PDT': (-700)}

def parsedate_tz(data):
    if not data:
        return
    else:
        data = data.split()
        if data[0][-1] in (b',', b'.') or data[0].lower() in _daynames:
            del data[0]
        else:
            i = data[0].rfind(b',')
            if i >= 0:
                data[0] = data[0][i + 1:]
        if len(data) == 3:
            stuff = data[0].split(b'-')
            if len(stuff) == 3:
                data = stuff + data[1:]
        if len(data) == 4:
            s = data[3]
            i = s.find(b'+')
            if i > 0:
                data[3:] = [
                 s[:i], s[i + 1:]]
            else:
                data.append(b'')
        if len(data) < 5:
            return
        data = data[:5]
        dd, mm, yy, tm, tz = data
        mm = mm.lower()
        if mm not in _monthnames:
            dd, mm = mm, dd.lower()
            if mm not in _monthnames:
                return
        mm = _monthnames.index(mm) + 1
        if mm > 12:
            mm = mm - 12
        if dd[-1] == b',':
            dd = dd[:-1]
        i = yy.find(b':')
        if i > 0:
            yy, tm = tm, yy
        if yy[-1] == b',':
            yy = yy[:-1]
        if not yy[0].isdigit():
            yy, tz = tz, yy
        if tm[-1] == b',':
            tm = tm[:-1]
        tm = tm.split(b':')
        if len(tm) == 2:
            thh, tmm = tm
            tss = b'0'
        elif len(tm) == 3:
            thh, tmm, tss = tm
        else:
            return
        try:
            yy = int(yy)
            dd = int(dd)
            thh = int(thh)
            tmm = int(tmm)
            tss = int(tss)
        except ValueError:
            return

        tzoffset = None
        tz = tz.upper()
        if tz in _timezones:
            tzoffset = _timezones[tz]
        else:
            try:
                tzoffset = int(tz)
            except ValueError:
                pass

        if tzoffset:
            if tzoffset < 0:
                tzsign = -1
                tzoffset = -tzoffset
            else:
                tzsign = 1
            tzoffset = tzsign * (tzoffset // 100 * 3600 + tzoffset % 100 * 60)
        return (
         yy, mm, dd, thh, tmm, tss, 0, 1, 0, tzoffset)


def parsedate(data):
    t = parsedate_tz(data)
    if t is None:
        return t
    else:
        return t[:9]


def mktime_tz(data):
    if data[9] is None:
        return time.mktime(data[:8] + (-1,))
    else:
        t = time.mktime(data[:8] + (0,))
        return t - data[9] - time.timezone
        return


def formatdate(timeval=None):
    if timeval is None:
        timeval = time.time()
    timeval = time.gmtime(timeval)
    return b'%s, %02d %s %04d %02d:%02d:%02d GMT' % (
     (b'Mon', b'Tue', b'Wed', b'Thu', b'Fri', b'Sat', b'Sun')[timeval[6]],
     timeval[2],
     (b'Jan', b'Feb', b'Mar', b'Apr', b'May', b'Jun', b'Jul', b'Aug', b'Sep', b'Oct', b'Nov', b'Dec')[timeval[1] - 1],
     timeval[0], timeval[3], timeval[4], timeval[5])


if __name__ == b'__main__':
    import sys, os
    file = os.path.join(os.environ[b'HOME'], b'Mail/inbox/1')
    if sys.argv[1:]:
        file = sys.argv[1]
    f = open(file, b'r')
    m = Message(f)
    print b'From:', m.getaddr(b'from')
    print b'To:', m.getaddrlist(b'to')
    print b'Subject:', m.getheader(b'subject')
    print b'Date:', m.getheader(b'date')
    date = m.getdate_tz(b'date')
    tz = date[-1]
    date = time.localtime(mktime_tz(date))
    if date:
        print b'ParsedDate:', time.asctime(date),
        hhmmss = tz
        hhmm, ss = divmod(hhmmss, 60)
        hh, mm = divmod(hhmm, 60)
        print b'%+03d%02d' % (hh, mm),
        if ss:
            print b'.%02d' % ss,
        print
    else:
        print b'ParsedDate:', None
    m.rewindbody()
    n = 0
    while f.readline():
        n += 1

    print b'Lines:', n
    print b'-' * 70
    print b'len =', len(m)
    if b'Date' in m:
        print b'Date =', m[b'Date']
    if b'X-Nonsense' in m:
        pass
    print b'keys =', m.keys()
    print b'values =', m.values()
    print b'items =', m.items()
