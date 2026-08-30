__revision__ = b'$Id$'
import os, string, sys
from types import *
try:
    import warnings
except ImportError:
    warnings = None

class Extension:

    def __init__(self, name, sources, include_dirs=None, define_macros=None, undef_macros=None, library_dirs=None, libraries=None, runtime_library_dirs=None, extra_objects=None, extra_compile_args=None, extra_link_args=None, export_symbols=None, swig_opts=None, depends=None, language=None, **kw):
        self.name = name
        self.sources = sources
        self.include_dirs = include_dirs or []
        self.define_macros = define_macros or []
        self.undef_macros = undef_macros or []
        self.library_dirs = library_dirs or []
        self.libraries = libraries or []
        self.runtime_library_dirs = runtime_library_dirs or []
        self.extra_objects = extra_objects or []
        self.extra_compile_args = extra_compile_args or []
        self.extra_link_args = extra_link_args or []
        self.export_symbols = export_symbols or []
        self.swig_opts = swig_opts or []
        self.depends = depends or []
        self.language = language
        if len(kw):
            L = kw.keys()
            L.sort()
            L = map(repr, L)
            msg = b'Unknown Extension options: ' + string.join(L, b', ')
            if warnings is not None:
                warnings.warn(msg)
            else:
                sys.stderr.write(msg + b'\n')
        return


def read_setup_file(filename):
    from distutils.sysconfig import parse_makefile, expand_makefile_vars, _variable_rx
    from distutils.text_file import TextFile
    from distutils.util import split_quoted
    vars = parse_makefile(filename)
    file = TextFile(filename, strip_comments=1, skip_blanks=1, join_lines=1, lstrip_ws=1, rstrip_ws=1)
    try:
        extensions = []
        while 1:
            line = file.readline()
            if line is None:
                break
            if _variable_rx.match(line):
                continue
                if line[0] == line[-1] == b'*':
                    file.warn(b"'%s' lines not handled yet" % line)
                    continue
            line = expand_makefile_vars(line, vars)
            words = split_quoted(line)
            module = words[0]
            ext = Extension(module, [])
            append_next_word = None
            for word in words[1:]:
                if append_next_word is not None:
                    append_next_word.append(word)
                    append_next_word = None
                    continue
                suffix = os.path.splitext(word)[1]
                switch = word[0:2]
                value = word[2:]
                if suffix in (b'.c', b'.cc', b'.cpp', b'.cxx', b'.c++', b'.m', b'.mm'):
                    ext.sources.append(word)
                elif switch == b'-I':
                    ext.include_dirs.append(value)
                elif switch == b'-D':
                    equals = string.find(value, b'=')
                    if equals == -1:
                        ext.define_macros.append((value, None))
                    else:
                        ext.define_macros.append((value[0:equals],
                         value[equals + 2:]))
                elif switch == b'-U':
                    ext.undef_macros.append(value)
                elif switch == b'-C':
                    ext.extra_compile_args.append(word)
                elif switch == b'-l':
                    ext.libraries.append(value)
                elif switch == b'-L':
                    ext.library_dirs.append(value)
                elif switch == b'-R':
                    ext.runtime_library_dirs.append(value)
                elif word == b'-rpath':
                    append_next_word = ext.runtime_library_dirs
                elif word == b'-Xlinker':
                    append_next_word = ext.extra_link_args
                elif word == b'-Xcompiler':
                    append_next_word = ext.extra_compile_args
                elif switch == b'-u':
                    ext.extra_link_args.append(word)
                    if not value:
                        append_next_word = ext.extra_link_args
                elif word == b'-Xcompiler':
                    append_next_word = ext.extra_compile_args
                elif switch == b'-u':
                    ext.extra_link_args.append(word)
                    if not value:
                        append_next_word = ext.extra_link_args
                elif suffix in (b'.a', b'.so', b'.sl', b'.o', b'.dylib'):
                    ext.extra_objects.append(word)
                else:
                    file.warn(b"unrecognized argument '%s'" % word)

            extensions.append(ext)

    finally:
        file.close()

    return extensions
