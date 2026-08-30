__version__ = b'0.4'
__all__ = [
 b'CGIHTTPRequestHandler']
import os, sys, urllib, BaseHTTPServer, SimpleHTTPServer, select, copy

class CGIHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    have_fork = hasattr(os, b'fork')
    have_popen2 = hasattr(os, b'popen2')
    have_popen3 = hasattr(os, b'popen3')
    rbufsize = 0

    def do_POST(self):
        if self.is_cgi():
            self.run_cgi()
        else:
            self.send_error(501, b'Can only POST to CGI scripts')
        return

    def send_head(self):
        if self.is_cgi():
            return self.run_cgi()
        else:
            return SimpleHTTPServer.SimpleHTTPRequestHandler.send_head(self)

        return

    def is_cgi(self):
        collapsed_path = _url_collapse_path(self.path)
        dir_sep = collapsed_path.find(b'/', 1)
        head, tail = collapsed_path[:dir_sep], collapsed_path[dir_sep + 1:]
        if head in self.cgi_directories:
            self.cgi_info = (
             head, tail)
            return True
        return False

    cgi_directories = [
     b'/cgi-bin', b'/htbin']

    def is_executable(self, path):
        return executable(path)

    def is_python(self, path):
        head, tail = os.path.splitext(path)
        return tail.lower() in (b'.py', b'.pyw')

    def run_cgi(self):
        dir, rest = self.cgi_info
        path = dir + b'/' + rest
        i = path.find(b'/', len(dir) + 1)
        while i >= 0:
            nextdir = path[:i]
            nextrest = path[i + 1:]
            scriptdir = self.translate_path(nextdir)
            if os.path.isdir(scriptdir):
                dir, rest = nextdir, nextrest
                i = path.find(b'/', len(dir) + 1)
            else:
                break

        rest, _, query = rest.partition(b'?')
        i = rest.find(b'/')
        if i >= 0:
            script, rest = rest[:i], rest[i:]
        else:
            script, rest = rest, b''
        scriptname = dir + b'/' + script
        scriptfile = self.translate_path(scriptname)
        if not os.path.exists(scriptfile):
            self.send_error(404, b'No such CGI script (%r)' % scriptname)
            return
        else:
            if not os.path.isfile(scriptfile):
                self.send_error(403, b'CGI script is not a plain file (%r)' % scriptname)
                return
            ispy = self.is_python(scriptname)
            if not ispy:
                if not (self.have_fork or self.have_popen2 or self.have_popen3):
                    self.send_error(403, b'CGI script is not a Python script (%r)' % scriptname)
                    return
                if not self.is_executable(scriptfile):
                    self.send_error(403, b'CGI script is not executable (%r)' % scriptname)
                    return
            env = copy.deepcopy(os.environ)
            env[b'SERVER_SOFTWARE'] = self.version_string()
            env[b'SERVER_NAME'] = self.server.server_name
            env[b'GATEWAY_INTERFACE'] = b'CGI/1.1'
            env[b'SERVER_PROTOCOL'] = self.protocol_version
            env[b'SERVER_PORT'] = str(self.server.server_port)
            env[b'REQUEST_METHOD'] = self.command
            uqrest = urllib.unquote(rest)
            env[b'PATH_INFO'] = uqrest
            env[b'PATH_TRANSLATED'] = self.translate_path(uqrest)
            env[b'SCRIPT_NAME'] = scriptname
            if query:
                env[b'QUERY_STRING'] = query
            host = self.address_string()
            if host != self.client_address[0]:
                env[b'REMOTE_HOST'] = host
            env[b'REMOTE_ADDR'] = self.client_address[0]
            authorization = self.headers.getheader(b'authorization')
            if authorization:
                authorization = authorization.split()
                if len(authorization) == 2:
                    import base64, binascii
                    env[b'AUTH_TYPE'] = authorization[0]
                    if authorization[0].lower() == b'basic':
                        try:
                            authorization = base64.decodestring(authorization[1])
                        except binascii.Error:
                            pass
                        else:
                            authorization = authorization.split(b':')
                            if len(authorization) == 2:
                                env[b'REMOTE_USER'] = authorization[0]
            if self.headers.typeheader is None:
                env[b'CONTENT_TYPE'] = self.headers.type
            else:
                env[b'CONTENT_TYPE'] = self.headers.typeheader
            length = self.headers.getheader(b'content-length')
            if length:
                env[b'CONTENT_LENGTH'] = length
            referer = self.headers.getheader(b'referer')
            if referer:
                env[b'HTTP_REFERER'] = referer
            accept = []
            for line in self.headers.getallmatchingheaders(b'accept'):
                if line[:1] in b'\t\n\r ':
                    accept.append(line.strip())
                else:
                    accept = accept + line[7:].split(b',')

            env[b'HTTP_ACCEPT'] = (b',').join(accept)
            ua = self.headers.getheader(b'user-agent')
            if ua:
                env[b'HTTP_USER_AGENT'] = ua
            co = filter(None, self.headers.getheaders(b'cookie'))
            if co:
                env[b'HTTP_COOKIE'] = (b', ').join(co)
            for k in (b'QUERY_STRING', b'REMOTE_HOST', b'CONTENT_LENGTH', b'HTTP_USER_AGENT', b'HTTP_COOKIE', b'HTTP_REFERER'):
                env.setdefault(k, b'')

            self.send_response(200, b'Script output follows')
            decoded_query = query.replace(b'+', b' ')
            if self.have_fork:
                args = [script]
                if b'=' not in decoded_query:
                    args.append(decoded_query)
                nobody = nobody_uid()
                self.wfile.flush()
                pid = os.fork()
                if pid != 0:
                    pid, sts = os.waitpid(pid, 0)
                    while select.select([self.rfile], [], [], 0)[0]:
                        if not self.rfile.read(1):
                            break

                    if sts:
                        self.log_error(b'CGI script exit status %#x', sts)
                    return
                try:
                    try:
                        os.setuid(nobody)
                    except os.error:
                        pass

                    os.dup2(self.rfile.fileno(), 0)
                    os.dup2(self.wfile.fileno(), 1)
                    os.execve(scriptfile, args, env)
                except:
                    self.server.handle_error(self.request, self.client_address)
                    os._exit(127)

            else:
                import subprocess
                cmdline = [
                 scriptfile]
                if self.is_python(scriptfile):
                    interp = sys.executable
                    if interp.lower().endswith(b'w.exe'):
                        interp = interp[:-5] + interp[-4:]
                    cmdline = [
                     interp, b'-u'] + cmdline
                if b'=' not in query:
                    cmdline.append(query)
                self.log_message(b'command: %s', subprocess.list2cmdline(cmdline))
                try:
                    nbytes = int(length)
                except (TypeError, ValueError):
                    nbytes = 0

                p = subprocess.Popen(cmdline, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
                if self.command.lower() == b'post' and nbytes > 0:
                    data = self.rfile.read(nbytes)
                else:
                    data = None
                while select.select([self.rfile._sock], [], [], 0)[0]:
                    if not self.rfile._sock.recv(1):
                        break

                stdout, stderr = p.communicate(data)
                self.wfile.write(stdout)
                if stderr:
                    self.log_error(b'%s', stderr)
                p.stderr.close()
                p.stdout.close()
                status = p.returncode
                if status:
                    self.log_error(b'CGI script exit status %#x', status)
                else:
                    self.log_message(b'CGI script exited OK')
            return


def _url_collapse_path(path):
    path, _, query = path.partition(b'?')
    path = urllib.unquote(path)
    path_parts = path.split(b'/')
    head_parts = []
    for part in path_parts[:-1]:
        if part == b'..':
            head_parts.pop()
        elif part and part != b'.':
            head_parts.append(part)

    if path_parts:
        tail_part = path_parts.pop()
        if tail_part:
            if tail_part == b'..':
                head_parts.pop()
                tail_part = b''
            elif tail_part == b'.':
                tail_part = b''
    else:
        tail_part = b''
    if query:
        tail_part = (b'?').join((tail_part, query))
    splitpath = (b'/' + (b'/').join(head_parts), tail_part)
    collapsed_path = (b'/').join(splitpath)
    return collapsed_path


nobody = None

def nobody_uid():
    global nobody
    if nobody:
        return nobody
    try:
        import pwd
    except ImportError:
        return -1

    try:
        nobody = pwd.getpwnam(b'nobody')[2]
    except KeyError:
        nobody = 1 + max(map((lambda x: x[2]), pwd.getpwall()))

    return nobody


def executable(path):
    try:
        st = os.stat(path)
    except os.error:
        return False

    return st.st_mode & 73 != 0


def test(HandlerClass=CGIHTTPRequestHandler, ServerClass=BaseHTTPServer.HTTPServer):
    SimpleHTTPServer.test(HandlerClass, ServerClass)
    return


if __name__ == b'__main__':
    test()
