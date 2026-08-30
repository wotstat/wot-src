import os, stat, shlex
if os.name == b'posix':
    import pwd
__all__ = [
 b'netrc', b'NetrcParseError']

class NetrcParseError(Exception):

    def __init__(self, msg, filename=None, lineno=None):
        self.filename = filename
        self.lineno = lineno
        self.msg = msg
        Exception.__init__(self, msg)
        return

    def __str__(self):
        return b'%s (%s, line %s)' % (self.msg, self.filename, self.lineno)


class netrc:

    def __init__(self, file=None):
        default_netrc = file is None
        if file is None:
            try:
                file = os.path.join(os.environ[b'HOME'], b'.netrc')
            except KeyError:
                raise IOError(b'Could not find .netrc: $HOME is not set')

        self.hosts = {}
        self.macros = {}
        with open(file) as fp:
            self._parse(file, fp, default_netrc)
        return

    def _parse(self, file, fp, default_netrc):
        lexer = shlex.shlex(fp)
        lexer.wordchars += b'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        lexer.commenters = lexer.commenters.replace(b'#', b'')
        while 1:
            toplevel = tt = lexer.get_token()
            if not tt:
                break
            elif tt[0] == b'#':
                pos = len(tt) + 1
                lexer.instream.seek(-pos, 1)
                lexer.instream.readline()
                continue
            elif tt == b'machine':
                entryname = lexer.get_token()
            elif tt == b'default':
                entryname = b'default'
            elif tt == b'macdef':
                entryname = lexer.get_token()
                self.macros[entryname] = []
                lexer.whitespace = b' \t'
                while 1:
                    line = lexer.instream.readline()
                    if not line or line == b'\n':
                        lexer.whitespace = b' \t\r\n'
                        break
                    self.macros[entryname].append(line)

                continue
            else:
                raise NetrcParseError(b'bad toplevel token %r' % tt, file, lexer.lineno)
            login = b''
            account = password = None
            self.hosts[entryname] = {}
            while 1:
                tt = lexer.get_token()
                if tt.startswith(b'#') or tt in {b'', b'machine', b'default', b'macdef'}:
                    if password:
                        self.hosts[entryname] = (
                         login, account, password)
                        lexer.push_token(tt)
                        break
                    else:
                        raise NetrcParseError(b'malformed %s entry %s terminated by %s' % (
                         toplevel, entryname, repr(tt)), file, lexer.lineno)
                elif tt == b'login' or tt == b'user':
                    login = lexer.get_token()
                elif tt == b'account':
                    account = lexer.get_token()
                elif tt == b'password':
                    if os.name == b'posix' and default_netrc:
                        prop = os.fstat(fp.fileno())
                        if prop.st_uid != os.getuid():
                            try:
                                fowner = pwd.getpwuid(prop.st_uid)[0]
                            except KeyError:
                                fowner = b'uid %s' % prop.st_uid

                            try:
                                user = pwd.getpwuid(os.getuid())[0]
                            except KeyError:
                                user = b'uid %s' % os.getuid()

                            raise NetrcParseError(b'~/.netrc file owner (%s) does not match current user (%s)' % (
                             fowner, user), file, lexer.lineno)
                        if prop.st_mode & (stat.S_IRWXG | stat.S_IRWXO):
                            raise NetrcParseError(b'~/.netrc access too permissive: access permissions must restrict access to only the owner', file, lexer.lineno)
                    password = lexer.get_token()
                else:
                    raise NetrcParseError(b'bad follower token %r' % tt, file, lexer.lineno)

        return

    def authenticators(self, host):
        if host in self.hosts:
            return self.hosts[host]
        else:
            if b'default' in self.hosts:
                return self.hosts[b'default']
            else:
                return

            return

    def __repr__(self):
        rep = b''
        for host in self.hosts.keys():
            attrs = self.hosts[host]
            rep += (b'machine {host}\n\tlogin {attrs[0]}\n').format(host=host, attrs=attrs)
            if attrs[1]:
                rep += (b'\taccount {attrs[1]}\n').format(attrs=attrs)
            rep += (b'\tpassword {attrs[2]}\n').format(attrs=attrs)

        for macro in self.macros.keys():
            rep += (b'macdef {macro}\n').format(macro=macro)
            for line in self.macros[macro]:
                rep += line

            rep += b'\n'

        return rep


if __name__ == b'__main__':
    print netrc()
