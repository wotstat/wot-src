import linecache, sys, types
__all__ = [
 2, 3, 4, 
 5, 6, 7, 
 8, 9]

def warnpy3k(message, category=None, stacklevel=1):
    if sys.py3kwarning:
        if category is None:
            category = DeprecationWarning
        warn(message, category, stacklevel + 1)
    return


def _show_warning(message, category, filename, lineno, file=None, line=None):
    if file is None:
        file = sys.stderr
        if file is None:
            return
    try:
        file.write(formatwarning(message, category, filename, lineno, line))
    except (IOError, UnicodeError):
        pass

    return


showwarning = _show_warning

def formatwarning(message, category, filename, lineno, line=None):
    try:
        unicodetype = unicode
    except NameError:
        unicodetype = ()

    try:
        message = str(message)
    except UnicodeEncodeError:
        pass

    s = b'%s: %s: %s\n' % (lineno, category.__name__, message)
    line = linecache.getline(filename, lineno) if line is None else line
    if line:
        line = line.strip()
        if isinstance(s, unicodetype) and isinstance(line, str):
            line = unicode(line, b'latin1')
        s += b'  %s\n' % line
    if isinstance(s, unicodetype) and isinstance(filename, str):
        enc = sys.getfilesystemencoding()
        if enc:
            try:
                filename = unicode(filename, enc)
            except UnicodeDecodeError:
                pass

    s = b'%s:%s' % (filename, s)
    return s


def filterwarnings(action, message=b'', category=Warning, module=b'', lineno=0, append=0):
    import re
    item = (
     action, re.compile(message, re.I), category,
     re.compile(module), int(lineno))
    if append:
        filters.append(item)
    else:
        filters.insert(0, item)
    return


def simplefilter(action, category=Warning, lineno=0, append=0):
    item = (
     action, None, category, None, int(lineno))
    if append:
        filters.append(item)
    else:
        filters.insert(0, item)
    return


def resetwarnings():
    filters[:] = []
    return


class _OptionError(Exception):
    pass


def _processoptions(args):
    for arg in args:
        try:
            _setoption(arg)
        except _OptionError as msg:
            print >> sys.stderr, b'Invalid -W option ignored:', msg

    return


def _setoption(arg):
    import re
    parts = arg.split(b':')
    if len(parts) > 5:
        raise _OptionError(b'too many fields (max 5): %r' % (arg,))
    while len(parts) < 5:
        parts.append(b'')

    action, message, category, module, lineno = [s.strip() for s in parts]
    action = _getaction(action)
    message = re.escape(message)
    category = _getcategory(category)
    module = re.escape(module)
    if module:
        module = module + b'$'
    if lineno:
        try:
            lineno = int(lineno)
            if lineno < 0:
                raise ValueError
        except (ValueError, OverflowError):
            raise _OptionError(b'invalid lineno %r' % (lineno,))

    else:
        lineno = 0
    filterwarnings(action, message, category, module, lineno)
    return


def _getaction(action):
    if not action:
        return b'default'
    if action == b'all':
        return b'always'
    for a in (b'default', b'always', b'ignore', b'module', b'once', b'error'):
        if a.startswith(action):
            return a

    raise _OptionError(b'invalid action: %r' % (action,))
    return


def _getcategory(category):
    import re
    if not category:
        return Warning
    else:
        if re.match(b'^[a-zA-Z0-9_]+$', category):
            try:
                cat = eval(category)
            except NameError:
                raise _OptionError(b'unknown warning category: %r' % (category,))

        else:
            i = category.rfind(b'.')
            module = category[:i]
            klass = category[i + 1:]
            try:
                m = __import__(module, None, None, [klass])
            except ImportError:
                raise _OptionError(b'invalid module name: %r' % (module,))

            try:
                cat = getattr(m, klass)
            except AttributeError:
                raise _OptionError(b'unknown warning category: %r' % (category,))

        if not issubclass(cat, Warning):
            raise _OptionError(b'invalid warning category: %r' % (category,))
        return cat


def warn(message, category=None, stacklevel=1):
    if isinstance(message, Warning):
        category = message.__class__
    if category is None:
        category = UserWarning
    try:
        caller = sys._getframe(stacklevel)
    except ValueError:
        globals = sys.__dict__
        lineno = 1
    else:
        globals = caller.f_globals
        lineno = caller.f_lineno

    if b'__name__' in globals:
        module = globals[b'__name__']
    else:
        module = b'<string>'
    filename = globals.get(b'__file__')
    if filename:
        fnl = filename.lower()
        if fnl.endswith((b'.pyc', b'.pyo')):
            filename = filename[:-1]
    elif module == b'__main__':
        try:
            filename = sys.argv[0]
        except AttributeError:
            filename = b'__main__'

    if not filename:
        filename = module
    registry = globals.setdefault(b'__warningregistry__', {})
    warn_explicit(message, category, filename, lineno, module, registry, globals)
    return


def warn_explicit(message, category, filename, lineno, module=None, registry=None, module_globals=None):
    lineno = int(lineno)
    if module is None:
        module = filename or b'<unknown>'
        if module[-3:].lower() == b'.py':
            module = module[:-3]
    if registry is None:
        registry = {}
    if isinstance(message, Warning):
        text = str(message)
        category = message.__class__
    else:
        text = message
        message = category(message)
    key = (
     text, category, lineno)
    if registry.get(key):
        return
    else:
        for item in filters:
            action, msg, cat, mod, ln = item
            if (msg is None or msg.match(text)) and issubclass(category, cat) and (mod is None or mod.match(module)) and (ln == 0 or lineno == ln):
                break
        else:
            action = defaultaction

        if action == b'ignore':
            registry[key] = 1
            return
        linecache.getlines(filename, module_globals)
        if action == b'error':
            raise message
        if action == b'once':
            registry[key] = 1
            oncekey = (text, category)
            if onceregistry.get(oncekey):
                return
            onceregistry[oncekey] = 1
        elif action == b'always':
            pass
        elif action == b'module':
            registry[key] = 1
            altkey = (text, category, 0)
            if registry.get(altkey):
                return
            registry[altkey] = 1
        elif action == b'default':
            registry[key] = 1
        else:
            raise RuntimeError(b'Unrecognized action (%r) in warnings.filters:\n %s' % (
             action, item))
        showwarning(message, category, filename, lineno)
        return


class WarningMessage(object):
    _WARNING_DETAILS = (b'message', b'category', b'filename', b'lineno', b'file', b'line')

    def __init__(self, message, category, filename, lineno, file=None, line=None):
        self.message = message
        self.category = category
        self.filename = filename
        self.lineno = lineno
        self.file = file
        self.line = line
        self._category_name = category.__name__ if category else None
        return

    def __str__(self):
        return b'{message : %r, category : %r, filename : %r, lineno : %s, line : %r}' % (
         self.message, self._category_name,
         self.filename, self.lineno, self.line)


class catch_warnings(object):

    def __init__(self, record=False, module=None):
        self._record = record
        self._module = sys.modules[b'warnings'] if module is None else module
        self._entered = False
        return

    def __repr__(self):
        args = []
        if self._record:
            args.append(b'record=True')
        if self._module is not sys.modules[b'warnings']:
            args.append(b'module=%r' % self._module)
        name = type(self).__name__
        return b'%s(%s)' % (name, (b', ').join(args))

    def __enter__(self):
        if self._entered:
            raise RuntimeError(b'Cannot enter %r twice' % self)
        self._entered = True
        self._filters = self._module.filters
        self._module.filters = self._filters[:]
        self._showwarning = self._module.showwarning
        if self._record:
            log = []

            def showwarning(*args, **kwargs):
                log.append(WarningMessage(*args, **kwargs))
                return

            self._module.showwarning = showwarning
            return log
        else:
            return
            return

    def __exit__(self, *exc_info):
        if not self._entered:
            raise RuntimeError(b'Cannot exit %r without entering first' % self)
        self._module.filters = self._filters
        self._module.showwarning = self._showwarning
        return


_warnings_defaults = False
try:
    from _warnings import filters, default_action, once_registry, warn, warn_explicit
    defaultaction = default_action
    onceregistry = once_registry
    _warnings_defaults = True
except ImportError:
    filters = []
    defaultaction = b'default'
    onceregistry = {}

_processoptions(sys.warnoptions)
if not _warnings_defaults:
    silence = [
     ImportWarning, PendingDeprecationWarning]
    if not sys.py3kwarning and not sys.flags.division_warning:
        silence.append(DeprecationWarning)
    for cls in silence:
        simplefilter(b'ignore', category=cls)

    bytes_warning = sys.flags.bytes_warning
    if bytes_warning > 1:
        bytes_action = b'error'
    elif bytes_warning:
        bytes_action = b'default'
    else:
        bytes_action = b'ignore'
    simplefilter(bytes_action, category=BytesWarning, append=1)
del _warnings_defaults
