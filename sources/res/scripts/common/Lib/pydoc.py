__author__ = b'Ka-Ping Yee <ping@lfw.org>'
__date__ = b'26 February 2001'
__version__ = b'$Revision: 88564 $'
__credits__ = b'Guido van Rossum, for an excellent programming language.\nTommy Burnette, the original creator of manpy.\nPaul Prescod, for all his work on onlinehelp.\nRichard Chamberlain, for the first implementation of textdoc.\n'
import sys, imp, os, re, types, inspect, __builtin__, pkgutil, warnings
from repr import Repr
from string import expandtabs, find, join, lower, split, strip, rfind, rstrip
from traceback import extract_tb
try:
    from collections import deque
except ImportError:

    class deque(list):

        def popleft(self):
            return self.pop(0)


def pathdirs():
    dirs = []
    normdirs = []
    for dir in sys.path:
        dir = os.path.abspath(dir or b'.')
        normdir = os.path.normcase(dir)
        if normdir not in normdirs and os.path.isdir(dir):
            dirs.append(dir)
            normdirs.append(normdir)

    return dirs


def getdoc(object):
    result = inspect.getdoc(object) or inspect.getcomments(object)
    result = _encode(result)
    return result and re.sub(b'^ *\n', b'', rstrip(result)) or b''


def splitdoc(doc):
    lines = split(strip(doc), b'\n')
    if len(lines) == 1:
        return (lines[0], b'')
    if len(lines) >= 2 and not rstrip(lines[1]):
        return (lines[0], join(lines[2:], b'\n'))
    return (
     b'', join(lines, b'\n'))


def classname(object, modname):
    name = object.__name__
    if object.__module__ != modname:
        name = object.__module__ + b'.' + name
    return name


def isdata(object):
    return not (inspect.ismodule(object) or inspect.isclass(object) or inspect.isroutine(object) or inspect.isframe(object) or inspect.istraceback(object) or inspect.iscode(object))


def replace(text, *pairs):
    while pairs:
        text = join(split(text, pairs[0]), pairs[1])
        pairs = pairs[2:]

    return text


def cram(text, maxlen):
    if len(text) > maxlen:
        pre = max(0, (maxlen - 3) // 2)
        post = max(0, maxlen - 3 - pre)
        return text[:pre] + b'...' + text[len(text) - post:]
    return text


_re_stripid = re.compile(b' at 0x[0-9a-f]{6,16}(>+)$', re.IGNORECASE)

def stripid(text):
    return _re_stripid.sub(b'\\1', text)


def _is_some_method(obj):
    return inspect.ismethod(obj) or inspect.ismethoddescriptor(obj)


def allmethods(cl):
    methods = {}
    for key, value in inspect.getmembers(cl, _is_some_method):
        methods[key] = 1

    for base in cl.__bases__:
        methods.update(allmethods(base))

    for key in methods.keys():
        methods[key] = getattr(cl, key)

    return methods


def _split_list(s, predicate):
    yes = []
    no = []
    for x in s:
        if predicate(x):
            yes.append(x)
        else:
            no.append(x)

    return (
     yes, no)


def visiblename(name, all=None, obj=None):
    _hidden_names = (b'__builtins__', b'__doc__', b'__file__', b'__path__', b'__module__', b'__name__', b'__slots__', b'__package__')
    if name in _hidden_names:
        return 0
    else:
        if name.startswith(b'__') and name.endswith(b'__'):
            return 1
        else:
            if name.startswith(b'_') and hasattr(obj, b'_fields'):
                return 1
            if all is not None:
                return name in all
            return not name.startswith(b'_')

        return


def classify_class_attrs(object):

    def fixup(data):
        name, kind, cls, value = data
        if inspect.isdatadescriptor(value):
            kind = b'data descriptor'
        return (
         name, kind, cls, value)

    return map(fixup, inspect.classify_class_attrs(object))


try:
    _unicode = unicode
except NameError:

    class _unicode(object):
        pass


    _encoding = b'ascii'

    def _encode(text, encoding=b'ascii'):
        return text


else:
    import locale
    _encoding = locale.getpreferredencoding()

    def _encode(text, encoding=None):
        if isinstance(text, unicode):
            return text.encode(encoding or _encoding, b'xmlcharrefreplace')
        else:
            return text

        return


def _binstr(obj):
    if isinstance(obj, _unicode):
        return obj.encode(_encoding, b'xmlcharrefreplace')
    return str(obj)


def ispackage(path):
    if os.path.isdir(path):
        for ext in (b'.py', b'.pyc', b'.pyo'):
            if os.path.isfile(os.path.join(path, b'__init__' + ext)):
                return True

    return False


def source_synopsis(file):
    line = file.readline()
    while line[:1] == b'#' or not strip(line):
        line = file.readline()
        if not line:
            break

    line = strip(line)
    if line[:4] == b'r"""':
        line = line[1:]
    if line[:3] == b'"""':
        line = line[3:]
        if line[-1:] == b'\\':
            line = line[:-1]
        while not strip(line):
            line = file.readline()
            if not line:
                break

        result = strip(split(line, b'"""')[0])
    else:
        result = None
    return result


def synopsis(filename, cache={}):
    mtime = os.stat(filename).st_mtime
    lastupdate, result = cache.get(filename, (None, None))
    if lastupdate is None or lastupdate < mtime:
        info = inspect.getmoduleinfo(filename)
        try:
            file = open(filename)
        except IOError:
            return

        if info and b'b' in info[2]:
            try:
                module = imp.load_module(b'__temp__', file, filename, info[1:])
            except:
                return

            result = module.__doc__.splitlines()[0] if module.__doc__ else None
            del sys.modules[b'__temp__']
        else:
            result = source_synopsis(file)
            file.close()
        cache[filename] = (
         mtime, result)
    return result


class ErrorDuringImport(Exception):

    def __init__(self, filename, exc_info):
        exc, value, tb = exc_info
        self.filename = filename
        self.exc = exc
        self.value = value
        self.tb = tb
        return

    def __str__(self):
        exc = self.exc
        if type(exc) is types.ClassType:
            exc = exc.__name__
        return b'problem in %s - %s: %s' % (self.filename, exc, self.value)


def importfile(path):
    magic = imp.get_magic()
    file = open(path, b'r')
    if file.read(len(magic)) == magic:
        kind = imp.PY_COMPILED
    else:
        kind = imp.PY_SOURCE
    file.close()
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    file = open(path, b'r')
    try:
        module = imp.load_module(name, file, path, (ext, b'r', kind))
    except:
        raise ErrorDuringImport(path, sys.exc_info())

    file.close()
    return module


def safeimport(path, forceload=0, cache={}):
    try:
        if forceload and path in sys.modules:
            if path not in sys.builtin_module_names:
                subs = [m for m in sys.modules if m.startswith(path + b'.')]
                for key in [path] + subs:
                    cache[key] = sys.modules[key]
                    del sys.modules[key]

        module = __import__(path)
    except:
        exc, value, tb = info = sys.exc_info()
        if path in sys.modules:
            raise ErrorDuringImport(sys.modules[path].__file__, info)
        elif exc is SyntaxError:
            raise ErrorDuringImport(value.filename, info)
        elif exc is ImportError and extract_tb(tb)[-1][2] == b'safeimport':
            return
        raise ErrorDuringImport(path, sys.exc_info())

    for part in split(path, b'.')[1:]:
        try:
            module = getattr(module, part)
        except AttributeError:
            return

    return module


class Doc():

    def document(self, object, name=None, *args):
        args = (
         object, name) + args
        if inspect.isgetsetdescriptor(object):
            return self.docdata(*args)
        if inspect.ismemberdescriptor(object):
            return self.docdata(*args)
        try:
            if inspect.ismodule(object):
                return self.docmodule(*args)
            if inspect.isclass(object):
                return self.docclass(*args)
            if inspect.isroutine(object):
                return self.docroutine(*args)
        except AttributeError:
            pass

        if isinstance(object, property):
            return self.docproperty(*args)
        return self.docother(*args)

    def fail(self, object, name=None, *args):
        message = b"don't know how to document object%s of type %s" % (
         name and b' ' + repr(name), type(object).__name__)
        raise TypeError, message
        return

    docmodule = docclass = docroutine = docother = docproperty = docdata = fail

    def getdocloc(self, object, basedir=os.path.join(sys.exec_prefix, b'lib', b'python' + sys.version[0:3])):
        try:
            file = inspect.getabsfile(object)
        except TypeError:
            file = b'(built-in)'

        docloc = os.environ.get(b'PYTHONDOCS', b'https://docs.python.org/library')
        basedir = os.path.normcase(basedir)
        if isinstance(object, type(os)) and (object.__name__ in (b'errno', b'exceptions', b'gc', b'imp', b'marshal', b'posix', b'signal', b'sys', b'thread', b'zipimport') or file.startswith(basedir) and not file.startswith(os.path.join(basedir, b'site-packages'))) and object.__name__ not in (b'xml.etree', b'test.pydoc_mod'):
            if docloc.startswith((b'http://', b'https://')):
                docloc = b'%s/%s' % (docloc.rstrip(b'/'), object.__name__.lower())
            else:
                docloc = os.path.join(docloc, object.__name__.lower() + b'.html')
        else:
            docloc = None
        return docloc


class HTMLRepr(Repr):

    def __init__(self):
        Repr.__init__(self)
        self.maxlist = self.maxtuple = 20
        self.maxdict = 10
        self.maxstring = self.maxother = 100
        return

    def escape(self, text):
        return replace(text, b'&', b'&amp;', b'<', b'&lt;', b'>', b'&gt;')

    def repr(self, object):
        return Repr.repr(self, object)

    def repr1(self, x, level):
        if hasattr(type(x), b'__name__'):
            methodname = b'repr_' + join(split(type(x).__name__), b'_')
            if hasattr(self, methodname):
                return getattr(self, methodname)(x, level)
        return self.escape(cram(stripid(repr(x)), self.maxother))

    def repr_string(self, x, level):
        test = cram(x, self.maxstring)
        testrepr = repr(test)
        if b'\\' in test and b'\\' not in replace(testrepr, b'\\\\', b''):
            return b'r' + testrepr[0] + self.escape(test) + testrepr[0]
        return re.sub(b'((\\\\[\\\\abfnrtv\\\'"]|\\\\[0-9]..|\\\\x..|\\\\u....)+)', b'<font color="#c040c0">\\1</font>', self.escape(testrepr))

    repr_str = repr_string

    def repr_instance(self, x, level):
        try:
            return self.escape(cram(stripid(repr(x)), self.maxstring))
        except:
            return self.escape(b'<%s instance>' % x.__class__.__name__)

        return

    repr_unicode = repr_string


class HTMLDoc(Doc):
    _repr_instance = HTMLRepr()
    repr = _repr_instance.repr
    escape = _repr_instance.escape

    def page(self, title, contents):
        return _encode(b'\n<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n<html><head><title>Python: %s</title>\n<meta charset="utf-8">\n</head><body bgcolor="#f0f0f8">\n%s\n</body></html>' % (title, contents), b'ascii')

    def heading(self, title, fgcol, bgcol, extras=b''):
        return b'\n<table width="100%%" cellspacing=0 cellpadding=2 border=0 summary="heading">\n<tr bgcolor="%s">\n<td valign=bottom>&nbsp;<br>\n<font color="%s" face="helvetica, arial">&nbsp;<br>%s</font></td\n><td align=right valign=bottom\n><font color="%s" face="helvetica, arial">%s</font></td></tr></table>\n    ' % (bgcol, fgcol, title, fgcol, extras or b'&nbsp;')

    def section(self, title, fgcol, bgcol, contents, width=6, prelude=b'', marginalia=None, gap=b'&nbsp;'):
        if marginalia is None:
            marginalia = b'<tt>' + b'&nbsp;' * width + b'</tt>'
        result = b'<p>\n<table width="100%%" cellspacing=0 cellpadding=2 border=0 summary="section">\n<tr bgcolor="%s">\n<td colspan=3 valign=bottom>&nbsp;<br>\n<font color="%s" face="helvetica, arial">%s</font></td></tr>\n    ' % (bgcol, fgcol, title)
        if prelude:
            result = result + b'\n<tr bgcolor="%s"><td rowspan=2>%s</td>\n<td colspan=2>%s</td></tr>\n<tr><td>%s</td>' % (bgcol, marginalia, prelude, gap)
        else:
            result = result + b'\n<tr><td bgcolor="%s">%s</td><td>%s</td>' % (bgcol, marginalia, gap)
        return result + b'\n<td width="100%%">%s</td></tr></table>' % contents

    def bigsection(self, title, *args):
        title = b'<big><strong>%s</strong></big>' % title
        return self.section(title, *args)

    def preformat(self, text):
        text = self.escape(expandtabs(text))
        return replace(text, b'\n\n', b'\n \n', b'\n\n', b'\n \n', b' ', b'&nbsp;', b'\n', b'<br>\n')

    def multicolumn(self, list, format, cols=4):
        result = b''
        rows = (len(list) + cols - 1) // cols
        for col in range(cols):
            result = result + b'<td width="%d%%" valign=top>' % (100 // cols)
            for i in range(rows * col, rows * col + rows):
                if i < len(list):
                    result = result + format(list[i]) + b'<br>\n'

            result = result + b'</td>'

        return b'<table width="100%%" summary="list"><tr>%s</tr></table>' % result

    def grey(self, text):
        return b'<font color="#909090">%s</font>' % text

    def namelink(self, name, *dicts):
        for dict in dicts:
            if name in dict:
                return b'<a href="%s">%s</a>' % (dict[name], name)

        return name

    def classlink(self, object, modname):
        name, module = object.__name__, sys.modules.get(object.__module__)
        if hasattr(module, name) and getattr(module, name) is object:
            return b'<a href="%s.html#%s">%s</a>' % (
             module.__name__, name, classname(object, modname))
        return classname(object, modname)

    def modulelink(self, object):
        return b'<a href="%s.html">%s</a>' % (object.__name__, object.__name__)

    def modpkglink(self, data):
        name, path, ispackage, shadowed = data
        if shadowed:
            return self.grey(name)
        if path:
            url = b'%s.%s.html' % (path, name)
        else:
            url = b'%s.html' % name
        if ispackage:
            text = b'<strong>%s</strong>&nbsp;(package)' % name
        else:
            text = name
        return b'<a href="%s">%s</a>' % (url, text)

    def markup(self, text, escape=None, funcs={}, classes={}, methods={}):
        escape = escape or self.escape
        results = []
        here = 0
        pattern = re.compile(b'\\b((http|ftp)://\\S+[\\w/]|RFC[- ]?(\\d+)|PEP[- ]?(\\d+)|(self\\.)?(\\w+))')
        while True:
            match = pattern.search(text, here)
            if not match:
                break
            start, end = match.span()
            results.append(escape(text[here:start]))
            all, scheme, rfc, pep, selfdot, name = match.groups()
            if scheme:
                url = escape(all).replace(b'"', b'&quot;')
                results.append(b'<a href="%s">%s</a>' % (url, url))
            elif rfc:
                url = b'http://www.rfc-editor.org/rfc/rfc%d.txt' % int(rfc)
                results.append(b'<a href="%s">%s</a>' % (url, escape(all)))
            elif pep:
                url = b'http://www.python.org/dev/peps/pep-%04d/' % int(pep)
                results.append(b'<a href="%s">%s</a>' % (url, escape(all)))
            elif selfdot:
                if text[end:end + 1] == b'(':
                    results.append(b'self.' + self.namelink(name, methods))
                else:
                    results.append(b'self.<strong>%s</strong>' % name)
            elif text[end:end + 1] == b'(':
                results.append(self.namelink(name, methods, funcs, classes))
            else:
                results.append(self.namelink(name, classes))
            here = end

        results.append(escape(text[here:]))
        return join(results, b'')

    def formattree(self, tree, modname, parent=None):
        result = b''
        for entry in tree:
            if type(entry) is type(()):
                c, bases = entry
                result = result + b'<dt><font face="helvetica, arial">'
                result = result + self.classlink(c, modname)
                if bases and bases != (parent,):
                    parents = []
                    for base in bases:
                        parents.append(self.classlink(base, modname))

                    result = result + b'(' + join(parents, b', ') + b')'
                result = result + b'\n</font></dt>'
            elif type(entry) is type([]):
                result = result + b'<dd>\n%s</dd>\n' % self.formattree(entry, modname, c)

        return b'<dl>\n%s</dl>\n' % result

    def docmodule(self, object, name=None, mod=None, *ignored):
        name = object.__name__
        try:
            all = object.__all__
        except AttributeError:
            all = None

        parts = split(name, b'.')
        links = []
        for i in range(len(parts) - 1):
            links.append(b'<a href="%s.html"><font color="#ffffff">%s</font></a>' % (
             join(parts[:i + 1], b'.'), parts[i]))

        linkedname = join(links + parts[-1:], b'.')
        head = b'<big><big><strong>%s</strong></big></big>' % linkedname
        try:
            path = inspect.getabsfile(object)
            url = path
            if sys.platform == b'win32':
                import nturl2path
                url = nturl2path.pathname2url(path)
            filelink = b'<a href="file:%s">%s</a>' % (url, path)
        except TypeError:
            filelink = b'(built-in)'

        info = []
        if hasattr(object, b'__version__'):
            version = _binstr(object.__version__)
            if version[:11] == b'$Revision: ' and version[-1:] == b'$':
                version = strip(version[11:-1])
            info.append(b'version %s' % self.escape(version))
        if hasattr(object, b'__date__'):
            info.append(self.escape(_binstr(object.__date__)))
        if info:
            head = head + b' (%s)' % join(info, b', ')
        docloc = self.getdocloc(object)
        if docloc is not None:
            docloc = b'<br><a href="%(docloc)s">Module Docs</a>' % locals()
        else:
            docloc = b''
        result = self.heading(head, b'#ffffff', b'#7799ee', b'<a href=".">index</a><br>' + filelink + docloc)
        modules = inspect.getmembers(object, inspect.ismodule)
        classes, cdict = [], {}
        for key, value in inspect.getmembers(object, inspect.isclass):
            if all is not None or (inspect.getmodule(value) or object) is object:
                if visiblename(key, all, object):
                    classes.append((key, value))
                    cdict[key] = cdict[value] = b'#' + key

        for key, value in classes:
            for base in value.__bases__:
                key, modname = base.__name__, base.__module__
                module = sys.modules.get(modname)
                if modname != name and module and hasattr(module, key):
                    if getattr(module, key) is base:
                        if key not in cdict:
                            cdict[key] = cdict[base] = modname + b'.html#' + key

        funcs, fdict = [], {}
        for key, value in inspect.getmembers(object, inspect.isroutine):
            if all is not None or inspect.isbuiltin(value) or inspect.getmodule(value) is object:
                if visiblename(key, all, object):
                    funcs.append((key, value))
                    fdict[key] = b'#-' + key
                    if inspect.isfunction(value):
                        fdict[value] = fdict[key]

        data = []
        for key, value in inspect.getmembers(object, isdata):
            if visiblename(key, all, object):
                data.append((key, value))

        doc = self.markup(getdoc(object), self.preformat, fdict, cdict)
        doc = doc and b'<tt>%s</tt>' % doc
        result = result + b'<p>%s</p>\n' % doc
        if hasattr(object, b'__path__'):
            modpkgs = []
            for importer, modname, ispkg in pkgutil.iter_modules(object.__path__):
                modpkgs.append((modname, name, ispkg, 0))

            modpkgs.sort()
            contents = self.multicolumn(modpkgs, self.modpkglink)
            result = result + self.bigsection(b'Package Contents', b'#ffffff', b'#aa55cc', contents)
        elif modules:
            contents = self.multicolumn(modules, (lambda key_value, s=self: s.modulelink(key_value[1])))
            result = result + self.bigsection(b'Modules', b'#ffffff', b'#aa55cc', contents)
        if classes:
            classlist = map((lambda key_value: key_value[1]), classes)
            contents = [
             self.formattree(inspect.getclasstree(classlist, 1), name)]
            for key, value in classes:
                contents.append(self.document(value, key, name, fdict, cdict))

            result = result + self.bigsection(b'Classes', b'#ffffff', b'#ee77aa', join(contents))
        if funcs:
            contents = []
            for key, value in funcs:
                contents.append(self.document(value, key, name, fdict, cdict))

            result = result + self.bigsection(b'Functions', b'#ffffff', b'#eeaa77', join(contents))
        if data:
            contents = []
            for key, value in data:
                contents.append(self.document(value, key))

            result = result + self.bigsection(b'Data', b'#ffffff', b'#55aa55', join(contents, b'<br>\n'))
        if hasattr(object, b'__author__'):
            contents = self.markup(_binstr(object.__author__), self.preformat)
            result = result + self.bigsection(b'Author', b'#ffffff', b'#7799ee', contents)
        if hasattr(object, b'__credits__'):
            contents = self.markup(_binstr(object.__credits__), self.preformat)
            result = result + self.bigsection(b'Credits', b'#ffffff', b'#7799ee', contents)
        return result

    def docclass(self, object, name=None, mod=None, funcs={}, classes={}, *ignored):
        realname = object.__name__
        name = name or realname
        bases = object.__bases__
        contents = []
        push = contents.append

        class HorizontalRule:

            def __init__(self):
                self.needone = 0
                return

            def maybe(self):
                if self.needone:
                    push(b'<hr>\n')
                self.needone = 1
                return

        hr = HorizontalRule()
        mro = deque(inspect.getmro(object))
        if len(mro) > 2:
            hr.maybe()
            push(b'<dl><dt>Method resolution order:</dt>\n')
            for base in mro:
                push(b'<dd>%s</dd>\n' % self.classlink(base, object.__module__))

            push(b'</dl>\n')

        def spill(msg, attrs, predicate):
            ok, attrs = _split_list(attrs, predicate)
            if ok:
                hr.maybe()
                push(msg)
                for name, kind, homecls, value in ok:
                    try:
                        value = getattr(object, name)
                    except Exception:
                        push(self._docdescriptor(name, value, mod))
                    else:
                        push(self.document(value, name, mod, funcs, classes, mdict, object))

                    push(b'\n')

            return attrs

        def spilldescriptors(msg, attrs, predicate):
            ok, attrs = _split_list(attrs, predicate)
            if ok:
                hr.maybe()
                push(msg)
                for name, kind, homecls, value in ok:
                    push(self._docdescriptor(name, value, mod))

            return attrs

        def spilldata(msg, attrs, predicate):
            ok, attrs = _split_list(attrs, predicate)
            if ok:
                hr.maybe()
                push(msg)
                for name, kind, homecls, value in ok:
                    base = self.docother(getattr(object, name), name, mod)
                    if hasattr(value, b'__call__') or inspect.isdatadescriptor(value):
                        doc = getattr(value, b'__doc__', None)
                    else:
                        doc = None
                    if doc is None:
                        push(b'<dl><dt>%s</dl>\n' % base)
                    else:
                        doc = self.markup(getdoc(value), self.preformat, funcs, classes, mdict)
                        doc = b'<dd><tt>%s</tt>' % doc
                        push(b'<dl><dt>%s%s</dl>\n' % (base, doc))
                    push(b'\n')

            return attrs

        attrs = filter((lambda data: visiblename(data[0], obj=object)), classify_class_attrs(object))
        mdict = {}
        for key, kind, homecls, value in attrs:
            mdict[key] = anchor = b'#' + name + b'-' + key
            try:
                value = getattr(object, name)
            except Exception:
                pass

            try:
                mdict[value] = anchor
            except TypeError:
                pass

        while attrs:
            if mro:
                thisclass = mro.popleft()
            else:
                thisclass = attrs[0][2]
            attrs, inherited = _split_list(attrs, (lambda t: t[2] is thisclass))
            if thisclass is __builtin__.object:
                attrs = inherited
                continue
            elif thisclass is object:
                tag = b'defined here'
            else:
                tag = b'inherited from %s' % self.classlink(thisclass, object.__module__)
            tag += b':<br>\n'
            try:
                attrs.sort(key=(lambda t: t[0]))
            except TypeError:
                attrs.sort((lambda t1, t2: cmp(t1[0], t2[0])))

            attrs = spill(b'Methods %s' % tag, attrs, (lambda t: t[1] == b'method'))
            attrs = spill(b'Class methods %s' % tag, attrs, (lambda t: t[1] == b'class method'))
            attrs = spill(b'Static methods %s' % tag, attrs, (lambda t: t[1] == b'static method'))
            attrs = spilldescriptors(b'Data descriptors %s' % tag, attrs, (lambda t: t[1] == b'data descriptor'))
            attrs = spilldata(b'Data and other attributes %s' % tag, attrs, (lambda t: t[1] == b'data'))
            attrs = inherited

        contents = (b'').join(contents)
        if name == realname:
            title = b'<a name="%s">class <strong>%s</strong></a>' % (
             name, realname)
        else:
            title = b'<strong>%s</strong> = <a name="%s">class %s</a>' % (
             name, name, realname)
        if bases:
            parents = []
            for base in bases:
                parents.append(self.classlink(base, object.__module__))

            title = title + b'(%s)' % join(parents, b', ')
        doc = self.markup(getdoc(object), self.preformat, funcs, classes, mdict)
        doc = doc and b'<tt>%s<br>&nbsp;</tt>' % doc
        return self.section(title, b'#000000', b'#ffc8d8', contents, 3, doc)

    def formatvalue(self, object):
        return self.grey(b'=' + self.repr(object))

    def docroutine(self, object, name=None, mod=None, funcs={}, classes={}, methods={}, cl=None):
        realname = object.__name__
        name = name or realname
        anchor = (cl and cl.__name__ or b'') + b'-' + name
        note = b''
        skipdocs = 0
        if inspect.ismethod(object):
            imclass = object.im_class
            if cl:
                if imclass is not cl:
                    note = b' from ' + self.classlink(imclass, mod)
            elif object.im_self is not None:
                note = b' method of %s instance' % self.classlink(object.im_self.__class__, mod)
            else:
                note = b' unbound %s method' % self.classlink(imclass, mod)
            object = object.im_func
        if name == realname:
            title = b'<a name="%s"><strong>%s</strong></a>' % (anchor, realname)
        else:
            if cl and realname in cl.__dict__ and cl.__dict__[realname] is object:
                reallink = b'<a href="#%s">%s</a>' % (
                 cl.__name__ + b'-' + realname, realname)
                skipdocs = 1
            else:
                reallink = realname
            title = b'<a name="%s"><strong>%s</strong></a> = %s' % (
             anchor, name, reallink)
        if inspect.isfunction(object):
            args, varargs, varkw, defaults = inspect.getargspec(object)
            argspec = inspect.formatargspec(args, varargs, varkw, defaults, formatvalue=self.formatvalue)
            if realname == b'<lambda>':
                title = b'<strong>%s</strong> <em>lambda</em> ' % name
                argspec = argspec[1:-1]
        else:
            argspec = b'(...)'
        decl = title + argspec + (note and self.grey(b'<font face="helvetica, arial">%s</font>' % note))
        if skipdocs:
            return b'<dl><dt>%s</dt></dl>\n' % decl
        else:
            doc = self.markup(getdoc(object), self.preformat, funcs, classes, methods)
            doc = doc and b'<dd><tt>%s</tt></dd>' % doc
            return b'<dl><dt>%s</dt>%s</dl>\n' % (decl, doc)
            return

    def _docdescriptor(self, name, value, mod):
        results = []
        push = results.append
        if name:
            push(b'<dl><dt><strong>%s</strong></dt>\n' % name)
        if value.__doc__ is not None:
            doc = self.markup(getdoc(value), self.preformat)
            push(b'<dd><tt>%s</tt></dd>\n' % doc)
        push(b'</dl>\n')
        return (b'').join(results)

    def docproperty(self, object, name=None, mod=None, cl=None):
        return self._docdescriptor(name, object, mod)

    def docother(self, object, name=None, mod=None, *ignored):
        lhs = name and b'<strong>%s</strong> = ' % name or b''
        return lhs + self.repr(object)

    def docdata(self, object, name=None, mod=None, cl=None):
        return self._docdescriptor(name, object, mod)

    def index(self, dir, shadowed=None):
        modpkgs = []
        if shadowed is None:
            shadowed = {}
        for importer, name, ispkg in pkgutil.iter_modules([dir]):
            modpkgs.append((name, b'', ispkg, name in shadowed))
            shadowed[name] = 1

        modpkgs.sort()
        contents = self.multicolumn(modpkgs, self.modpkglink)
        return self.bigsection(dir, b'#ffffff', b'#ee77aa', contents)


class TextRepr(Repr):

    def __init__(self):
        Repr.__init__(self)
        self.maxlist = self.maxtuple = 20
        self.maxdict = 10
        self.maxstring = self.maxother = 100
        return

    def repr1(self, x, level):
        if hasattr(type(x), b'__name__'):
            methodname = b'repr_' + join(split(type(x).__name__), b'_')
            if hasattr(self, methodname):
                return getattr(self, methodname)(x, level)
        return cram(stripid(repr(x)), self.maxother)

    def repr_string(self, x, level):
        test = cram(x, self.maxstring)
        testrepr = repr(test)
        if b'\\' in test and b'\\' not in replace(testrepr, b'\\\\', b''):
            return b'r' + testrepr[0] + test + testrepr[0]
        return testrepr

    repr_str = repr_string

    def repr_instance(self, x, level):
        try:
            return cram(stripid(repr(x)), self.maxstring)
        except:
            return b'<%s instance>' % x.__class__.__name__

        return


class TextDoc(Doc):
    _repr_instance = TextRepr()
    repr = _repr_instance.repr

    def bold(self, text):
        return join(map((lambda ch: ch + b'\x08' + ch), text), b'')

    def indent(self, text, prefix=b'    '):
        if not text:
            return b''
        lines = split(text, b'\n')
        lines = map((lambda line, prefix=prefix: prefix + line), lines)
        if lines:
            lines[-1] = rstrip(lines[-1])
        return join(lines, b'\n')

    def section(self, title, contents):
        return self.bold(title) + b'\n' + rstrip(self.indent(contents)) + b'\n\n'

    def formattree(self, tree, modname, parent=None, prefix=b''):
        result = b''
        for entry in tree:
            if type(entry) is type(()):
                c, bases = entry
                result = result + prefix + classname(c, modname)
                if bases and bases != (parent,):
                    parents = map((lambda c, m=modname: classname(c, m)), bases)
                    result = result + b'(%s)' % join(parents, b', ')
                result = result + b'\n'
            elif type(entry) is type([]):
                result = result + self.formattree(entry, modname, c, prefix + b'    ')

        return result

    def docmodule(self, object, name=None, mod=None):
        name = object.__name__
        synop, desc = splitdoc(getdoc(object))
        result = self.section(b'NAME', name + (synop and b' - ' + synop))
        try:
            all = object.__all__
        except AttributeError:
            all = None

        try:
            file = inspect.getabsfile(object)
        except TypeError:
            file = b'(built-in)'

        result = result + self.section(b'FILE', file)
        docloc = self.getdocloc(object)
        if docloc is not None:
            result = result + self.section(b'MODULE DOCS', docloc)
        if desc:
            result = result + self.section(b'DESCRIPTION', desc)
        classes = []
        for key, value in inspect.getmembers(object, inspect.isclass):
            if all is not None or (inspect.getmodule(value) or object) is object:
                if visiblename(key, all, object):
                    classes.append((key, value))

        funcs = []
        for key, value in inspect.getmembers(object, inspect.isroutine):
            if all is not None or inspect.isbuiltin(value) or inspect.getmodule(value) is object:
                if visiblename(key, all, object):
                    funcs.append((key, value))

        data = []
        for key, value in inspect.getmembers(object, isdata):
            if visiblename(key, all, object):
                data.append((key, value))

        modpkgs = []
        modpkgs_names = set()
        if hasattr(object, b'__path__'):
            for importer, modname, ispkg in pkgutil.iter_modules(object.__path__):
                modpkgs_names.add(modname)
                if ispkg:
                    modpkgs.append(modname + b' (package)')
                else:
                    modpkgs.append(modname)

            modpkgs.sort()
            result = result + self.section(b'PACKAGE CONTENTS', join(modpkgs, b'\n'))
        submodules = []
        for key, value in inspect.getmembers(object, inspect.ismodule):
            if value.__name__.startswith(name + b'.') and key not in modpkgs_names:
                submodules.append(key)

        if submodules:
            submodules.sort()
            result = result + self.section(b'SUBMODULES', join(submodules, b'\n'))
        if classes:
            classlist = map((lambda key_value: key_value[1]), classes)
            contents = [
             self.formattree(inspect.getclasstree(classlist, 1), name)]
            for key, value in classes:
                contents.append(self.document(value, key, name))

            result = result + self.section(b'CLASSES', join(contents, b'\n'))
        if funcs:
            contents = []
            for key, value in funcs:
                contents.append(self.document(value, key, name))

            result = result + self.section(b'FUNCTIONS', join(contents, b'\n'))
        if data:
            contents = []
            for key, value in data:
                contents.append(self.docother(value, key, name, maxlen=70))

            result = result + self.section(b'DATA', join(contents, b'\n'))
        if hasattr(object, b'__version__'):
            version = _binstr(object.__version__)
            if version[:11] == b'$Revision: ' and version[-1:] == b'$':
                version = strip(version[11:-1])
            result = result + self.section(b'VERSION', version)
        if hasattr(object, b'__date__'):
            result = result + self.section(b'DATE', _binstr(object.__date__))
        if hasattr(object, b'__author__'):
            result = result + self.section(b'AUTHOR', _binstr(object.__author__))
        if hasattr(object, b'__credits__'):
            result = result + self.section(b'CREDITS', _binstr(object.__credits__))
        return result

    def docclass(self, object, name=None, mod=None, *ignored):
        realname = object.__name__
        name = name or realname
        bases = object.__bases__

        def makename(c, m=object.__module__):
            return classname(c, m)

        if name == realname:
            title = b'class ' + self.bold(realname)
        else:
            title = self.bold(name) + b' = class ' + realname
        if bases:
            parents = map(makename, bases)
            title = title + b'(%s)' % join(parents, b', ')
        doc = getdoc(object)
        contents = doc and [doc + b'\n'] or []
        push = contents.append
        mro = deque(inspect.getmro(object))
        if len(mro) > 2:
            push(b'Method resolution order:')
            for base in mro:
                push(b'    ' + makename(base))

            push(b'')

        class HorizontalRule:

            def __init__(self):
                self.needone = 0
                return

            def maybe(self):
                if self.needone:
                    push(b'-' * 70)
                self.needone = 1
                return

        hr = HorizontalRule()

        def spill(msg, attrs, predicate):
            ok, attrs = _split_list(attrs, predicate)
            if ok:
                hr.maybe()
                push(msg)
                for name, kind, homecls, value in ok:
                    try:
                        value = getattr(object, name)
                    except Exception:
                        push(self._docdescriptor(name, value, mod))
                    else:
                        push(self.document(value, name, mod, object))

            return attrs

        def spilldescriptors(msg, attrs, predicate):
            ok, attrs = _split_list(attrs, predicate)
            if ok:
                hr.maybe()
                push(msg)
                for name, kind, homecls, value in ok:
                    push(self._docdescriptor(name, value, mod))

            return attrs

        def spilldata(msg, attrs, predicate):
            ok, attrs = _split_list(attrs, predicate)
            if ok:
                hr.maybe()
                push(msg)
                for name, kind, homecls, value in ok:
                    if hasattr(value, b'__call__') or inspect.isdatadescriptor(value):
                        doc = getdoc(value)
                    else:
                        doc = None
                    push(self.docother(getattr(object, name), name, mod, maxlen=70, doc=doc) + b'\n')

            return attrs

        attrs = filter((lambda data: visiblename(data[0], obj=object)), classify_class_attrs(object))
        while attrs:
            if mro:
                thisclass = mro.popleft()
            else:
                thisclass = attrs[0][2]
            attrs, inherited = _split_list(attrs, (lambda t: t[2] is thisclass))
            if thisclass is __builtin__.object:
                attrs = inherited
                continue
            elif thisclass is object:
                tag = b'defined here'
            else:
                tag = b'inherited from %s' % classname(thisclass, object.__module__)
            attrs.sort()
            attrs = spill(b'Methods %s:\n' % tag, attrs, (lambda t: t[1] == b'method'))
            attrs = spill(b'Class methods %s:\n' % tag, attrs, (lambda t: t[1] == b'class method'))
            attrs = spill(b'Static methods %s:\n' % tag, attrs, (lambda t: t[1] == b'static method'))
            attrs = spilldescriptors(b'Data descriptors %s:\n' % tag, attrs, (lambda t: t[1] == b'data descriptor'))
            attrs = spilldata(b'Data and other attributes %s:\n' % tag, attrs, (lambda t: t[1] == b'data'))
            attrs = inherited

        contents = (b'\n').join(contents)
        if not contents:
            return title + b'\n'
        return title + b'\n' + self.indent(rstrip(contents), b' |  ') + b'\n'

    def formatvalue(self, object):
        return b'=' + self.repr(object)

    def docroutine(self, object, name=None, mod=None, cl=None):
        realname = object.__name__
        name = name or realname
        note = b''
        skipdocs = 0
        if inspect.ismethod(object):
            imclass = object.im_class
            if cl:
                if imclass is not cl:
                    note = b' from ' + classname(imclass, mod)
            elif object.im_self is not None:
                note = b' method of %s instance' % classname(object.im_self.__class__, mod)
            else:
                note = b' unbound %s method' % classname(imclass, mod)
            object = object.im_func
        if name == realname:
            title = self.bold(realname)
        elif cl and realname in cl.__dict__ and cl.__dict__[realname] is object:
            skipdocs = 1
        title = self.bold(name) + b' = ' + realname
        if inspect.isfunction(object):
            args, varargs, varkw, defaults = inspect.getargspec(object)
            argspec = inspect.formatargspec(args, varargs, varkw, defaults, formatvalue=self.formatvalue)
            if realname == b'<lambda>':
                title = self.bold(name) + b' lambda '
                argspec = argspec[1:-1]
        else:
            argspec = b'(...)'
        decl = title + argspec + note
        if skipdocs:
            return decl + b'\n'
        else:
            doc = getdoc(object) or b''
            return decl + b'\n' + (doc and rstrip(self.indent(doc)) + b'\n')
            return

    def _docdescriptor(self, name, value, mod):
        results = []
        push = results.append
        if name:
            push(self.bold(name))
            push(b'\n')
        doc = getdoc(value) or b''
        if doc:
            push(self.indent(doc))
            push(b'\n')
        return (b'').join(results)

    def docproperty(self, object, name=None, mod=None, cl=None):
        return self._docdescriptor(name, object, mod)

    def docdata(self, object, name=None, mod=None, cl=None):
        return self._docdescriptor(name, object, mod)

    def docother(self, object, name=None, mod=None, parent=None, maxlen=None, doc=None):
        repr = self.repr(object)
        if maxlen:
            line = (name and name + b' = ' or b'') + repr
            chop = maxlen - len(line)
            if chop < 0:
                repr = repr[:chop] + b'...'
        line = (name and self.bold(name) + b' = ' or b'') + repr
        if doc is not None:
            line += b'\n' + self.indent(str(doc))
        return line


def pager(text):
    global pager
    pager = getpager()
    pager(text)
    return


def getpager():
    if type(sys.stdout) is not types.FileType:
        return plainpager
    if not hasattr(sys.stdin, b'isatty'):
        return plainpager
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        return plainpager
    if b'PAGER' in os.environ:
        if sys.platform == b'win32':
            return (lambda text: tempfilepager(plain(text), os.environ[b'PAGER']))
        else:
            if os.environ.get(b'TERM') in (b'dumb', b'emacs'):
                return (lambda text: pipepager(plain(text), os.environ[b'PAGER']))
            return (lambda text: pipepager(text, os.environ[b'PAGER']))

    if os.environ.get(b'TERM') in (b'dumb', b'emacs'):
        return plainpager
    if sys.platform == b'win32' or sys.platform.startswith(b'os2'):
        return (lambda text: tempfilepager(plain(text), b'more <'))
    if hasattr(os, b'system') and os.system(b'(less) 2>/dev/null') == 0:
        return (lambda text: pipepager(text, b'less'))
    import tempfile
    fd, filename = tempfile.mkstemp()
    os.close(fd)
    try:
        if hasattr(os, b'system') and os.system(b'more "%s"' % filename) == 0:
            return (lambda text: pipepager(text, b'more'))
        else:
            return ttypager

    finally:
        os.unlink(filename)

    return


def plain(text):
    return re.sub(b'.\x08', b'', text)


def pipepager(text, cmd):
    pipe = os.popen(cmd, b'w')
    try:
        pipe.write(_encode(text))
        pipe.close()
    except IOError:
        pass

    return


def tempfilepager(text, cmd):
    import tempfile
    filename = tempfile.mktemp()
    file = open(filename, b'w')
    file.write(_encode(text))
    file.close()
    try:
        os.system(cmd + b' "' + filename + b'"')
    finally:
        os.unlink(filename)

    return


def ttypager(text):
    lines = plain(_encode(plain(text), getattr(sys.stdout, b'encoding', _encoding))).split(b'\n')
    try:
        import tty
        fd = sys.stdin.fileno()
        old = tty.tcgetattr(fd)
        tty.setcbreak(fd)
        getchar = lambda : sys.stdin.read(1)
    except (ImportError, AttributeError):
        tty = None
        getchar = lambda : sys.stdin.readline()[:-1][:1]

    try:
        try:
            h = int(os.environ.get(b'LINES', 0))
        except ValueError:
            h = 0

        if h <= 1:
            h = 25
        r = inc = h - 1
        sys.stdout.write(join(lines[:inc], b'\n') + b'\n')
        while lines[r:]:
            sys.stdout.write(b'-- more --')
            sys.stdout.flush()
            c = getchar()
            if c in (b'q', b'Q'):
                sys.stdout.write(b'\r          \r')
                break
            elif c in (b'\r', b'\n'):
                sys.stdout.write(b'\r          \r' + lines[r] + b'\n')
                r = r + 1
                continue
            if c in (b'b', b'B', b'\x1b'):
                r = r - inc - inc
                if r < 0:
                    r = 0
            sys.stdout.write(b'\n' + join(lines[r:r + inc], b'\n') + b'\n')
            r = r + inc

    finally:
        if tty:
            tty.tcsetattr(fd, tty.TCSAFLUSH, old)

    return


def plainpager(text):
    sys.stdout.write(_encode(plain(text), getattr(sys.stdout, b'encoding', _encoding)))
    return


def describe(thing):
    if inspect.ismodule(thing):
        if thing.__name__ in sys.builtin_module_names:
            return b'built-in module ' + thing.__name__
        else:
            if hasattr(thing, b'__path__'):
                return b'package ' + thing.__name__
            return b'module ' + thing.__name__

    if inspect.isbuiltin(thing):
        return b'built-in function ' + thing.__name__
    if inspect.isgetsetdescriptor(thing):
        return b'getset descriptor %s.%s.%s' % (
         thing.__objclass__.__module__, thing.__objclass__.__name__,
         thing.__name__)
    if inspect.ismemberdescriptor(thing):
        return b'member descriptor %s.%s.%s' % (
         thing.__objclass__.__module__, thing.__objclass__.__name__,
         thing.__name__)
    if inspect.isclass(thing):
        return b'class ' + thing.__name__
    if inspect.isfunction(thing):
        return b'function ' + thing.__name__
    if inspect.ismethod(thing):
        return b'method ' + thing.__name__
    if type(thing) is types.InstanceType:
        return b'instance of ' + thing.__class__.__name__
    return type(thing).__name__


def locate(path, forceload=0):
    parts = [part for part in split(path, b'.') if part]
    module, n = (None, 0)
    while n < len(parts):
        nextmodule = safeimport(join(parts[:n + 1], b'.'), forceload)
        if nextmodule:
            module, n = nextmodule, n + 1
        else:
            break

    if module:
        object = module
    else:
        object = __builtin__
    for part in parts[n:]:
        try:
            object = getattr(object, part)
        except AttributeError:
            return

    return object


text = TextDoc()
html = HTMLDoc()

class _OldStyleClass():
    pass


_OLD_INSTANCE_TYPE = type(_OldStyleClass())

def resolve(thing, forceload=0):
    if isinstance(thing, str):
        object = locate(thing, forceload)
        if object is None:
            raise ImportError, b'no Python documentation found for %r' % thing
        return (object, thing)
    else:
        name = getattr(thing, b'__name__', None)
        return (thing, name if isinstance(name, str) else None)
        return


def render_doc(thing, title=b'Python Library Documentation: %s', forceload=0):
    object, name = resolve(thing, forceload)
    desc = describe(object)
    module = inspect.getmodule(object)
    if name and b'.' in name:
        desc += b' in ' + name[:name.rfind(b'.')]
    elif module and module is not object:
        desc += b' in module ' + module.__name__
    if type(object) is _OLD_INSTANCE_TYPE:
        object = object.__class__
    elif not (inspect.ismodule(object) or inspect.isclass(object) or inspect.isroutine(object) or inspect.isgetsetdescriptor(object) or inspect.ismemberdescriptor(object) or isinstance(object, property)):
        object = type(object)
        desc += b' object'
    return title % desc + b'\n\n' + text.document(object, name)


def doc(thing, title=b'Python Library Documentation: %s', forceload=0):
    try:
        pager(render_doc(thing, title, forceload))
    except (ImportError, ErrorDuringImport) as value:
        print value

    return


def writedoc(thing, forceload=0):
    try:
        object, name = resolve(thing, forceload)
        page = html.page(describe(object), html.document(object, name))
        file = open(name + b'.html', b'w')
        file.write(page)
        file.close()
        print b'wrote', name + b'.html'
    except (ImportError, ErrorDuringImport) as value:
        print value

    return


def writedocs(dir, pkgpath=b'', done=None):
    if done is None:
        done = {}
    for importer, modname, ispkg in pkgutil.walk_packages([dir], pkgpath):
        writedoc(modname)

    return


class Helper():
    keywords = {b'and': b'BOOLEAN', 
       b'as': b'with', 
       b'assert': (b'assert', b''), 
       b'break': (b'break', b'while for'), 
       b'class': (b'class', b'CLASSES SPECIALMETHODS'), 
       b'continue': (b'continue', b'while for'), 
       b'def': (b'function', b''), 
       b'del': (b'del', b'BASICMETHODS'), 
       b'elif': b'if', 
       b'else': (b'else', b'while for'), 
       b'except': b'try', 
       b'exec': (b'exec', b''), 
       b'finally': b'try', 
       b'for': (b'for', b'break continue while'), 
       b'from': b'import', 
       b'global': (b'global', b'NAMESPACES'), 
       b'if': (b'if', b'TRUTHVALUE'), 
       b'import': (b'import', b'MODULES'), 
       b'in': (b'in', b'SEQUENCEMETHODS2'), 
       b'is': b'COMPARISON', 
       b'lambda': (b'lambda', b'FUNCTIONS'), 
       b'not': b'BOOLEAN', 
       b'or': b'BOOLEAN', 
       b'pass': (b'pass', b''), 
       b'print': (b'print', b''), 
       b'raise': (b'raise', b'EXCEPTIONS'), 
       b'return': (b'return', b'FUNCTIONS'), 
       b'try': (b'try', b'EXCEPTIONS'), 
       b'while': (b'while', b'break continue if TRUTHVALUE'), 
       b'with': (b'with', b'CONTEXTMANAGERS EXCEPTIONS yield'), 
       b'yield': (b'yield', b'')}
    _strprefixes = tuple(p + q for p in (b'b', b'r', b'u') for q in (b"'", b'"'))
    _symbols_inverse = {b'STRINGS': ((b"'", b"'''", b'"""', b'"') + _strprefixes), 
       b'OPERATORS': (b'+', b'-', b'*', b'**', b'/', b'//', b'%', b'<<', b'>>', b'&', b'|', b'^', b'~', b'<', b'>', b'<=', b'>=', b'==', b'!=', b'<>'), 
       b'COMPARISON': (b'<', b'>', b'<=', b'>=', b'==', b'!=', b'<>'), 
       b'UNARY': (b'-', b'~'), 
       b'AUGMENTEDASSIGNMENT': (b'+=', b'-=', b'*=', b'/=', b'%=', b'&=', b'|=', b'^=', b'<<=', b'>>=', b'**=', b'//='), 
       b'BITWISE': (b'<<', b'>>', b'&', b'|', b'^', b'~'), 
       b'COMPLEX': (b'j', b'J')}
    symbols = {b'%': b'OPERATORS FORMATTING', 
       b'**': b'POWER', 
       b',': b'TUPLES LISTS FUNCTIONS', 
       b'.': b'ATTRIBUTES FLOAT MODULES OBJECTS', 
       b'...': b'ELLIPSIS', 
       b':': b'SLICINGS DICTIONARYLITERALS', 
       b'@': b'def class', 
       b'\\': b'STRINGS', 
       b'_': b'PRIVATENAMES', 
       b'__': b'PRIVATENAMES SPECIALMETHODS', 
       b'`': b'BACKQUOTES', 
       b'(': b'TUPLES FUNCTIONS CALLS', 
       b')': b'TUPLES FUNCTIONS CALLS', 
       b'[': b'LISTS SUBSCRIPTS SLICINGS', 
       b']': b'LISTS SUBSCRIPTS SLICINGS'}
    for topic, symbols_ in _symbols_inverse.iteritems():
        for symbol in symbols_:
            topics = symbols.get(symbol, topic)
            if topic not in topics:
                topics = topics + b' ' + topic
            symbols[symbol] = topics

    topics = {b'TYPES': (b'types', b'STRINGS UNICODE NUMBERS SEQUENCES MAPPINGS FUNCTIONS CLASSES MODULES FILES inspect'), b'STRINGS': (b'strings', b'str UNICODE SEQUENCES STRINGMETHODS FORMATTING TYPES'), 
       b'STRINGMETHODS': (b'string-methods', b'STRINGS FORMATTING'), 
       b'FORMATTING': (b'formatstrings', b'OPERATORS'), 
       b'UNICODE': (b'strings', b'encodings unicode SEQUENCES STRINGMETHODS FORMATTING TYPES'), 
       b'NUMBERS': (b'numbers', b'INTEGER FLOAT COMPLEX TYPES'), 
       b'INTEGER': (b'integers', b'int range'), 
       b'FLOAT': (b'floating', b'float math'), 
       b'COMPLEX': (b'imaginary', b'complex cmath'), 
       b'SEQUENCES': (b'typesseq', b'STRINGMETHODS FORMATTING xrange LISTS'), 
       b'MAPPINGS': b'DICTIONARIES', 
       b'FUNCTIONS': (b'typesfunctions', b'def TYPES'), 
       b'METHODS': (b'typesmethods', b'class def CLASSES TYPES'), 
       b'CODEOBJECTS': (b'bltin-code-objects', b'compile FUNCTIONS TYPES'), 
       b'TYPEOBJECTS': (b'bltin-type-objects', b'types TYPES'), 
       b'FRAMEOBJECTS': b'TYPES', 
       b'TRACEBACKS': b'TYPES', 
       b'NONE': (b'bltin-null-object', b''), 
       b'ELLIPSIS': (b'bltin-ellipsis-object', b'SLICINGS'), 
       b'FILES': (b'bltin-file-objects', b''), 
       b'SPECIALATTRIBUTES': (b'specialattrs', b''), 
       b'CLASSES': (b'types', b'class SPECIALMETHODS PRIVATENAMES'), 
       b'MODULES': (b'typesmodules', b'import'), 
       b'PACKAGES': b'import', 
       b'EXPRESSIONS': (b'operator-summary', b'lambda or and not in is BOOLEAN COMPARISON BITWISE SHIFTING BINARY FORMATTING POWER UNARY ATTRIBUTES SUBSCRIPTS SLICINGS CALLS TUPLES LISTS DICTIONARIES BACKQUOTES'), 
       b'OPERATORS': b'EXPRESSIONS', 
       b'PRECEDENCE': b'EXPRESSIONS', 
       b'OBJECTS': (b'objects', b'TYPES'), 
       b'SPECIALMETHODS': (b'specialnames', b'BASICMETHODS ATTRIBUTEMETHODS CALLABLEMETHODS SEQUENCEMETHODS1 MAPPINGMETHODS SEQUENCEMETHODS2 NUMBERMETHODS CLASSES'), 
       b'BASICMETHODS': (b'customization', b'cmp hash repr str SPECIALMETHODS'), 
       b'ATTRIBUTEMETHODS': (b'attribute-access', b'ATTRIBUTES SPECIALMETHODS'), 
       b'CALLABLEMETHODS': (b'callable-types', b'CALLS SPECIALMETHODS'), 
       b'SEQUENCEMETHODS1': (b'sequence-types', b'SEQUENCES SEQUENCEMETHODS2 SPECIALMETHODS'), 
       b'SEQUENCEMETHODS2': (b'sequence-methods', b'SEQUENCES SEQUENCEMETHODS1 SPECIALMETHODS'), 
       b'MAPPINGMETHODS': (b'sequence-types', b'MAPPINGS SPECIALMETHODS'), 
       b'NUMBERMETHODS': (b'numeric-types', b'NUMBERS AUGMENTEDASSIGNMENT SPECIALMETHODS'), 
       b'EXECUTION': (b'execmodel', b'NAMESPACES DYNAMICFEATURES EXCEPTIONS'), 
       b'NAMESPACES': (b'naming', b'global ASSIGNMENT DELETION DYNAMICFEATURES'), 
       b'DYNAMICFEATURES': (b'dynamic-features', b''), 
       b'SCOPING': b'NAMESPACES', 
       b'FRAMES': b'NAMESPACES', 
       b'EXCEPTIONS': (b'exceptions', b'try except finally raise'), 
       b'COERCIONS': (b'coercion-rules', b'CONVERSIONS'), 
       b'CONVERSIONS': (b'conversions', b'COERCIONS'), 
       b'IDENTIFIERS': (b'identifiers', b'keywords SPECIALIDENTIFIERS'), 
       b'SPECIALIDENTIFIERS': (b'id-classes', b''), 
       b'PRIVATENAMES': (b'atom-identifiers', b''), 
       b'LITERALS': (b'atom-literals', b'STRINGS BACKQUOTES NUMBERS TUPLELITERALS LISTLITERALS DICTIONARYLITERALS'), 
       b'TUPLES': b'SEQUENCES', 
       b'TUPLELITERALS': (b'exprlists', b'TUPLES LITERALS'), 
       b'LISTS': (b'typesseq-mutable', b'LISTLITERALS'), 
       b'LISTLITERALS': (b'lists', b'LISTS LITERALS'), 
       b'DICTIONARIES': (b'typesmapping', b'DICTIONARYLITERALS'), 
       b'DICTIONARYLITERALS': (b'dict', b'DICTIONARIES LITERALS'), 
       b'BACKQUOTES': (b'string-conversions', b'repr str STRINGS LITERALS'), 
       b'ATTRIBUTES': (b'attribute-references', b'getattr hasattr setattr ATTRIBUTEMETHODS'), 
       b'SUBSCRIPTS': (b'subscriptions', b'SEQUENCEMETHODS1'), 
       b'SLICINGS': (b'slicings', b'SEQUENCEMETHODS2'), 
       b'CALLS': (b'calls', b'EXPRESSIONS'), 
       b'POWER': (b'power', b'EXPRESSIONS'), 
       b'UNARY': (b'unary', b'EXPRESSIONS'), 
       b'BINARY': (b'binary', b'EXPRESSIONS'), 
       b'SHIFTING': (b'shifting', b'EXPRESSIONS'), 
       b'BITWISE': (b'bitwise', b'EXPRESSIONS'), 
       b'COMPARISON': (b'comparisons', b'EXPRESSIONS BASICMETHODS'), 
       b'BOOLEAN': (b'booleans', b'EXPRESSIONS TRUTHVALUE'), 
       b'ASSERTION': b'assert', 
       b'ASSIGNMENT': (b'assignment', b'AUGMENTEDASSIGNMENT'), 
       b'AUGMENTEDASSIGNMENT': (b'augassign', b'NUMBERMETHODS'), 
       b'DELETION': b'del', 
       b'PRINTING': b'print', 
       b'RETURNING': b'return', 
       b'IMPORTING': b'import', 
       b'CONDITIONAL': b'if', 
       b'LOOPING': (b'compound', b'for while break continue'), 
       b'TRUTHVALUE': (b'truth', b'if while and or not BASICMETHODS'), 
       b'DEBUGGING': (b'debugger', b'pdb'), 
       b'CONTEXTMANAGERS': (b'context-managers', b'with')}

    def __init__(self, input=None, output=None):
        self._input = input
        self._output = output
        return

    input = property((lambda self: self._input or sys.stdin))
    output = property((lambda self: self._output or sys.stdout))

    def __repr__(self):
        if inspect.stack()[1][3] == b'?':
            self()
            return b''
        return b'<pydoc.Helper instance>'

    _GoInteractive = object()

    def __call__(self, request=_GoInteractive):
        if request is not self._GoInteractive:
            self.help(request)
        else:
            self.intro()
            self.interact()
            self.output.write(b'\nYou are now leaving help and returning to the Python interpreter.\nIf you want to ask for help on a particular object directly from the\ninterpreter, you can type "help(object)".  Executing "help(\'string\')"\nhas the same effect as typing a particular string at the help> prompt.\n')
        return

    def interact(self):
        self.output.write(b'\n')
        while True:
            try:
                request = self.getline(b'help> ')
                if not request:
                    break
            except (KeyboardInterrupt, EOFError):
                break

            request = strip(request)
            if len(request) > 2 and request[0] == request[-1] in (b"'", b'"') and request[0] not in request[1:-1]:
                request = request[1:-1]
            if lower(request) in (b'q', b'quit'):
                break
            self.help(request)

        return

    def getline(self, prompt):
        if self.input is sys.stdin:
            return raw_input(prompt)
        else:
            self.output.write(prompt)
            self.output.flush()
            return self.input.readline()

        return

    def help(self, request):
        if type(request) is type(b''):
            request = request.strip()
            if request == b'help':
                self.intro()
            elif request == b'keywords':
                self.listkeywords()
            elif request == b'symbols':
                self.listsymbols()
            elif request == b'topics':
                self.listtopics()
            if request == b'modules':
                self.listmodules()
            elif request[:8] == b'modules ':
                self.listmodules(split(request)[1])
            elif request in self.symbols:
                self.showsymbol(request)
            if request in self.keywords:
                self.showtopic(request)
            elif request in self.topics:
                self.showtopic(request)
            elif request:
                doc(request, b'Help on %s:')
        elif isinstance(request, Helper):
            self()
        else:
            doc(request, b'Help on %s:')
        self.output.write(b'\n')
        return

    def intro(self):
        self.output.write(b'\nWelcome to Python %s!  This is the online help utility.\n\nIf this is your first time using Python, you should definitely check out\nthe tutorial on the Internet at http://docs.python.org/%s/tutorial/.\n\nEnter the name of any module, keyword, or topic to get help on writing\nPython programs and using Python modules.  To quit this help utility and\nreturn to the interpreter, just type "quit".\n\nTo get a list of available modules, keywords, or topics, type "modules",\n"keywords", or "topics".  Each module also comes with a one-line summary\nof what it does; to list the modules whose summaries contain a given word\nsuch as "spam", type "modules spam".\n' % tuple([sys.version[:3]] * 2))
        return

    def list(self, items, columns=4, width=80):
        items = items[:]
        items.sort()
        colw = width / columns
        rows = (len(items) + columns - 1) / columns
        for row in range(rows):
            for col in range(columns):
                i = col * rows + row
                if i < len(items):
                    self.output.write(items[i])
                    if col < columns - 1:
                        self.output.write(b' ' + b' ' * (colw - 1 - len(items[i])))

            self.output.write(b'\n')

        return

    def listkeywords(self):
        self.output.write(b'\nHere is a list of the Python keywords.  Enter any keyword to get more help.\n\n')
        self.list(self.keywords.keys())
        return

    def listsymbols(self):
        self.output.write(b'\nHere is a list of the punctuation symbols which Python assigns special meaning\nto. Enter any symbol to get more help.\n\n')
        self.list(self.symbols.keys())
        return

    def listtopics(self):
        self.output.write(b'\nHere is a list of available topics.  Enter any topic name to get more help.\n\n')
        self.list(self.topics.keys())
        return

    def showtopic(self, topic, more_xrefs=b''):
        try:
            import pydoc_data.topics
        except ImportError:
            self.output.write(b'\nSorry, topic and keyword documentation is not available because the\nmodule "pydoc_data.topics" could not be found.\n')
            return

        target = self.topics.get(topic, self.keywords.get(topic))
        if not target:
            self.output.write(b'no documentation found for %s\n' % repr(topic))
            return
        if type(target) is type(b''):
            return self.showtopic(target, more_xrefs)
        label, xrefs = target
        try:
            doc = pydoc_data.topics.topics[label]
        except KeyError:
            self.output.write(b'no documentation found for %s\n' % repr(topic))
            return

        pager(strip(doc) + b'\n')
        if more_xrefs:
            xrefs = (xrefs or b'') + b' ' + more_xrefs
        if xrefs:
            import StringIO, formatter
            buffer = StringIO.StringIO()
            formatter.DumbWriter(buffer).send_flowing_data(b'Related help topics: ' + join(split(xrefs), b', ') + b'\n')
            self.output.write(b'\n%s\n' % buffer.getvalue())
        return

    def showsymbol(self, symbol):
        target = self.symbols[symbol]
        topic, _, xrefs = target.partition(b' ')
        self.showtopic(topic, xrefs)
        return

    def listmodules(self, key=b''):
        if key:
            self.output.write(b'\nHere is a list of matching modules.  Enter any module name to get more help.\n\n')
            apropos(key)
        else:
            self.output.write(b'\nPlease wait a moment while I gather a list of all available modules...\n\n')
            modules = {}

            def callback(path, modname, desc, modules=modules):
                if modname and modname[-9:] == b'.__init__':
                    modname = modname[:-9] + b' (package)'
                if find(modname, b'.') < 0:
                    modules[modname] = 1
                return

            def onerror(modname):
                callback(None, modname, None)
                return

            ModuleScanner().run(callback, onerror=onerror)
            self.list(modules.keys())
            self.output.write(b'\nEnter any module name to get more help.  Or, type "modules spam" to search\nfor modules whose descriptions contain the word "spam".\n')
        return


help = Helper()

class Scanner():

    def __init__(self, roots, children, descendp):
        self.roots = roots[:]
        self.state = []
        self.children = children
        self.descendp = descendp
        return

    def next(self):
        if not self.state:
            if not self.roots:
                return None
            root = self.roots.pop(0)
            self.state = [(root, self.children(root))]
        node, children = self.state[-1]
        if not children:
            self.state.pop()
            return self.next()
        else:
            child = children.pop(0)
            if self.descendp(child):
                self.state.append((child, self.children(child)))
            return child


class ModuleScanner():

    def run(self, callback, key=None, completer=None, onerror=None):
        if key:
            key = lower(key)
        self.quit = False
        seen = {}
        for modname in sys.builtin_module_names:
            if modname != b'__main__':
                seen[modname] = 1
                if key is None:
                    callback(None, modname, b'')
                else:
                    desc = split(__import__(modname).__doc__ or b'', b'\n')[0]
                    if find(lower(modname + b' - ' + desc), key) >= 0:
                        callback(None, modname, desc)

        for importer, modname, ispkg in pkgutil.walk_packages(onerror=onerror):
            if self.quit:
                break
            if key is None:
                callback(None, modname, b'')
            else:
                loader = importer.find_module(modname)
                if hasattr(loader, b'get_source'):
                    import StringIO
                    desc = source_synopsis(StringIO.StringIO(loader.get_source(modname))) or b''
                    if hasattr(loader, b'get_filename'):
                        path = loader.get_filename(modname)
                    else:
                        path = None
                else:
                    module = loader.load_module(modname)
                    desc = module.__doc__.splitlines()[0] if module.__doc__ else b''
                    path = getattr(module, b'__file__', None)
                if find(lower(modname + b' - ' + desc), key) >= 0:
                    callback(path, modname, desc)

        if completer:
            completer()
        return


def apropos(key):

    def callback(path, modname, desc):
        if modname[-9:] == b'.__init__':
            modname = modname[:-9] + b' (package)'
        print modname, desc and b'- ' + desc
        return

    def onerror(modname):
        return

    with warnings.catch_warnings():
        warnings.filterwarnings(b'ignore')
        ModuleScanner().run(callback, key, onerror=onerror)
    return


def serve(port, callback=None, completer=None):
    import BaseHTTPServer, mimetools, select

    class Message(mimetools.Message):

        def __init__(self, fp, seekable=1):
            Message = self.__class__
            Message.__bases__[0].__bases__[0].__init__(self, fp, seekable)
            self.encodingheader = self.getheader(b'content-transfer-encoding')
            self.typeheader = self.getheader(b'content-type')
            self.parsetype()
            self.parseplist()
            return

    class DocHandler(BaseHTTPServer.BaseHTTPRequestHandler):

        def send_document(self, title, contents):
            try:
                self.send_response(200)
                self.send_header(b'Content-Type', b'text/html')
                self.end_headers()
                self.wfile.write(html.page(title, contents))
            except IOError:
                pass

            return

        def do_GET(self):
            path = self.path
            if path[-5:] == b'.html':
                path = path[:-5]
            if path[:1] == b'/':
                path = path[1:]
            if path and path != b'.':
                try:
                    obj = locate(path, forceload=1)
                except ErrorDuringImport as value:
                    self.send_document(path, html.escape(str(value)))
                    return

                if obj:
                    self.send_document(describe(obj), html.document(obj, path))
                else:
                    self.send_document(path, b'no Python documentation found for %s' % repr(path))
            else:
                heading = html.heading(b'<big><big><strong>Python: Index of Modules</strong></big></big>', b'#ffffff', b'#7799ee')

                def bltinlink(name):
                    return b'<a href="%s.html">%s</a>' % (name, name)

                names = filter((lambda x: x != b'__main__'), sys.builtin_module_names)
                contents = html.multicolumn(names, bltinlink)
                indices = [
                 b'<p>' + html.bigsection(b'Built-in Modules', b'#ffffff', b'#ee77aa', contents)]
                seen = {}
                for dir in sys.path:
                    indices.append(html.index(dir, seen))

                contents = heading + join(indices) + b'<p align=right>\n<font color="#909090" face="helvetica, arial"><strong>\npydoc</strong> by Ka-Ping Yee &lt;ping@lfw.org&gt;</font>'
                self.send_document(b'Index of Modules', contents)
            return

        def log_message(self, *args):
            return

    class DocServer(BaseHTTPServer.HTTPServer):

        def __init__(self, port, callback):
            host = b'localhost'
            self.address = (host, port)
            self.callback = callback
            self.base.__init__(self, self.address, self.handler)
            return

        def serve_until_quit(self):
            import select
            self.quit = False
            while not self.quit:
                rd, wr, ex = select.select([self.socket.fileno()], [], [], 1)
                if rd:
                    self.handle_request()

            return

        def server_activate(self):
            self.base.server_activate(self)
            self.url = b'http://%s:%d/' % (self.address[0], self.server_port)
            if self.callback:
                self.callback(self)
            return

    DocServer.base = BaseHTTPServer.HTTPServer
    DocServer.handler = DocHandler
    DocHandler.MessageClass = Message
    try:
        try:
            DocServer(port, callback).serve_until_quit()
        except (KeyboardInterrupt, select.error):
            pass

    finally:
        if completer:
            completer()

    return


def gui():

    class GUI:

        def __init__(self, window, port=7464):
            self.window = window
            self.server = None
            self.scanner = None
            import Tkinter
            self.server_frm = Tkinter.Frame(window)
            self.title_lbl = Tkinter.Label(self.server_frm, text=b'Starting server...\n ')
            self.open_btn = Tkinter.Button(self.server_frm, text=b'open browser', command=self.open, state=b'disabled')
            self.quit_btn = Tkinter.Button(self.server_frm, text=b'quit serving', command=self.quit, state=b'disabled')
            self.search_frm = Tkinter.Frame(window)
            self.search_lbl = Tkinter.Label(self.search_frm, text=b'Search for')
            self.search_ent = Tkinter.Entry(self.search_frm)
            self.search_ent.bind(b'<Return>', self.search)
            self.stop_btn = Tkinter.Button(self.search_frm, text=b'stop', pady=0, command=self.stop, state=b'disabled')
            if sys.platform == b'win32':
                self.stop_btn.pack(side=b'right')
            self.window.title(b'pydoc')
            self.window.protocol(b'WM_DELETE_WINDOW', self.quit)
            self.title_lbl.pack(side=b'top', fill=b'x')
            self.open_btn.pack(side=b'left', fill=b'x', expand=1)
            self.quit_btn.pack(side=b'right', fill=b'x', expand=1)
            self.server_frm.pack(side=b'top', fill=b'x')
            self.search_lbl.pack(side=b'left')
            self.search_ent.pack(side=b'right', fill=b'x', expand=1)
            self.search_frm.pack(side=b'top', fill=b'x')
            self.search_ent.focus_set()
            font = (
             b'helvetica', sys.platform == b'win32' and 8 or 10)
            self.result_lst = Tkinter.Listbox(window, font=font, height=6)
            self.result_lst.bind(b'<Button-1>', self.select)
            self.result_lst.bind(b'<Double-Button-1>', self.goto)
            self.result_scr = Tkinter.Scrollbar(window, orient=b'vertical', command=self.result_lst.yview)
            self.result_lst.config(yscrollcommand=self.result_scr.set)
            self.result_frm = Tkinter.Frame(window)
            self.goto_btn = Tkinter.Button(self.result_frm, text=b'go to selected', command=self.goto)
            self.hide_btn = Tkinter.Button(self.result_frm, text=b'hide results', command=self.hide)
            self.goto_btn.pack(side=b'left', fill=b'x', expand=1)
            self.hide_btn.pack(side=b'right', fill=b'x', expand=1)
            self.window.update()
            self.minwidth = self.window.winfo_width()
            self.minheight = self.window.winfo_height()
            self.bigminheight = self.server_frm.winfo_reqheight() + self.search_frm.winfo_reqheight() + self.result_lst.winfo_reqheight() + self.result_frm.winfo_reqheight()
            self.bigwidth, self.bigheight = self.minwidth, self.bigminheight
            self.expanded = 0
            self.window.wm_geometry(b'%dx%d' % (self.minwidth, self.minheight))
            self.window.wm_minsize(self.minwidth, self.minheight)
            self.window.tk.willdispatch()
            import threading
            threading.Thread(target=serve, args=(port, self.ready, self.quit)).start()
            return

        def ready(self, server):
            self.server = server
            self.title_lbl.config(text=b'Python documentation server at\n' + server.url)
            self.open_btn.config(state=b'normal')
            self.quit_btn.config(state=b'normal')
            return

        def open(self, event=None, url=None):
            url = url or self.server.url
            try:
                import webbrowser
                webbrowser.open(url)
            except ImportError:
                if sys.platform == b'win32':
                    os.system(b'start "%s"' % url)
                else:
                    rc = os.system(b'netscape -remote "openURL(%s)" &' % url)
                    if rc:
                        os.system(b'netscape "%s" &' % url)

            return

        def quit(self, event=None):
            if self.server:
                self.server.quit = 1
            self.window.quit()
            return

        def search(self, event=None):
            key = self.search_ent.get()
            self.stop_btn.pack(side=b'right')
            self.stop_btn.config(state=b'normal')
            self.search_lbl.config(text=b'Searching for "%s"...' % key)
            self.search_ent.forget()
            self.search_lbl.pack(side=b'left')
            self.result_lst.delete(0, b'end')
            self.goto_btn.config(state=b'disabled')
            self.expand()
            import threading
            if self.scanner:
                self.scanner.quit = 1
            self.scanner = ModuleScanner()

            def onerror(modname):
                return

            threading.Thread(target=self.scanner.run, args=(
             self.update, key, self.done), kwargs=dict(onerror=onerror)).start()
            return

        def update(self, path, modname, desc):
            if modname[-9:] == b'.__init__':
                modname = modname[:-9] + b' (package)'
            self.result_lst.insert(b'end', modname + b' - ' + (desc or b'(no description)'))
            return

        def stop(self, event=None):
            if self.scanner:
                self.scanner.quit = 1
                self.scanner = None
            return

        def done(self):
            self.scanner = None
            self.search_lbl.config(text=b'Search for')
            self.search_lbl.pack(side=b'left')
            self.search_ent.pack(side=b'right', fill=b'x', expand=1)
            if sys.platform != b'win32':
                self.stop_btn.forget()
            self.stop_btn.config(state=b'disabled')
            return

        def select(self, event=None):
            self.goto_btn.config(state=b'normal')
            return

        def goto(self, event=None):
            selection = self.result_lst.curselection()
            if selection:
                modname = split(self.result_lst.get(selection[0]))[0]
                self.open(url=self.server.url + modname + b'.html')
            return

        def collapse(self):
            if not self.expanded:
                return
            self.result_frm.forget()
            self.result_scr.forget()
            self.result_lst.forget()
            self.bigwidth = self.window.winfo_width()
            self.bigheight = self.window.winfo_height()
            self.window.wm_geometry(b'%dx%d' % (self.minwidth, self.minheight))
            self.window.wm_minsize(self.minwidth, self.minheight)
            self.expanded = 0
            return

        def expand(self):
            if self.expanded:
                return
            self.result_frm.pack(side=b'bottom', fill=b'x')
            self.result_scr.pack(side=b'right', fill=b'y')
            self.result_lst.pack(side=b'top', fill=b'both', expand=1)
            self.window.wm_geometry(b'%dx%d' % (self.bigwidth, self.bigheight))
            self.window.wm_minsize(self.minwidth, self.bigminheight)
            self.expanded = 1
            return

        def hide(self, event=None):
            self.stop()
            self.collapse()
            return

    import Tkinter
    try:
        root = Tkinter.Tk()
        try:
            gui = GUI(root)
            root.mainloop()
        finally:
            root.destroy()

    except KeyboardInterrupt:
        pass

    return


def ispath(x):
    return isinstance(x, str) and find(x, os.sep) >= 0


def cli():
    import getopt

    class BadUsage:
        pass

    if b'' not in sys.path:
        scriptdir = os.path.dirname(sys.argv[0])
        if scriptdir in sys.path:
            sys.path.remove(scriptdir)
        sys.path.insert(0, b'.')
    try:
        opts, args = getopt.getopt(sys.argv[1:], b'gk:p:w')
        writing = 0
        for opt, val in opts:
            if opt == b'-g':
                gui()
                return
            if opt == b'-k':
                apropos(val)
                return
            if opt == b'-p':
                try:
                    port = int(val)
                except ValueError:
                    raise BadUsage

                def ready(server):
                    print b'pydoc server ready at %s' % server.url
                    return

                def stopped():
                    print b'pydoc server stopped'
                    return

                serve(port, ready, stopped)
                return
            if opt == b'-w':
                writing = 1

        if not args:
            raise BadUsage
        for arg in args:
            if ispath(arg) and not os.path.exists(arg):
                print b'file %r does not exist' % arg
                break
            try:
                if ispath(arg) and os.path.isfile(arg):
                    arg = importfile(arg)
                if writing:
                    if ispath(arg) and os.path.isdir(arg):
                        writedocs(arg)
                    else:
                        writedoc(arg)
                else:
                    help.help(arg)
            except ErrorDuringImport as value:
                print value

    except (getopt.error, BadUsage):
        cmd = os.path.basename(sys.argv[0])
        print b"pydoc - the Python documentation tool\n\n%s <name> ...\n    Show text documentation on something.  <name> may be the name of a\n    Python keyword, topic, function, module, or package, or a dotted\n    reference to a class or function within a module or module in a\n    package.  If <name> contains a '%s', it is used as the path to a\n    Python source file to document. If name is 'keywords', 'topics',\n    or 'modules', a listing of these things is displayed.\n\n%s -k <keyword>\n    Search for a keyword in the synopsis lines of all available modules.\n\n%s -p <port>\n    Start an HTTP server on the given port on the local machine.  Port\n    number 0 can be used to get an arbitrary unused port.\n\n%s -g\n    Pop up a graphical interface for finding and serving documentation.\n\n%s -w <name> ...\n    Write out the HTML documentation for a module to a file in the current\n    directory.  If <name> contains a '%s', it is treated as a filename; if\n    it names a directory, documentation is written for all the contents.\n" % (cmd, os.sep, cmd, cmd, cmd, cmd, os.sep)

    return


if __name__ == b'__main__':
    cli()
