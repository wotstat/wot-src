import posixpath
__all__ = [
 2, 3, 4, 5, 
 6, 7]

class FileWrapper:

    def __init__(self, filelike, blksize=8192):
        self.filelike = filelike
        self.blksize = blksize
        if hasattr(filelike, b'close'):
            self.close = filelike.close
        return

    def __getitem__(self, key):
        data = self.filelike.read(self.blksize)
        if data:
            return data
        raise IndexError
        return

    def __iter__(self):
        return self

    def next(self):
        data = self.filelike.read(self.blksize)
        if data:
            return data
        raise StopIteration
        return


def guess_scheme(environ):
    if environ.get(b'HTTPS') in (b'yes', b'on', b'1'):
        return b'https'
    else:
        return b'http'

    return


def application_uri(environ):
    url = environ[b'wsgi.url_scheme'] + b'://'
    from urllib import quote
    if environ.get(b'HTTP_HOST'):
        url += environ[b'HTTP_HOST']
    else:
        url += environ[b'SERVER_NAME']
        if environ[b'wsgi.url_scheme'] == b'https':
            if environ[b'SERVER_PORT'] != b'443':
                url += b':' + environ[b'SERVER_PORT']
        elif environ[b'SERVER_PORT'] != b'80':
            url += b':' + environ[b'SERVER_PORT']
    url += quote(environ.get(b'SCRIPT_NAME') or b'/')
    return url


def request_uri(environ, include_query=1):
    url = application_uri(environ)
    from urllib import quote
    path_info = quote(environ.get(b'PATH_INFO', b''), safe=b'/;=,')
    if not environ.get(b'SCRIPT_NAME'):
        url += path_info[1:]
    else:
        url += path_info
    if include_query and environ.get(b'QUERY_STRING'):
        url += b'?' + environ[b'QUERY_STRING']
    return url


def shift_path_info(environ):
    path_info = environ.get(b'PATH_INFO', b'')
    if not path_info:
        return
    else:
        path_parts = path_info.split(b'/')
        path_parts[1:(-1)] = [p for p in path_parts[1:-1] if p and p != b'.']
        name = path_parts[1]
        del path_parts[1]
        script_name = environ.get(b'SCRIPT_NAME', b'')
        script_name = posixpath.normpath(script_name + b'/' + name)
        if script_name.endswith(b'/'):
            script_name = script_name[:-1]
        if not name and not script_name.endswith(b'/'):
            script_name += b'/'
        environ[b'SCRIPT_NAME'] = script_name
        environ[b'PATH_INFO'] = (b'/').join(path_parts)
        if name == b'.':
            name = None
        return name


def setup_testing_defaults(environ):
    environ.setdefault(b'SERVER_NAME', b'127.0.0.1')
    environ.setdefault(b'SERVER_PROTOCOL', b'HTTP/1.0')
    environ.setdefault(b'HTTP_HOST', environ[b'SERVER_NAME'])
    environ.setdefault(b'REQUEST_METHOD', b'GET')
    if b'SCRIPT_NAME' not in environ and b'PATH_INFO' not in environ:
        environ.setdefault(b'SCRIPT_NAME', b'')
        environ.setdefault(b'PATH_INFO', b'/')
    environ.setdefault(b'wsgi.version', (1, 0))
    environ.setdefault(b'wsgi.run_once', 0)
    environ.setdefault(b'wsgi.multithread', 0)
    environ.setdefault(b'wsgi.multiprocess', 0)
    from StringIO import StringIO
    environ.setdefault(b'wsgi.input', StringIO(b''))
    environ.setdefault(b'wsgi.errors', StringIO())
    environ.setdefault(b'wsgi.url_scheme', guess_scheme(environ))
    if environ[b'wsgi.url_scheme'] == b'http':
        environ.setdefault(b'SERVER_PORT', b'80')
    elif environ[b'wsgi.url_scheme'] == b'https':
        environ.setdefault(b'SERVER_PORT', b'443')
    return


_hoppish = {b'connection': 1, 
   b'keep-alive': 1, b'proxy-authenticate': 1, b'proxy-authorization': 1, 
   b'te': 1, b'trailers': 1, b'transfer-encoding': 1, b'upgrade': 1}.__contains__

def is_hop_by_hop(header_name):
    return _hoppish(header_name.lower())
