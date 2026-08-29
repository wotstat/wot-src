__version__ = b'0.6'
__all__ = [
 b'SimpleHTTPRequestHandler']
import os, posixpath, BaseHTTPServer, urllib, urlparse, cgi, sys, shutil, mimetypes
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

class SimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    server_version = b'SimpleHTTP/' + __version__

    def do_GET(self):
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()

        return

    def do_HEAD(self):
        f = self.send_head()
        if f:
            f.close()
        return

    def send_head(self):
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            parts = urlparse.urlsplit(self.path)
            if not parts.path.endswith(b'/'):
                self.send_response(301)
                new_parts = (parts[0], parts[1], parts[2] + b'/',
                 parts[3], parts[4])
                new_url = urlparse.urlunsplit(new_parts)
                self.send_header(b'Location', new_url)
                self.end_headers()
                return
            for index in (b'index.html', b'index.htm'):
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)

        ctype = self.guess_type(path)
        try:
            f = open(path, b'rb')
        except IOError:
            self.send_error(404, b'File not found')
            return

        try:
            self.send_response(200)
            self.send_header(b'Content-type', ctype)
            fs = os.fstat(f.fileno())
            self.send_header(b'Content-Length', str(fs[6]))
            self.send_header(b'Last-Modified', self.date_time_string(fs.st_mtime))
            self.end_headers()
            return f
        except:
            f.close()
            raise

        return

    def list_directory(self, path):
        try:
            list = os.listdir(path)
        except os.error:
            self.send_error(404, b'No permission to list directory')
            return

        list.sort(key=(lambda a: a.lower()))
        f = StringIO()
        displaypath = cgi.escape(urllib.unquote(self.path))
        f.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write(b'<html>\n<title>Directory listing for %s</title>\n' % displaypath)
        f.write(b'<body>\n<h2>Directory listing for %s</h2>\n' % displaypath)
        f.write(b'<hr>\n<ul>\n')
        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            if os.path.isdir(fullname):
                displayname = name + b'/'
                linkname = name + b'/'
            if os.path.islink(fullname):
                displayname = name + b'@'
            f.write(b'<li><a href="%s">%s</a>\n' % (
             urllib.quote(linkname), cgi.escape(displayname)))

        f.write(b'</ul>\n<hr>\n</body>\n</html>\n')
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header(b'Content-type', b'text/html; charset=%s' % encoding)
        self.send_header(b'Content-Length', str(length))
        self.end_headers()
        return f

    def translate_path(self, path):
        path = path.split(b'?', 1)[0]
        path = path.split(b'#', 1)[0]
        trailing_slash = path.rstrip().endswith(b'/')
        path = posixpath.normpath(urllib.unquote(path))
        words = path.split(b'/')
        words = filter(None, words)
        path = os.getcwd()
        for word in words:
            if os.path.dirname(word) or word in (os.curdir, os.pardir):
                continue
            path = os.path.join(path, word)

        if trailing_slash:
            path += b'/'
        return path

    def copyfile(self, source, outputfile):
        shutil.copyfileobj(source, outputfile)
        return

    def guess_type(self, path):
        base, ext = posixpath.splitext(path)
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        else:
            ext = ext.lower()
            if ext in self.extensions_map:
                return self.extensions_map[ext]
            return self.extensions_map[b'']

        return

    if not mimetypes.inited:
        mimetypes.init()
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({b'': b'application/octet-stream', 
       b'.py': b'text/plain', 
       b'.c': b'text/plain', 
       b'.h': b'text/plain'})


def test(HandlerClass=SimpleHTTPRequestHandler, ServerClass=BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)
    return


if __name__ == b'__main__':
    test()
