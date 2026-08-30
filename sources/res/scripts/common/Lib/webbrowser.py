import os, shlex, sys, stat, subprocess, time
__all__ = [
 2, 3, 4, 5, 6, 7]

class Error(Exception):
    pass


_browsers = {}
_tryorder = []

def register(name, klass, instance=None, update_tryorder=1):
    _browsers[name.lower()] = [
     klass, instance]
    if update_tryorder > 0:
        _tryorder.append(name)
    elif update_tryorder < 0:
        _tryorder.insert(0, name)
    return


def get(using=None):
    if using is not None:
        alternatives = [
         using]
    else:
        alternatives = _tryorder
    for browser in alternatives:
        if b'%s' in browser:
            browser = shlex.split(browser)
            if browser[-1] == b'&':
                return BackgroundBrowser(browser[:-1])
            return GenericBrowser(browser)
        else:
            try:
                command = _browsers[browser.lower()]
            except KeyError:
                command = _synthesize(browser)

            if command[1] is not None:
                return command[1]
            if command[0] is not None:
                return command[0]()

    raise Error(b'could not locate runnable browser')
    return


def open(url, new=0, autoraise=True):
    for name in _tryorder:
        browser = get(name)
        if browser.open(url, new, autoraise):
            return True

    return False


def open_new(url):
    return open(url, 1)


def open_new_tab(url):
    return open(url, 2)


def _synthesize(browser, update_tryorder=1):
    cmd = browser.split()[0]
    if not _iscommand(cmd):
        return [None, None]
    else:
        name = os.path.basename(cmd)
        try:
            command = _browsers[name.lower()]
        except KeyError:
            return [
             None, None]

        controller = command[1]
        if controller and name.lower() == controller.basename:
            import copy
            controller = copy.copy(controller)
            controller.name = browser
            controller.basename = os.path.basename(browser)
            register(browser, None, controller, update_tryorder)
            return [
             None, controller]
        return [
         None, None]


if sys.platform[:3] == b'win':

    def _isexecutable(cmd):
        cmd = cmd.lower()
        if os.path.isfile(cmd) and cmd.endswith((b'.exe', b'.bat')):
            return True
        for ext in (b'.exe', b'.bat'):
            if os.path.isfile(cmd + ext):
                return True

        return False


else:

    def _isexecutable(cmd):
        if os.path.isfile(cmd):
            mode = os.stat(cmd)[stat.ST_MODE]
            if mode & stat.S_IXUSR or mode & stat.S_IXGRP or mode & stat.S_IXOTH:
                return True
        return False


def _iscommand(cmd):
    if _isexecutable(cmd):
        return True
    path = os.environ.get(b'PATH')
    if not path:
        return False
    for d in path.split(os.pathsep):
        exe = os.path.join(d, cmd)
        if _isexecutable(exe):
            return True

    return False


class BaseBrowser(object):
    args = [
     b'%s']

    def __init__(self, name=b''):
        self.name = name
        self.basename = name
        return

    def open(self, url, new=0, autoraise=True):
        raise NotImplementedError
        return

    def open_new(self, url):
        return self.open(url, 1)

    def open_new_tab(self, url):
        return self.open(url, 2)


class GenericBrowser(BaseBrowser):

    def __init__(self, name):
        if isinstance(name, basestring):
            self.name = name
            self.args = [b'%s']
        else:
            self.name = name[0]
            self.args = name[1:]
        self.basename = os.path.basename(self.name)
        return

    def open(self, url, new=0, autoraise=True):
        cmdline = [self.name] + [arg.replace(b'%s', url) for arg in self.args]
        try:
            if sys.platform[:3] == b'win':
                p = subprocess.Popen(cmdline)
            else:
                p = subprocess.Popen(cmdline, close_fds=True)
            return not p.wait()
        except OSError:
            return False

        return


class BackgroundBrowser(GenericBrowser):

    def open(self, url, new=0, autoraise=True):
        cmdline = [self.name] + [arg.replace(b'%s', url) for arg in self.args]
        try:
            if sys.platform[:3] == b'win':
                p = subprocess.Popen(cmdline)
            else:
                setsid = getattr(os, b'setsid', None)
                if not setsid:
                    setsid = getattr(os, b'setpgrp', None)
                p = subprocess.Popen(cmdline, close_fds=True, preexec_fn=setsid)
            return p.poll() is None
        except OSError:
            return False

        return


class UnixBrowser(BaseBrowser):
    raise_opts = None
    remote_args = [b'%action', b'%s']
    remote_action = None
    remote_action_newwin = None
    remote_action_newtab = None
    background = False
    redirect_stdout = True

    def _invoke(self, args, remote, autoraise):
        raise_opt = []
        if remote and self.raise_opts:
            autoraise = int(autoraise)
            opt = self.raise_opts[autoraise]
            if opt:
                raise_opt = [opt]
        cmdline = [
         self.name] + raise_opt + args
        if remote or self.background:
            inout = file(os.devnull, b'r+')
        else:
            inout = None
        setsid = getattr(os, b'setsid', None)
        if not setsid:
            setsid = getattr(os, b'setpgrp', None)
        p = subprocess.Popen(cmdline, close_fds=True, stdin=inout, stdout=self.redirect_stdout and inout or None, stderr=inout, preexec_fn=setsid)
        if remote:
            time.sleep(1)
            rc = p.poll()
            if rc is None:
                time.sleep(4)
                rc = p.poll()
                if rc is None:
                    return True
            return not rc
        else:
            if self.background:
                if p.poll() is None:
                    return True
                else:
                    return False

            else:
                return not p.wait()
            return

    def open(self, url, new=0, autoraise=True):
        if new == 0:
            action = self.remote_action
        elif new == 1:
            action = self.remote_action_newwin
        elif new == 2:
            if self.remote_action_newtab is None:
                action = self.remote_action_newwin
            else:
                action = self.remote_action_newtab
        else:
            raise Error(b"Bad 'new' parameter to open(); " + b'expected 0, 1, or 2, got %s' % new)
        args = [arg.replace(b'%s', url).replace(b'%action', action) for arg in self.remote_args]
        success = self._invoke(args, True, autoraise)
        if not success:
            args = [arg.replace(b'%s', url) for arg in self.args]
            return self._invoke(args, False, False)
        else:
            return True
            return


class Mozilla(UnixBrowser):
    raise_opts = [
     b'-noraise', b'-raise']
    remote_args = [b'-remote', b'openURL(%s%action)']
    remote_action = b''
    remote_action_newwin = b',new-window'
    remote_action_newtab = b',new-tab'
    background = True


Netscape = Mozilla

class Galeon(UnixBrowser):
    raise_opts = [
     b'-noraise', b'']
    remote_args = [b'%action', b'%s']
    remote_action = b'-n'
    remote_action_newwin = b'-w'
    background = True


class Chrome(UnixBrowser):
    remote_args = [
     b'%action', b'%s']
    remote_action = b''
    remote_action_newwin = b'--new-window'
    remote_action_newtab = b''
    background = True


Chromium = Chrome

class Opera(UnixBrowser):
    remote_args = [
     b'%action', b'%s']
    remote_action = b''
    remote_action_newwin = b'--new-window'
    remote_action_newtab = b''
    background = True


class Elinks(UnixBrowser):
    remote_args = [
     b'-remote', b'openURL(%s%action)']
    remote_action = b''
    remote_action_newwin = b',new-window'
    remote_action_newtab = b',new-tab'
    background = False
    redirect_stdout = False


class Konqueror(BaseBrowser):

    def open(self, url, new=0, autoraise=True):
        if new == 2:
            action = b'newTab'
        else:
            action = b'openURL'
        devnull = file(os.devnull, b'r+')
        setsid = getattr(os, b'setsid', None)
        if not setsid:
            setsid = getattr(os, b'setpgrp', None)
        try:
            p = subprocess.Popen([b'kfmclient', action, url], close_fds=True, stdin=devnull, stdout=devnull, stderr=devnull)
        except OSError:
            pass
        else:
            p.wait()
            return True

        try:
            p = subprocess.Popen([b'konqueror', b'--silent', url], close_fds=True, stdin=devnull, stdout=devnull, stderr=devnull, preexec_fn=setsid)
        except OSError:
            pass
        else:
            if p.poll() is None:
                return True

        try:
            p = subprocess.Popen([b'kfm', b'-d', url], close_fds=True, stdin=devnull, stdout=devnull, stderr=devnull, preexec_fn=setsid)
        except OSError:
            return False

        return p.poll() is None
        return


class Grail(BaseBrowser):

    def _find_grail_rc(self):
        import glob, pwd, socket, tempfile
        tempdir = os.path.join(tempfile.gettempdir(), b'.grail-unix')
        user = pwd.getpwuid(os.getuid())[0]
        filename = os.path.join(tempdir, user + b'-*')
        maybes = glob.glob(filename)
        if not maybes:
            return
        else:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            for fn in maybes:
                try:
                    s.connect(fn)
                except socket.error:
                    try:
                        os.unlink(fn)
                    except IOError:
                        pass

                else:
                    return s

            return

    def _remote(self, action):
        s = self._find_grail_rc()
        if not s:
            return 0
        s.send(action)
        s.close()
        return 1

    def open(self, url, new=0, autoraise=True):
        if new:
            ok = self._remote(b'LOADNEW ' + url)
        else:
            ok = self._remote(b'LOAD ' + url)
        return ok


def register_X_browsers():
    if _iscommand(b'xdg-open'):
        register(b'xdg-open', None, BackgroundBrowser(b'xdg-open'))
    if b'GNOME_DESKTOP_SESSION_ID' in os.environ and _iscommand(b'gvfs-open'):
        register(b'gvfs-open', None, BackgroundBrowser(b'gvfs-open'))
    if b'GNOME_DESKTOP_SESSION_ID' in os.environ and _iscommand(b'gnome-open'):
        register(b'gnome-open', None, BackgroundBrowser(b'gnome-open'))
    if b'KDE_FULL_SESSION' in os.environ and _iscommand(b'kfmclient'):
        register(b'kfmclient', Konqueror, Konqueror(b'kfmclient'))
    if _iscommand(b'x-www-browser'):
        register(b'x-www-browser', None, BackgroundBrowser(b'x-www-browser'))
    for browser in (b'mozilla-firefox', b'firefox', b'mozilla-firebird', b'firebird', b'iceweasel', b'iceape', b'seamonkey', b'mozilla', b'netscape'):
        if _iscommand(browser):
            register(browser, None, Mozilla(browser))

    if _iscommand(b'kfm'):
        register(b'kfm', Konqueror, Konqueror(b'kfm'))
    elif _iscommand(b'konqueror'):
        register(b'konqueror', Konqueror, Konqueror(b'konqueror'))
    for browser in (b'galeon', b'epiphany'):
        if _iscommand(browser):
            register(browser, None, Galeon(browser))

    if _iscommand(b'skipstone'):
        register(b'skipstone', None, BackgroundBrowser(b'skipstone'))
    for browser in (b'google-chrome', b'chrome', b'chromium', b'chromium-browser'):
        if _iscommand(browser):
            register(browser, None, Chrome(browser))

    if _iscommand(b'opera'):
        register(b'opera', None, Opera(b'opera'))
    if _iscommand(b'mosaic'):
        register(b'mosaic', None, BackgroundBrowser(b'mosaic'))
    if _iscommand(b'grail'):
        register(b'grail', Grail, None)
    return


if os.environ.get(b'DISPLAY'):
    register_X_browsers()
if os.environ.get(b'TERM'):
    if _iscommand(b'www-browser'):
        register(b'www-browser', None, GenericBrowser(b'www-browser'))
    if _iscommand(b'links'):
        register(b'links', None, GenericBrowser(b'links'))
    if _iscommand(b'elinks'):
        register(b'elinks', None, Elinks(b'elinks'))
    if _iscommand(b'lynx'):
        register(b'lynx', None, GenericBrowser(b'lynx'))
    if _iscommand(b'w3m'):
        register(b'w3m', None, GenericBrowser(b'w3m'))
if sys.platform[:3] == b'win':

    class WindowsDefault(BaseBrowser):

        def open(self, url, new=0, autoraise=True):
            try:
                os.startfile(url)
            except WindowsError:
                return False

            return True
            return


    _tryorder = []
    _browsers = {}
    register(b'windows-default', WindowsDefault)
    iexplore = os.path.join(os.environ.get(b'PROGRAMFILES', b'C:\\Program Files'), b'Internet Explorer\\IEXPLORE.EXE')
    for browser in (b'firefox', b'firebird', b'seamonkey', b'mozilla',
     b'netscape', b'opera', iexplore):
        if _iscommand(browser):
            register(browser, None, BackgroundBrowser(browser))

if sys.platform == b'darwin':

    class MacOSX(BaseBrowser):

        def __init__(self, name):
            self.name = name
            return

        def open(self, url, new=0, autoraise=True):
            if b':' not in url:
                url = b'file:' + url
            new = int(bool(new))
            if self.name == b'default':
                script = b'open location "%s"' % url.replace(b'"', b'%22')
            else:
                if self.name == b'OmniWeb':
                    toWindow = b''
                else:
                    toWindow = b'toWindow %d' % (new - 1)
                cmd = b'OpenURL "%s"' % url.replace(b'"', b'%22')
                script = b'tell application "%s"\n                                activate\n                                %s %s\n                            end tell' % (self.name, cmd, toWindow)
            osapipe = os.popen(b'osascript', b'w')
            if osapipe is None:
                return False
            else:
                osapipe.write(script)
                rc = osapipe.close()
                return not rc


    class MacOSXOSAScript(BaseBrowser):

        def __init__(self, name):
            self._name = name
            return

        def open(self, url, new=0, autoraise=True):
            if self._name == b'default':
                script = b'open location "%s"' % url.replace(b'"', b'%22')
            else:
                script = b'\n                   tell application "%s"\n                       activate\n                       open location "%s"\n                   end\n                   ' % (self._name, url.replace(b'"', b'%22'))
            osapipe = os.popen(b'osascript', b'w')
            if osapipe is None:
                return False
            else:
                osapipe.write(script)
                rc = osapipe.close()
                return not rc


    register(b'safari', None, MacOSXOSAScript(b'safari'), -1)
    register(b'firefox', None, MacOSXOSAScript(b'firefox'), -1)
    register(b'chrome', None, MacOSXOSAScript(b'chrome'), -1)
    register(b'MacOSX', None, MacOSXOSAScript(b'default'), -1)
if sys.platform[:3] == b'os2' and _iscommand(b'netscape'):
    _tryorder = []
    _browsers = {}
    register(b'os2netscape', None, GenericBrowser([b'start', b'netscape', b'%s']), -1)
if b'BROWSER' in os.environ:
    _userchoices = os.environ[b'BROWSER'].split(os.pathsep)
    _userchoices.reverse()
    for cmdline in _userchoices:
        if cmdline != b'':
            cmd = _synthesize(cmdline, -1)
            if cmd[1] is None:
                register(cmdline, None, GenericBrowser(cmdline), -1)

    cmdline = None
    del cmdline
    del _userchoices

def main():
    import getopt
    usage = b'Usage: %s [-n | -t] url\n    -n: open new window\n    -t: open new tab' % sys.argv[0]
    try:
        opts, args = getopt.getopt(sys.argv[1:], b'ntd')
    except getopt.error as msg:
        print >> sys.stderr, msg
        print >> sys.stderr, usage
        sys.exit(1)

    new_win = 0
    for o, a in opts:
        if o == b'-n':
            new_win = 1
        elif o == b'-t':
            new_win = 2

    if len(args) != 1:
        print >> sys.stderr, usage
        sys.exit(1)
    url = args[0]
    open(url, new_win)
    print b'\x07'
    return


if __name__ == b'__main__':
    main()
