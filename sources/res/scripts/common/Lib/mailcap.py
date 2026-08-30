import os
__all__ = [
 b'getcaps', b'findmatch']

def getcaps():
    caps = {}
    for mailcap in listmailcapfiles():
        try:
            fp = open(mailcap, b'r')
        except IOError:
            continue

        with fp:
            morecaps = readmailcapfile(fp)
        for key, value in morecaps.iteritems():
            if key not in caps:
                caps[key] = value
            else:
                caps[key] = caps[key] + value

    return caps


def listmailcapfiles():
    if b'MAILCAPS' in os.environ:
        str = os.environ[b'MAILCAPS']
        mailcaps = str.split(b':')
    else:
        if b'HOME' in os.environ:
            home = os.environ[b'HOME']
        else:
            home = b'.'
        mailcaps = [
         home + b'/.mailcap', b'/etc/mailcap',
         b'/usr/etc/mailcap', b'/usr/local/etc/mailcap']
    return mailcaps


def readmailcapfile(fp):
    caps = {}
    while 1:
        line = fp.readline()
        if not line:
            break
        if line[0] == b'#' or line.strip() == b'':
            continue
        nextline = line
        while nextline[-2:] == b'\\\n':
            nextline = fp.readline()
            if not nextline:
                nextline = b'\n'
            line = line[:-2] + nextline

        key, fields = parseline(line)
        if not (key and fields):
            continue
        types = key.split(b'/')
        for j in range(len(types)):
            types[j] = types[j].strip()

        key = (b'/').join(types).lower()
        if key in caps:
            caps[key].append(fields)
        else:
            caps[key] = [
             fields]

    return caps


def parseline(line):
    fields = []
    i, n = 0, len(line)
    while i < n:
        field, i = parsefield(line, i, n)
        fields.append(field)
        i = i + 1

    if len(fields) < 2:
        return (None, None)
    else:
        key, view, rest = fields[0], fields[1], fields[2:]
        fields = {b'view': view}
        for field in rest:
            i = field.find(b'=')
            if i < 0:
                fkey = field
                fvalue = b''
            else:
                fkey = field[:i].strip()
                fvalue = field[i + 1:].strip()
            if fkey in fields:
                pass
            else:
                fields[fkey] = fvalue

        return (
         key, fields)


def parsefield(line, i, n):
    start = i
    while i < n:
        c = line[i]
        if c == b';':
            break
        elif c == b'\\':
            i = i + 2
        else:
            i = i + 1

    return (
     line[start:i].strip(), i)


def findmatch(caps, MIMEtype, key=b'view', filename=b'/dev/null', plist=[]):
    entries = lookup(caps, MIMEtype, key)
    for e in entries:
        if b'test' in e:
            test = subst(e[b'test'], filename, plist)
            if test and os.system(test) != 0:
                continue
        command = subst(e[key], MIMEtype, filename, plist)
        return (command, e)

    return (None, None)


def lookup(caps, MIMEtype, key=None):
    entries = []
    if MIMEtype in caps:
        entries = entries + caps[MIMEtype]
    MIMEtypes = MIMEtype.split(b'/')
    MIMEtype = MIMEtypes[0] + b'/*'
    if MIMEtype in caps:
        entries = entries + caps[MIMEtype]
    if key is not None:
        entries = filter((lambda e, key=key: key in e), entries)
    return entries


def subst(field, MIMEtype, filename, plist=[]):
    res = b''
    i, n = 0, len(field)
    while i < n:
        c = field[i]
        i = i + 1
        if c != b'%':
            if c == b'\\':
                c = field[i:i + 1]
                i = i + 1
            res = res + c
        else:
            c = field[i]
            i = i + 1
            if c == b'%':
                res = res + c
            elif c == b's':
                res = res + filename
            elif c == b't':
                res = res + MIMEtype
            elif c == b'{':
                start = i
                while i < n and field[i] != b'}':
                    i = i + 1

                name = field[start:i]
                i = i + 1
                res = res + findparam(name, plist)
            else:
                res = res + b'%' + c

    return res


def findparam(name, plist):
    name = name.lower() + b'='
    n = len(name)
    for p in plist:
        if p[:n].lower() == name:
            return p[n:]

    return b''


def test():
    import sys
    caps = getcaps()
    if not sys.argv[1:]:
        show(caps)
        return
    for i in range(1, len(sys.argv), 2):
        args = sys.argv[i:i + 2]
        if len(args) < 2:
            print b'usage: mailcap [MIMEtype file] ...'
            return
        MIMEtype = args[0]
        file = args[1]
        command, e = findmatch(caps, MIMEtype, b'view', file)
        if not command:
            print b'No viewer found for', type
        else:
            print b'Executing:', command
            sts = os.system(command)
            if sts:
                print b'Exit status:', sts

    return


def show(caps):
    print b'Mailcap files:'
    for fn in listmailcapfiles():
        print b'\t' + fn

    print
    if not caps:
        caps = getcaps()
    print b'Mailcap entries:'
    print
    ckeys = caps.keys()
    ckeys.sort()
    for type in ckeys:
        print type
        entries = caps[type]
        for e in entries:
            keys = e.keys()
            keys.sort()
            for k in keys:
                print b'  %-15s' % k, e[k]

            print

    return


if __name__ == b'__main__':
    test()
