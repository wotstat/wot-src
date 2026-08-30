import inspect, keyword, linecache, os, pydoc, sys, tempfile, time, tokenize, traceback, types

def reset():
    return b'<!--: spam\nContent-Type: text/html\n\n<body bgcolor="#f0f0f8"><font color="#f0f0f8" size="-5"> -->\n<body bgcolor="#f0f0f8"><font color="#f0f0f8" size="-5"> --> -->\n</font> </font> </font> </script> </object> </blockquote> </pre>\n</table> </table> </table> </table> </table> </font> </font> </font>'


__UNDEF__ = []

def small(text):
    if text:
        return b'<small>' + text + b'</small>'
    else:
        return b''

    return


def strong(text):
    if text:
        return b'<strong>' + text + b'</strong>'
    else:
        return b''

    return


def grey(text):
    if text:
        return b'<font color="#909090">' + text + b'</font>'
    else:
        return b''

    return


def lookup(name, frame, locals):
    if name in locals:
        return (b'local', locals[name])
    else:
        if name in frame.f_globals:
            return (b'global', frame.f_globals[name])
        if b'__builtins__' in frame.f_globals:
            builtins = frame.f_globals[b'__builtins__']
            if type(builtins) is type({}):
                if name in builtins:
                    return (b'builtin', builtins[name])
            elif hasattr(builtins, name):
                return (b'builtin', getattr(builtins, name))
        return (
         None, __UNDEF__)


def scanvars(reader, frame, locals):
    vars, lasttoken, parent, prefix, value = ([], None, None, b'', __UNDEF__)
    for ttype, token, start, end, line in tokenize.generate_tokens(reader):
        if ttype == tokenize.NEWLINE:
            break
        if ttype == tokenize.NAME and token not in keyword.kwlist:
            if lasttoken == b'.':
                if parent is not __UNDEF__:
                    value = getattr(parent, token, __UNDEF__)
                    vars.append((prefix + token, prefix, value))
            else:
                where, value = lookup(token, frame, locals)
                vars.append((token, where, value))
        elif token == b'.':
            prefix += lasttoken + b'.'
            parent = value
        else:
            parent, prefix = (None, b'')
        lasttoken = token

    return vars


def html(einfo, context=5):
    etype, evalue, etb = einfo
    if type(etype) is types.ClassType:
        etype = etype.__name__
    pyver = b'Python ' + sys.version.split()[0] + b': ' + sys.executable
    date = time.ctime(time.time())
    head = b'<body bgcolor="#f0f0f8">' + pydoc.html.heading(b'<big><big>%s</big></big>' % strong(pydoc.html.escape(str(etype))), b'#ffffff', b'#6622aa', pyver + b'<br>' + date) + b'\n<p>A problem occurred in a Python script.  Here is the sequence of\nfunction calls leading up to the error, in the order they occurred.</p>'
    indent = b'<tt>' + small(b'&nbsp;' * 5) + b'&nbsp;</tt>'
    frames = []
    records = inspect.getinnerframes(etb, context)
    for frame, file, lnum, func, lines, index in records:
        if file:
            file = os.path.abspath(file)
            link = b'<a href="file://%s">%s</a>' % (file, pydoc.html.escape(file))
        else:
            file = link = b'?'
        args, varargs, varkw, locals = inspect.getargvalues(frame)
        call = b''
        if func != b'?':
            call = b'in ' + strong(pydoc.html.escape(func)) + inspect.formatargvalues(args, varargs, varkw, locals, formatvalue=(lambda value: b'=' + pydoc.html.repr(value)))
        highlight = {}

        def reader(lnum=[lnum]):
            highlight[lnum[0]] = 1
            try:
                return linecache.getline(file, lnum[0])
            finally:
                lnum[0] += 1

            return

        vars = scanvars(reader, frame, locals)
        rows = [
         b'<tr><td bgcolor="#d8bbff">%s%s %s</td></tr>' % (
          b'<big>&nbsp;</big>', link, call)]
        if index is not None:
            i = lnum - index
            for line in lines:
                num = small(b'&nbsp;' * (5 - len(str(i))) + str(i)) + b'&nbsp;'
                if i in highlight:
                    line = b'<tt>=&gt;%s%s</tt>' % (num, pydoc.html.preformat(line))
                    rows.append(b'<tr><td bgcolor="#ffccee">%s</td></tr>' % line)
                else:
                    line = b'<tt>&nbsp;&nbsp;%s%s</tt>' % (num, pydoc.html.preformat(line))
                    rows.append(b'<tr><td>%s</td></tr>' % grey(line))
                i += 1

        done, dump = {}, []
        for name, where, value in vars:
            if name in done:
                continue
            done[name] = 1
            if value is not __UNDEF__:
                if where in (b'global', b'builtin'):
                    name = b'<em>%s</em> ' % where + strong(name)
                elif where == b'local':
                    name = strong(name)
                else:
                    name = where + strong(name.split(b'.')[-1])
                dump.append(b'%s&nbsp;= %s' % (name, pydoc.html.repr(value)))
            else:
                dump.append(name + b' <em>undefined</em>')

        rows.append(b'<tr><td>%s</td></tr>' % small(grey((b', ').join(dump))))
        frames.append(b'\n<table width="100%%" cellspacing=0 cellpadding=0 border=0>\n%s</table>' % (b'\n').join(rows))

    exception = [
     b'<p>%s: %s' % (strong(pydoc.html.escape(str(etype))),
      pydoc.html.escape(str(evalue)))]
    if isinstance(evalue, BaseException):
        for name in dir(evalue):
            if name[:1] == b'_':
                continue
            value = pydoc.html.repr(getattr(evalue, name))
            exception.append(b'\n<br>%s%s&nbsp;=\n%s' % (indent, name, value))

    return head + (b'').join(frames) + (b'').join(exception) + b"\n\n\n<!-- The above is a description of an error in a Python program, formatted\n     for a Web browser because the 'cgitb' module was enabled.  In case you\n     are not reading this in a Web browser, here is the original traceback:\n\n%s\n-->\n" % pydoc.html.escape((b'').join(traceback.format_exception(etype, evalue, etb)))


def text(einfo, context=5):
    etype, evalue, etb = einfo
    if type(etype) is types.ClassType:
        etype = etype.__name__
    pyver = b'Python ' + sys.version.split()[0] + b': ' + sys.executable
    date = time.ctime(time.time())
    head = b'%s\n%s\n%s\n' % (str(etype), pyver, date) + b'\nA problem occurred in a Python script.  Here is the sequence of\nfunction calls leading up to the error, in the order they occurred.\n'
    frames = []
    records = inspect.getinnerframes(etb, context)
    for frame, file, lnum, func, lines, index in records:
        file = file and os.path.abspath(file) or b'?'
        args, varargs, varkw, locals = inspect.getargvalues(frame)
        call = b''
        if func != b'?':
            call = b'in ' + func + inspect.formatargvalues(args, varargs, varkw, locals, formatvalue=(lambda value: b'=' + pydoc.text.repr(value)))
        highlight = {}

        def reader(lnum=[lnum]):
            highlight[lnum[0]] = 1
            try:
                return linecache.getline(file, lnum[0])
            finally:
                lnum[0] += 1

            return

        vars = scanvars(reader, frame, locals)
        rows = [
         b' %s %s' % (file, call)]
        if index is not None:
            i = lnum - index
            for line in lines:
                num = b'%5d ' % i
                rows.append(num + line.rstrip())
                i += 1

        done, dump = {}, []
        for name, where, value in vars:
            if name in done:
                continue
            done[name] = 1
            if value is not __UNDEF__:
                if where == b'global':
                    name = b'global ' + name
                elif where != b'local':
                    name = where + name.split(b'.')[-1]
                dump.append(b'%s = %s' % (name, pydoc.text.repr(value)))
            else:
                dump.append(name + b' undefined')

        rows.append((b'\n').join(dump))
        frames.append(b'\n%s\n' % (b'\n').join(rows))

    exception = [b'%s: %s' % (str(etype), str(evalue))]
    if isinstance(evalue, BaseException):
        for name in dir(evalue):
            value = pydoc.text.repr(getattr(evalue, name))
            exception.append(b'\n%s%s = %s' % (b'    ', name, value))

    return head + (b'').join(frames) + (b'').join(exception) + b'\n\nThe above is a description of an error in a Python program.  Here is\nthe original traceback:\n\n%s\n' % (b'').join(traceback.format_exception(etype, evalue, etb))


class Hook:

    def __init__(self, display=1, logdir=None, context=5, file=None, format=b'html'):
        self.display = display
        self.logdir = logdir
        self.context = context
        self.file = file or sys.stdout
        self.format = format
        return

    def __call__(self, etype, evalue, etb):
        self.handle((etype, evalue, etb))
        return

    def handle(self, info=None):
        info = info or sys.exc_info()
        if self.format == b'html':
            self.file.write(reset())
        formatter = self.format == b'html' and html or text
        plain = False
        try:
            doc = formatter(info, self.context)
        except:
            doc = (b'').join(traceback.format_exception(*info))
            plain = True

        if self.display:
            if plain:
                doc = pydoc.html.escape(doc)
                self.file.write(b'<pre>' + doc + b'</pre>\n')
            else:
                self.file.write(doc + b'\n')
        else:
            self.file.write(b'<p>A problem occurred in a Python script.\n')
        if self.logdir is not None:
            suffix = [
             b'.txt', b'.html'][self.format == b'html']
            fd, path = tempfile.mkstemp(suffix=suffix, dir=self.logdir)
            try:
                file = os.fdopen(fd, b'w')
                file.write(doc)
                file.close()
                msg = b'%s contains the description of this error.' % path
            except:
                msg = b'Tried to save traceback to %s, but failed.' % path

            if self.format == b'html':
                self.file.write(b'<p>%s</p>\n' % msg)
            else:
                self.file.write(msg + b'\n')
        try:
            self.file.flush()
        except:
            pass

        return


handler = Hook().handle

def enable(display=1, logdir=None, context=5, format=b'html'):
    sys.excepthook = Hook(display=display, logdir=logdir, context=context, format=format)
    return
