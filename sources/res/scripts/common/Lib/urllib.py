import string, socket, os, time, sys, base64, re
from urlparse import urljoin as basejoin
__all__ = [
 3, 4, 5, 6, 
 7, 8, 9, 10, 11, 
 12, 13, 14, 15, 
 16, 17, 18, 
 19, 20, 
 21, 22, 23, 24, 25, 
 26, 27, 28, 29, 
 30]
__version__ = b'1.17'
MAXFTPCACHE = 10
if os.name == b'nt':
    from nturl2path import url2pathname, pathname2url
elif os.name == b'riscos':
    from rourl2path import url2pathname, pathname2url
else:

    def url2pathname(pathname):
        return unquote(pathname)


    def pathname2url(pathname):
        return quote(pathname)


_urlopener = None

def urlopen(url, data=None, proxies=None, context=None):
    global _urlopener
    from warnings import warnpy3k
    warnpy3k(b'urllib.urlopen() has been removed in Python 3.0 in favor of urllib2.urlopen()', stacklevel=2)
    if proxies is not None or context is not None:
        opener = FancyURLopener(proxies=proxies, context=context)
    elif not _urlopener:
        opener = FancyURLopener()
        _urlopener = opener
    else:
        opener = _urlopener
    if data is None:
        return opener.open(url)
    else:
        return opener.open(url, data)
        return


def urlretrieve(url, filename=None, reporthook=None, data=None, context=None):
    global _urlopener
    if context is not None:
        opener = FancyURLopener(context=context)
    elif not _urlopener:
        _urlopener = opener = FancyURLopener()
    else:
        opener = _urlopener
    return opener.retrieve(url, filename, reporthook, data)


def urlcleanup():
    if _urlopener:
        _urlopener.cleanup()
    _safe_quoters.clear()
    ftpcache.clear()
    return


try:
    import ssl
except:
    _have_ssl = False
else:
    _have_ssl = True

class ContentTooShortError(IOError):

    def __init__(self, message, content):
        IOError.__init__(self, message)
        self.content = content
        return


ftpcache = {}

class URLopener():
    __tempfiles = None
    version = b'Python-urllib/%s' % __version__

    def __init__(self, proxies=None, context=None, **x509):
        if proxies is None:
            proxies = getproxies()
        self.proxies = proxies
        self.key_file = x509.get(b'key_file')
        self.cert_file = x509.get(b'cert_file')
        self.context = context
        self.addheaders = [(b'User-Agent', self.version), (b'Accept', b'*/*')]
        self.__tempfiles = []
        self.__unlink = os.unlink
        self.tempcache = None
        self.ftpcache = ftpcache
        return

    def __del__(self):
        self.close()
        return

    def close(self):
        self.cleanup()
        return

    def cleanup(self):
        if self.__tempfiles:
            for file in self.__tempfiles:
                try:
                    self.__unlink(file)
                except OSError:
                    pass

            del self.__tempfiles[:]
        if self.tempcache:
            self.tempcache.clear()
        return

    def addheader(self, *args):
        self.addheaders.append(args)
        return

    def open(self, fullurl, data=None):
        fullurl = unwrap(toBytes(fullurl))
        fullurl = quote(fullurl, safe=b"%/:=&?~#+!$,;'@()*[]|")
        if self.tempcache and fullurl in self.tempcache:
            filename, headers = self.tempcache[fullurl]
            fp = open(filename, b'rb')
            return addinfourl(fp, headers, fullurl)
        else:
            urltype, url = splittype(fullurl)
            if not urltype:
                urltype = b'file'
            if urltype in self.proxies:
                proxy = self.proxies[urltype]
                urltype, proxyhost = splittype(proxy)
                host, selector = splithost(proxyhost)
                url = (host, fullurl)
            else:
                proxy = None
            name = b'open_' + urltype
            self.type = urltype
            name = name.replace(b'-', b'_')
            if not hasattr(self, name) or name == b'open_local_file':
                if proxy:
                    return self.open_unknown_proxy(proxy, fullurl, data)
                else:
                    return self.open_unknown(fullurl, data)

            try:
                if data is None:
                    return getattr(self, name)(url)
                else:
                    return getattr(self, name)(url, data)

            except socket.error as msg:
                raise IOError, (b'socket error', msg), sys.exc_info()[2]

            return

    def open_unknown(self, fullurl, data=None):
        type, url = splittype(fullurl)
        raise IOError, (b'url error', b'unknown url type', type)
        return

    def open_unknown_proxy(self, proxy, fullurl, data=None):
        type, url = splittype(fullurl)
        raise IOError, (b'url error', b'invalid proxy for %s' % type, proxy)
        return

    def retrieve(self, url, filename=None, reporthook=None, data=None):
        url = unwrap(toBytes(url))
        if self.tempcache and url in self.tempcache:
            return self.tempcache[url]
        else:
            type, url1 = splittype(url)
            if filename is None and (not type or type == b'file'):
                try:
                    fp = self.open_local_file(url1)
                    hdrs = fp.info()
                    fp.close()
                    return (url2pathname(splithost(url1)[1]), hdrs)
                except IOError:
                    pass

            fp = self.open(url, data)
            try:
                headers = fp.info()
                if filename:
                    tfp = open(filename, b'wb')
                else:
                    import tempfile
                    garbage, path = splittype(url)
                    garbage, path = splithost(path or b'')
                    path, garbage = splitquery(path or b'')
                    path, garbage = splitattr(path or b'')
                    suffix = os.path.splitext(path)[1]
                    fd, filename = tempfile.mkstemp(suffix)
                    self.__tempfiles.append(filename)
                    tfp = os.fdopen(fd, b'wb')
                try:
                    result = (
                     filename, headers)
                    if self.tempcache is not None:
                        self.tempcache[url] = result
                    bs = 8192
                    size = -1
                    read = 0
                    blocknum = 0
                    if b'content-length' in headers:
                        size = int(headers[b'Content-Length'])
                    if reporthook:
                        reporthook(blocknum, bs, size)
                    while 1:
                        block = fp.read(bs)
                        if block == b'':
                            break
                        read += len(block)
                        tfp.write(block)
                        blocknum += 1
                        if reporthook:
                            reporthook(blocknum, bs, size)

                finally:
                    tfp.close()

            finally:
                fp.close()

            if size >= 0 and read < size:
                raise ContentTooShortError(b'retrieval incomplete: got only %i out of %i bytes' % (
                 read, size), result)
            return result

    def open_http(self, url, data=None):
        import httplib
        user_passwd = None
        proxy_passwd = None
        if isinstance(url, str):
            host, selector = splithost(url)
            if host:
                user_passwd, host = splituser(host)
                host = unquote(host)
            realhost = host
        else:
            host, selector = url
            proxy_passwd, host = splituser(host)
            urltype, rest = splittype(selector)
            url = rest
            user_passwd = None
            if urltype.lower() != b'http':
                realhost = None
            else:
                realhost, rest = splithost(rest)
                if realhost:
                    user_passwd, realhost = splituser(realhost)
                if user_passwd:
                    selector = b'%s://%s%s' % (urltype, realhost, rest)
                if proxy_bypass(realhost):
                    host = realhost
        if not host:
            raise IOError, (b'http error', b'no host given')
        if proxy_passwd:
            proxy_passwd = unquote(proxy_passwd)
            proxy_auth = base64.b64encode(proxy_passwd).strip()
        else:
            proxy_auth = None
        if user_passwd:
            user_passwd = unquote(user_passwd)
            auth = base64.b64encode(user_passwd).strip()
        else:
            auth = None
        h = httplib.HTTP(host)
        if data is not None:
            h.putrequest(b'POST', selector)
            h.putheader(b'Content-Type', b'application/x-www-form-urlencoded')
            h.putheader(b'Content-Length', b'%d' % len(data))
        else:
            h.putrequest(b'GET', selector)
        if proxy_auth:
            h.putheader(b'Proxy-Authorization', b'Basic %s' % proxy_auth)
        if auth:
            h.putheader(b'Authorization', b'Basic %s' % auth)
        if realhost:
            h.putheader(b'Host', realhost)
        for args in self.addheaders:
            h.putheader(*args)

        h.endheaders(data)
        errcode, errmsg, headers = h.getreply()
        fp = h.getfile()
        if errcode == -1:
            if fp:
                fp.close()
            raise IOError, (b'http protocol error', 0, b'got a bad status line', None)
        if 200 <= errcode < 300:
            return addinfourl(fp, headers, b'http:' + url, errcode)
        else:
            if data is None:
                return self.http_error(url, fp, errcode, errmsg, headers)
            else:
                return self.http_error(url, fp, errcode, errmsg, headers, data)

            return

    def http_error(self, url, fp, errcode, errmsg, headers, data=None):
        name = b'http_error_%d' % errcode
        if hasattr(self, name):
            method = getattr(self, name)
            if data is None:
                result = method(url, fp, errcode, errmsg, headers)
            else:
                result = method(url, fp, errcode, errmsg, headers, data)
            if result:
                return result
        return self.http_error_default(url, fp, errcode, errmsg, headers)

    def http_error_default(self, url, fp, errcode, errmsg, headers):
        fp.close()
        raise IOError, (b'http error', errcode, errmsg, headers)
        return

    if _have_ssl:

        def open_https(self, url, data=None):
            import httplib
            user_passwd = None
            proxy_passwd = None
            if isinstance(url, str):
                host, selector = splithost(url)
                if host:
                    user_passwd, host = splituser(host)
                    host = unquote(host)
                realhost = host
            else:
                host, selector = url
                proxy_passwd, host = splituser(host)
                urltype, rest = splittype(selector)
                url = rest
                user_passwd = None
                if urltype.lower() != b'https':
                    realhost = None
                else:
                    realhost, rest = splithost(rest)
                    if realhost:
                        user_passwd, realhost = splituser(realhost)
                    if user_passwd:
                        selector = b'%s://%s%s' % (urltype, realhost, rest)
            if not host:
                raise IOError, (b'https error', b'no host given')
            if proxy_passwd:
                proxy_passwd = unquote(proxy_passwd)
                proxy_auth = base64.b64encode(proxy_passwd).strip()
            else:
                proxy_auth = None
            if user_passwd:
                user_passwd = unquote(user_passwd)
                auth = base64.b64encode(user_passwd).strip()
            else:
                auth = None
            h = httplib.HTTPS(host, 0, key_file=self.key_file, cert_file=self.cert_file, context=self.context)
            if data is not None:
                h.putrequest(b'POST', selector)
                h.putheader(b'Content-Type', b'application/x-www-form-urlencoded')
                h.putheader(b'Content-Length', b'%d' % len(data))
            else:
                h.putrequest(b'GET', selector)
            if proxy_auth:
                h.putheader(b'Proxy-Authorization', b'Basic %s' % proxy_auth)
            if auth:
                h.putheader(b'Authorization', b'Basic %s' % auth)
            if realhost:
                h.putheader(b'Host', realhost)
            for args in self.addheaders:
                h.putheader(*args)

            h.endheaders(data)
            errcode, errmsg, headers = h.getreply()
            fp = h.getfile()
            if errcode == -1:
                if fp:
                    fp.close()
                raise IOError, (b'http protocol error', 0, b'got a bad status line', None)
            if 200 <= errcode < 300:
                return addinfourl(fp, headers, b'https:' + url, errcode)
            else:
                if data is None:
                    return self.http_error(url, fp, errcode, errmsg, headers)
                else:
                    return self.http_error(url, fp, errcode, errmsg, headers, data)

                return

    def open_file(self, url):
        if not isinstance(url, str):
            raise IOError, (b'file error', b'proxy support for file protocol currently not implemented')
        if url[:2] == b'//' and url[2:3] != b'/' and url[2:12].lower() != b'localhost/':
            return self.open_ftp(url)
        else:
            return self.open_local_file(url)

        return

    def open_local_file(self, url):
        import mimetypes, mimetools, email.utils
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO

        host, file = splithost(url)
        localname = url2pathname(file)
        try:
            stats = os.stat(localname)
        except OSError as e:
            raise IOError(e.errno, e.strerror, e.filename)

        size = stats.st_size
        modified = email.utils.formatdate(stats.st_mtime, usegmt=True)
        mtype = mimetypes.guess_type(url)[0]
        headers = mimetools.Message(StringIO(b'Content-Type: %s\nContent-Length: %d\nLast-modified: %s\n' % (
         mtype or b'text/plain', size, modified)))
        if not host:
            urlfile = file
            if file[:1] == b'/':
                urlfile = b'file://' + file
            elif file[:2] == b'./':
                raise ValueError(b'local file url may start with / or file:. Unknown url of type: %s' % url)
            return addinfourl(open(localname, b'rb'), headers, urlfile)
        host, port = splitport(host)
        if not port and socket.gethostbyname(host) in (localhost(), thishost()):
            urlfile = file
            if file[:1] == b'/':
                urlfile = b'file://' + file
            return addinfourl(open(localname, b'rb'), headers, urlfile)
        raise IOError, (b'local file error', b'not on local host')
        return

    def open_ftp(self, url):
        if not isinstance(url, str):
            raise IOError, (b'ftp error', b'proxy support for ftp protocol currently not implemented')
        import mimetypes, mimetools
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO

        host, path = splithost(url)
        if not host:
            raise IOError, (b'ftp error', b'no host given')
        host, port = splitport(host)
        user, host = splituser(host)
        if user:
            user, passwd = splitpasswd(user)
        else:
            passwd = None
        host = unquote(host)
        user = user or b''
        passwd = passwd or b''
        host = socket.gethostbyname(host)
        if not port:
            import ftplib
            port = ftplib.FTP_PORT
        else:
            port = int(port)
        path, attrs = splitattr(path)
        path = unquote(path)
        dirs = path.split(b'/')
        dirs, file = dirs[:-1], dirs[-1]
        if dirs and not dirs[0]:
            dirs = dirs[1:]
        if dirs and not dirs[0]:
            dirs[0] = b'/'
        key = (
         user, host, port, (b'/').join(dirs))
        if len(self.ftpcache) > MAXFTPCACHE:
            for k in self.ftpcache.keys():
                if k != key:
                    v = self.ftpcache[k]
                    del self.ftpcache[k]
                    v.close()

        try:
            if key not in self.ftpcache:
                self.ftpcache[key] = ftpwrapper(user, passwd, host, port, dirs)
            if not file:
                type = b'D'
            else:
                type = b'I'
            for attr in attrs:
                attr, value = splitvalue(attr)
                if attr.lower() == b'type' and value in (b'a', b'A', b'i', b'I', b'd', b'D'):
                    type = value.upper()

            fp, retrlen = self.ftpcache[key].retrfile(file, type)
            mtype = mimetypes.guess_type(b'ftp:' + url)[0]
            headers = b''
            if mtype:
                headers += b'Content-Type: %s\n' % mtype
            if retrlen is not None and retrlen >= 0:
                headers += b'Content-Length: %d\n' % retrlen
            headers = mimetools.Message(StringIO(headers))
            return addinfourl(fp, headers, b'ftp:' + url)
        except ftperrors() as msg:
            raise IOError, (b'ftp error', msg), sys.exc_info()[2]

        return

    def open_data(self, url, data=None):
        if not isinstance(url, str):
            raise IOError, (b'data error', b'proxy support for data protocol currently not implemented')
        import mimetools
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO

        try:
            type, data = url.split(b',', 1)
        except ValueError:
            raise IOError, (b'data error', b'bad data URL')

        if not type:
            type = b'text/plain;charset=US-ASCII'
        semi = type.rfind(b';')
        if semi >= 0 and b'=' not in type[semi:]:
            encoding = type[semi + 1:]
            type = type[:semi]
        else:
            encoding = b''
        msg = []
        msg.append(b'Date: %s' % time.strftime(b'%a, %d %b %Y %H:%M:%S GMT', time.gmtime(time.time())))
        msg.append(b'Content-type: %s' % type)
        if encoding == b'base64':
            data = base64.decodestring(data)
        else:
            data = unquote(data)
        msg.append(b'Content-Length: %d' % len(data))
        msg.append(b'')
        msg.append(data)
        msg = (b'\n').join(msg)
        f = StringIO(msg)
        headers = mimetools.Message(f, 0)
        return addinfourl(f, headers, url)


class FancyURLopener(URLopener):

    def __init__(self, *args, **kwargs):
        URLopener.__init__(self, *args, **kwargs)
        self.auth_cache = {}
        self.tries = 0
        self.maxtries = 10
        return

    def http_error_default(self, url, fp, errcode, errmsg, headers):
        return addinfourl(fp, headers, b'http:' + url, errcode)

    def http_error_302(self, url, fp, errcode, errmsg, headers, data=None):
        self.tries += 1
        try:
            if self.maxtries and self.tries >= self.maxtries:
                if hasattr(self, b'http_error_500'):
                    meth = self.http_error_500
                else:
                    meth = self.http_error_default
                return meth(url, fp, 500, b'Internal Server Error: Redirect Recursion', headers)
            else:
                result = self.redirect_internal(url, fp, errcode, errmsg, headers, data)
                return result

        finally:
            self.tries = 0

        return

    def redirect_internal(self, url, fp, errcode, errmsg, headers, data):
        if b'location' in headers:
            newurl = headers[b'location']
        elif b'uri' in headers:
            newurl = headers[b'uri']
        else:
            return
        fp.close()
        newurl = basejoin(self.type + b':' + url, newurl)
        newurl_lower = newurl.lower()
        if not (newurl_lower.startswith(b'http://') or newurl_lower.startswith(b'https://') or newurl_lower.startswith(b'ftp://')):
            raise IOError(b'redirect error', errcode, errmsg + b" - Redirection to url '%s' is not allowed" % newurl, headers)
        return self.open(newurl)

    def http_error_301(self, url, fp, errcode, errmsg, headers, data=None):
        return self.http_error_302(url, fp, errcode, errmsg, headers, data)

    def http_error_303(self, url, fp, errcode, errmsg, headers, data=None):
        return self.http_error_302(url, fp, errcode, errmsg, headers, data)

    def http_error_307(self, url, fp, errcode, errmsg, headers, data=None):
        if data is None:
            return self.http_error_302(url, fp, errcode, errmsg, headers, data)
        else:
            return self.http_error_default(url, fp, errcode, errmsg, headers)
            return

    def http_error_401(self, url, fp, errcode, errmsg, headers, data=None):
        if b'www-authenticate' not in headers:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        stuff = headers[b'www-authenticate']
        import re
        match = re.match(b'[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
        if not match:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        scheme, realm = match.groups()
        if scheme.lower() != b'basic':
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        name = b'retry_' + self.type + b'_basic_auth'
        if data is None:
            return getattr(self, name)(url, realm)
        else:
            return getattr(self, name)(url, realm, data)
            return

    def http_error_407(self, url, fp, errcode, errmsg, headers, data=None):
        if b'proxy-authenticate' not in headers:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        stuff = headers[b'proxy-authenticate']
        import re
        match = re.match(b'[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
        if not match:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        scheme, realm = match.groups()
        if scheme.lower() != b'basic':
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        name = b'retry_proxy_' + self.type + b'_basic_auth'
        if data is None:
            return getattr(self, name)(url, realm)
        else:
            return getattr(self, name)(url, realm, data)
            return

    def retry_proxy_http_basic_auth(self, url, realm, data=None):
        host, selector = splithost(url)
        newurl = b'http://' + host + selector
        proxy = self.proxies[b'http']
        urltype, proxyhost = splittype(proxy)
        proxyhost, proxyselector = splithost(proxyhost)
        i = proxyhost.find(b'@') + 1
        proxyhost = proxyhost[i:]
        user, passwd = self.get_user_passwd(proxyhost, realm, i)
        if not (user or passwd):
            return
        else:
            proxyhost = quote(user, safe=b'') + b':' + quote(passwd, safe=b'') + b'@' + proxyhost
            self.proxies[b'http'] = b'http://' + proxyhost + proxyselector
            if data is None:
                return self.open(newurl)
            return self.open(newurl, data)
            return

    def retry_proxy_https_basic_auth(self, url, realm, data=None):
        host, selector = splithost(url)
        newurl = b'https://' + host + selector
        proxy = self.proxies[b'https']
        urltype, proxyhost = splittype(proxy)
        proxyhost, proxyselector = splithost(proxyhost)
        i = proxyhost.find(b'@') + 1
        proxyhost = proxyhost[i:]
        user, passwd = self.get_user_passwd(proxyhost, realm, i)
        if not (user or passwd):
            return
        else:
            proxyhost = quote(user, safe=b'') + b':' + quote(passwd, safe=b'') + b'@' + proxyhost
            self.proxies[b'https'] = b'https://' + proxyhost + proxyselector
            if data is None:
                return self.open(newurl)
            return self.open(newurl, data)
            return

    def retry_http_basic_auth(self, url, realm, data=None):
        host, selector = splithost(url)
        i = host.find(b'@') + 1
        host = host[i:]
        user, passwd = self.get_user_passwd(host, realm, i)
        if not (user or passwd):
            return
        else:
            host = quote(user, safe=b'') + b':' + quote(passwd, safe=b'') + b'@' + host
            newurl = b'http://' + host + selector
            if data is None:
                return self.open(newurl)
            return self.open(newurl, data)
            return

    def retry_https_basic_auth(self, url, realm, data=None):
        host, selector = splithost(url)
        i = host.find(b'@') + 1
        host = host[i:]
        user, passwd = self.get_user_passwd(host, realm, i)
        if not (user or passwd):
            return
        else:
            host = quote(user, safe=b'') + b':' + quote(passwd, safe=b'') + b'@' + host
            newurl = b'https://' + host + selector
            if data is None:
                return self.open(newurl)
            return self.open(newurl, data)
            return

    def get_user_passwd(self, host, realm, clear_cache=0):
        key = realm + b'@' + host.lower()
        if key in self.auth_cache:
            if clear_cache:
                del self.auth_cache[key]
            else:
                return self.auth_cache[key]
        user, passwd = self.prompt_user_passwd(host, realm)
        if user or passwd:
            self.auth_cache[key] = (user, passwd)
        return (
         user, passwd)

    def prompt_user_passwd(self, host, realm):
        import getpass
        try:
            user = raw_input(b'Enter username for %s at %s: ' % (realm,
             host))
            passwd = getpass.getpass(b'Enter password for %s in %s at %s: ' % (
             user, realm, host))
            return (user, passwd)
        except KeyboardInterrupt:
            print
            return (None, None)

        return


_localhost = None

def localhost():
    global _localhost
    if _localhost is None:
        _localhost = socket.gethostbyname(b'localhost')
    return _localhost


_thishost = None

def thishost():
    global _thishost
    if _thishost is None:
        try:
            _thishost = socket.gethostbyname(socket.gethostname())
        except socket.gaierror:
            _thishost = socket.gethostbyname(b'localhost')

    return _thishost


_ftperrors = None

def ftperrors():
    global _ftperrors
    if _ftperrors is None:
        import ftplib
        _ftperrors = ftplib.all_errors
    return _ftperrors


_noheaders = None

def noheaders():
    global _noheaders
    if _noheaders is None:
        import mimetools
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO

        _noheaders = mimetools.Message(StringIO(), 0)
        _noheaders.fp.close()
    return _noheaders


class ftpwrapper():

    def __init__(self, user, passwd, host, port, dirs, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, persistent=True):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.dirs = dirs
        self.timeout = timeout
        self.refcount = 0
        self.keepalive = persistent
        try:
            self.init()
        except:
            self.close()
            raise

        return

    def init(self):
        import ftplib
        self.busy = 0
        self.ftp = ftplib.FTP()
        self.ftp.connect(self.host, self.port, self.timeout)
        self.ftp.login(self.user, self.passwd)
        _target = (b'/').join(self.dirs)
        self.ftp.cwd(_target)
        return

    def retrfile(self, file, type):
        import ftplib
        self.endtransfer()
        if type in (b'd', b'D'):
            cmd = b'TYPE A'
            isdir = 1
        else:
            cmd = b'TYPE ' + type
            isdir = 0
        try:
            self.ftp.voidcmd(cmd)
        except ftplib.all_errors:
            self.init()
            self.ftp.voidcmd(cmd)

        conn = None
        if file and not isdir:
            try:
                cmd = b'RETR ' + file
                conn, retrlen = self.ftp.ntransfercmd(cmd)
            except ftplib.error_perm as reason:
                if str(reason)[:3] != b'550':
                    raise IOError, (b'ftp error', reason), sys.exc_info()[2]

        if not conn:
            self.ftp.voidcmd(b'TYPE A')
            if file:
                pwd = self.ftp.pwd()
                try:
                    try:
                        self.ftp.cwd(file)
                    except ftplib.error_perm as reason:
                        raise IOError, (b'ftp error', reason), sys.exc_info()[2]

                finally:
                    self.ftp.cwd(pwd)

                cmd = b'LIST ' + file
            else:
                cmd = b'LIST'
            conn, retrlen = self.ftp.ntransfercmd(cmd)
        self.busy = 1
        ftpobj = addclosehook(conn.makefile(b'rb'), self.file_close)
        self.refcount += 1
        conn.close()
        return (
         ftpobj, retrlen)

    def endtransfer(self):
        if not self.busy:
            return
        self.busy = 0
        try:
            self.ftp.voidresp()
        except ftperrors():
            pass

        return

    def close(self):
        self.keepalive = False
        if self.refcount <= 0:
            self.real_close()
        return

    def file_close(self):
        self.endtransfer()
        self.refcount -= 1
        if self.refcount <= 0 and not self.keepalive:
            self.real_close()
        return

    def real_close(self):
        self.endtransfer()
        try:
            self.ftp.close()
        except ftperrors():
            pass

        return


class addbase():

    def __init__(self, fp):
        self.fp = fp
        self.read = self.fp.read
        self.readline = self.fp.readline
        if hasattr(self.fp, b'readlines'):
            self.readlines = self.fp.readlines
        if hasattr(self.fp, b'fileno'):
            self.fileno = self.fp.fileno
        else:
            self.fileno = lambda : None
        if hasattr(self.fp, b'__iter__'):
            self.__iter__ = self.fp.__iter__
            if hasattr(self.fp, b'next'):
                self.next = self.fp.next
        return

    def __repr__(self):
        return b'<%s at %r whose fp = %r>' % (self.__class__.__name__,
         id(self), self.fp)

    def close(self):
        self.read = None
        self.readline = None
        self.readlines = None
        self.fileno = None
        if self.fp:
            self.fp.close()
        self.fp = None
        return


class addclosehook(addbase):

    def __init__(self, fp, closehook, *hookargs):
        addbase.__init__(self, fp)
        self.closehook = closehook
        self.hookargs = hookargs
        return

    def close(self):
        try:
            closehook = self.closehook
            hookargs = self.hookargs
            if closehook:
                self.closehook = None
                self.hookargs = None
                closehook(*hookargs)
        finally:
            addbase.close(self)

        return


class addinfo(addbase):

    def __init__(self, fp, headers):
        addbase.__init__(self, fp)
        self.headers = headers
        return

    def info(self):
        return self.headers


class addinfourl(addbase):

    def __init__(self, fp, headers, url, code=None):
        addbase.__init__(self, fp)
        self.headers = headers
        self.url = url
        self.code = code
        return

    def info(self):
        return self.headers

    def getcode(self):
        return self.code

    def geturl(self):
        return self.url


try:
    unicode
except NameError:

    def _is_unicode(x):
        return 0


else:

    def _is_unicode(x):
        return isinstance(x, unicode)


def toBytes(url):
    if _is_unicode(url):
        try:
            url = url.encode(b'ASCII')
        except UnicodeError:
            raise UnicodeError(b'URL ' + repr(url) + b' contains non-ASCII characters')

    return url


def unwrap(url):
    url = url.strip()
    if url[:1] == b'<' and url[-1:] == b'>':
        url = url[1:-1].strip()
    if url[:4] == b'URL:':
        url = url[4:].strip()
    return url


_typeprog = None

def splittype(url):
    global _typeprog
    if _typeprog is None:
        import re
        _typeprog = re.compile(b'^([^/:]+):')
    match = _typeprog.match(url)
    if match:
        scheme = match.group(1)
        return (
         scheme.lower(), url[len(scheme) + 1:])
    else:
        return (
         None, url)


_hostprog = None

def splithost(url):
    global _hostprog
    if _hostprog is None:
        _hostprog = re.compile(b'//([^/#?]*)(.*)', re.DOTALL)
    match = _hostprog.match(url)
    if match:
        host_port = match.group(1)
        path = match.group(2)
        if path and not path.startswith(b'/'):
            path = b'/' + path
        return (host_port, path)
    else:
        return (
         None, url)


_userprog = None

def splituser(host):
    global _userprog
    if _userprog is None:
        import re
        _userprog = re.compile(b'^(.*)@(.*)$')
    match = _userprog.match(host)
    if match:
        return match.group(1, 2)
    else:
        return (
         None, host)


_passwdprog = None

def splitpasswd(user):
    global _passwdprog
    if _passwdprog is None:
        import re
        _passwdprog = re.compile(b'^([^:]*):(.*)$', re.S)
    match = _passwdprog.match(user)
    if match:
        return match.group(1, 2)
    else:
        return (
         user, None)


_portprog = None

def splitport(host):
    global _portprog
    if _portprog is None:
        import re
        _portprog = re.compile(b'^(.*):([0-9]*)$')
    match = _portprog.match(host)
    if match:
        host, port = match.groups()
        if port:
            return (host, port)
    return (
     host, None)


_nportprog = None

def splitnport(host, defport=-1):
    global _nportprog
    if _nportprog is None:
        import re
        _nportprog = re.compile(b'^(.*):(.*)$')
    match = _nportprog.match(host)
    if match:
        host, port = match.group(1, 2)
        if port:
            try:
                nport = int(port)
            except ValueError:
                nport = None

            return (host, nport)
    return (
     host, defport)


_queryprog = None

def splitquery(url):
    global _queryprog
    if _queryprog is None:
        import re
        _queryprog = re.compile(b'^(.*)\\?([^?]*)$')
    match = _queryprog.match(url)
    if match:
        return match.group(1, 2)
    else:
        return (
         url, None)


_tagprog = None

def splittag(url):
    global _tagprog
    if _tagprog is None:
        import re
        _tagprog = re.compile(b'^(.*)#([^#]*)$')
    match = _tagprog.match(url)
    if match:
        return match.group(1, 2)
    else:
        return (
         url, None)


def splitattr(url):
    words = url.split(b';')
    return (words[0], words[1:])


_valueprog = None

def splitvalue(attr):
    global _valueprog
    if _valueprog is None:
        import re
        _valueprog = re.compile(b'^([^=]*)=(.*)$')
    match = _valueprog.match(attr)
    if match:
        return match.group(1, 2)
    else:
        return (
         attr, None)


_hexdig = b'0123456789ABCDEFabcdef'
_hextochr = dict((a + b, chr(int(a + b, 16))) for a in _hexdig for b in _hexdig)
_asciire = re.compile(b'([\x00-\x7f]+)')

def unquote(s):
    if _is_unicode(s):
        if b'%' not in s:
            return s
        bits = _asciire.split(s)
        res = [bits[0]]
        append = res.append
        for i in range(1, len(bits), 2):
            append(unquote(str(bits[i])).decode(b'latin1'))
            append(bits[i + 1])

        return (b'').join(res)
    bits = s.split(b'%')
    if len(bits) == 1:
        return s
    res = [
     bits[0]]
    append = res.append
    for item in bits[1:]:
        try:
            append(_hextochr[item[:2]])
            append(item[2:])
        except KeyError:
            append(b'%')
            append(item)

    return (b'').join(res)


def unquote_plus(s):
    s = s.replace(b'+', b' ')
    return unquote(s)


always_safe = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-'
_safe_map = {}
for i, c in zip(xrange(256), str(bytearray(xrange(256)))):
    _safe_map[c] = c if i < 128 and c in always_safe else (b'%{:02X}').format(i)

_safe_quoters = {}

def quote(s, safe=b'/'):
    if not s:
        if s is None:
            raise TypeError(b'None object cannot be quoted')
        return s
    cachekey = (
     safe, always_safe)
    try:
        quoter, safe = _safe_quoters[cachekey]
    except KeyError:
        safe_map = _safe_map.copy()
        safe_map.update([(c, c) for c in safe])
        quoter = safe_map.__getitem__
        safe = always_safe + safe
        _safe_quoters[cachekey] = (quoter, safe)

    if not s.rstrip(safe):
        return s
    else:
        return (b'').join(map(quoter, s))


def quote_plus(s, safe=b''):
    if b' ' in s:
        s = quote(s, safe + b' ')
        return s.replace(b' ', b'+')
    return quote(s, safe)


def urlencode(query, doseq=0):
    if hasattr(query, b'items'):
        query = query.items()
    else:
        try:
            if len(query) and not isinstance(query[0], tuple):
                raise TypeError
        except TypeError:
            ty, va, tb = sys.exc_info()
            raise TypeError, b'not a valid non-string sequence or mapping object', tb

    l = []
    if not doseq:
        for k, v in query:
            k = quote_plus(str(k))
            v = quote_plus(str(v))
            l.append(k + b'=' + v)

    else:
        for k, v in query:
            k = quote_plus(str(k))
            if isinstance(v, str):
                v = quote_plus(v)
                l.append(k + b'=' + v)
            elif _is_unicode(v):
                v = quote_plus(v.encode(b'ASCII', b'replace'))
                l.append(k + b'=' + v)
            else:
                try:
                    len(v)
                except TypeError:
                    v = quote_plus(str(v))
                    l.append(k + b'=' + v)

                for elt in v:
                    l.append(k + b'=' + quote_plus(str(elt)))

    return (b'&').join(l)


def getproxies_environment():
    proxies = {}
    for name, value in os.environ.items():
        name = name.lower()
        if value and name[-6:] == b'_proxy':
            proxies[name[:-6]] = value

    if b'REQUEST_METHOD' in os.environ:
        proxies.pop(b'http', None)
    for name, value in os.environ.items():
        if name[-6:] == b'_proxy':
            name = name.lower()
            if value:
                proxies[name[:-6]] = value
            else:
                proxies.pop(name[:-6], None)

    return proxies


def proxy_bypass_environment(host, proxies=None):
    if proxies is None:
        proxies = getproxies_environment()
    try:
        no_proxy = proxies[b'no']
    except KeyError:
        return 0

    if no_proxy == b'*':
        return 1
    else:
        hostonly, port = splitport(host)
        no_proxy_list = [proxy.strip() for proxy in no_proxy.split(b',')]
        for name in no_proxy_list:
            if name:
                name = name.lstrip(b'.')
                name = re.escape(name)
                pattern = b'(.+\\.)?%s$' % name
                if re.match(pattern, hostonly, re.I) or re.match(pattern, host, re.I):
                    return 1

        return 0


if sys.platform == b'darwin':
    from _scproxy import _get_proxy_settings, _get_proxies

    def proxy_bypass_macosx_sysconf(host):
        import re, socket
        from fnmatch import fnmatch
        hostonly, port = splitport(host)

        def ip2num(ipAddr):
            parts = ipAddr.split(b'.')
            parts = map(int, parts)
            if len(parts) != 4:
                parts = (parts + [0, 0, 0, 0])[:4]
            return parts[0] << 24 | parts[1] << 16 | parts[2] << 8 | parts[3]

        proxy_settings = _get_proxy_settings()
        if b'.' not in host:
            if proxy_settings[b'exclude_simple']:
                return True
        hostIP = None
        for value in proxy_settings.get(b'exceptions', ()):
            if not value:
                continue
            m = re.match(b'(\\d+(?:\\.\\d+)*)(/\\d+)?', value)
            if m is not None:
                if hostIP is None:
                    try:
                        hostIP = socket.gethostbyname(hostonly)
                        hostIP = ip2num(hostIP)
                    except socket.error:
                        continue

                base = ip2num(m.group(1))
                mask = m.group(2)
                if mask is None:
                    mask = 8 * (m.group(1).count(b'.') + 1)
                else:
                    mask = int(mask[1:])
                mask = 32 - mask
                if hostIP >> mask == base >> mask:
                    return True
            elif fnmatch(host, value):
                return True

        return False


    def getproxies_macosx_sysconf():
        return _get_proxies()


    def proxy_bypass(host):
        proxies = getproxies_environment()
        if proxies:
            return proxy_bypass_environment(host, proxies)
        else:
            return proxy_bypass_macosx_sysconf(host)

        return


    def getproxies():
        return getproxies_environment() or getproxies_macosx_sysconf()


elif os.name == b'nt':

    def getproxies_registry():
        proxies = {}
        try:
            import _winreg
        except ImportError:
            return proxies

        try:
            internetSettings = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, b'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings')
            proxyEnable = _winreg.QueryValueEx(internetSettings, b'ProxyEnable')[0]
            if proxyEnable:
                proxyServer = str(_winreg.QueryValueEx(internetSettings, b'ProxyServer')[0])
                if b'=' in proxyServer:
                    for p in proxyServer.split(b';'):
                        protocol, address = p.split(b'=', 1)
                        import re
                        if not re.match(b'^([^/:]+)://', address):
                            address = b'%s://%s' % (protocol, address)
                        proxies[protocol] = address

                elif proxyServer[:5] == b'http:':
                    proxies[b'http'] = proxyServer
                else:
                    proxies[b'http'] = b'http://%s' % proxyServer
                    proxies[b'https'] = b'https://%s' % proxyServer
                    proxies[b'ftp'] = b'ftp://%s' % proxyServer
            internetSettings.Close()
        except (WindowsError, ValueError, TypeError):
            pass

        return proxies


    def getproxies():
        return getproxies_environment() or getproxies_registry()


    def proxy_bypass_registry(host):
        try:
            import _winreg, re
        except ImportError:
            return 0

        try:
            internetSettings = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, b'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings')
            proxyEnable = _winreg.QueryValueEx(internetSettings, b'ProxyEnable')[0]
            proxyOverride = str(_winreg.QueryValueEx(internetSettings, b'ProxyOverride')[0])
        except WindowsError:
            return 0

        if not proxyEnable or not proxyOverride:
            return 0
        rawHost, port = splitport(host)
        host = [rawHost]
        try:
            addr = socket.gethostbyname(rawHost)
            if addr != rawHost:
                host.append(addr)
        except socket.error:
            pass

        try:
            fqdn = socket.getfqdn(rawHost)
            if fqdn != rawHost:
                host.append(fqdn)
        except socket.error:
            pass

        proxyOverride = proxyOverride.split(b';')
        for test in proxyOverride:
            if test == b'<local>':
                if b'.' not in rawHost:
                    return 1
            test = test.replace(b'.', b'\\.')
            test = test.replace(b'*', b'.*')
            test = test.replace(b'?', b'.')
            for val in host:
                if re.match(test, val, re.I):
                    return 1

        return 0


    def proxy_bypass(host):
        proxies = getproxies_environment()
        if proxies:
            return proxy_bypass_environment(host, proxies)
        else:
            return proxy_bypass_registry(host)

        return


else:
    getproxies = getproxies_environment
    proxy_bypass = proxy_bypass_environment

def test1():
    s = b''
    for i in range(256):
        s = s + chr(i)

    s = s * 4
    t0 = time.time()
    qs = quote(s)
    uqs = unquote(qs)
    t1 = time.time()
    if uqs != s:
        print b'Wrong!'
    print repr(s)
    print repr(qs)
    print repr(uqs)
    print round(t1 - t0, 3), b'sec'
    return


def reporthook(blocknum, blocksize, totalsize):
    print b'Block number: %d, Block size: %d, Total size: %d' % (
     blocknum, blocksize, totalsize)
    return
