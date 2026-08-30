try:
    from collections import OrderedDict as _default_dict
except ImportError:
    _default_dict = dict

import re
__all__ = [
 3, 4, 5, 
 6, 7, 
 8, 9, 
 10, 
 11, 12, 13, 
 14, 15]
DEFAULTSECT = b'DEFAULT'
MAX_INTERPOLATION_DEPTH = 10

class Error(Exception):

    def _get_message(self):
        return self.__message

    def _set_message(self, value):
        self.__message = value
        return

    message = property(_get_message, _set_message)

    def __init__(self, msg=b''):
        self.message = msg
        Exception.__init__(self, msg)
        return

    def __repr__(self):
        return self.message

    __str__ = __repr__


class NoSectionError(Error):

    def __init__(self, section):
        Error.__init__(self, b'No section: %r' % (section,))
        self.section = section
        self.args = (section,)
        return


class DuplicateSectionError(Error):

    def __init__(self, section):
        Error.__init__(self, b'Section %r already exists' % section)
        self.section = section
        self.args = (section,)
        return


class NoOptionError(Error):

    def __init__(self, option, section):
        Error.__init__(self, b'No option %r in section: %r' % (
         option, section))
        self.option = option
        self.section = section
        self.args = (option, section)
        return


class InterpolationError(Error):

    def __init__(self, option, section, msg):
        Error.__init__(self, msg)
        self.option = option
        self.section = section
        self.args = (option, section, msg)
        return


class InterpolationMissingOptionError(InterpolationError):

    def __init__(self, option, section, rawval, reference):
        msg = b'Bad value substitution:\n\tsection: [%s]\n\toption : %s\n\tkey    : %s\n\trawval : %s\n' % (
         section, option, reference, rawval)
        InterpolationError.__init__(self, option, section, msg)
        self.reference = reference
        self.args = (option, section, rawval, reference)
        return


class InterpolationSyntaxError(InterpolationError):
    pass


class InterpolationDepthError(InterpolationError):

    def __init__(self, option, section, rawval):
        msg = b'Value interpolation too deeply recursive:\n\tsection: [%s]\n\toption : %s\n\trawval : %s\n' % (
         section, option, rawval)
        InterpolationError.__init__(self, option, section, msg)
        self.args = (option, section, rawval)
        return


class ParsingError(Error):

    def __init__(self, filename):
        Error.__init__(self, b'File contains parsing errors: %s' % filename)
        self.filename = filename
        self.errors = []
        self.args = (filename,)
        return

    def append(self, lineno, line):
        self.errors.append((lineno, line))
        self.message += b'\n\t[line %2d]: %s' % (lineno, line)
        return


class MissingSectionHeaderError(ParsingError):

    def __init__(self, filename, lineno, line):
        Error.__init__(self, b'File contains no section headers.\nfile: %s, line: %d\n%r' % (
         filename, lineno, line))
        self.filename = filename
        self.lineno = lineno
        self.line = line
        self.args = (filename, lineno, line)
        return


class RawConfigParser():

    def __init__(self, defaults=None, dict_type=_default_dict, allow_no_value=False):
        self._dict = dict_type
        self._sections = self._dict()
        self._defaults = self._dict()
        if allow_no_value:
            self._optcre = self.OPTCRE_NV
        else:
            self._optcre = self.OPTCRE
        if defaults:
            for key, value in defaults.items():
                self._defaults[self.optionxform(key)] = value

        return

    def defaults(self):
        return self._defaults

    def sections(self):
        return self._sections.keys()

    def add_section(self, section):
        if section.lower() == b'default':
            raise ValueError, b'Invalid section name: %s' % section
        if section in self._sections:
            raise DuplicateSectionError(section)
        self._sections[section] = self._dict()
        return

    def has_section(self, section):
        return section in self._sections

    def options(self, section):
        try:
            opts = self._sections[section].copy()
        except KeyError:
            raise NoSectionError(section)

        opts.update(self._defaults)
        if b'__name__' in opts:
            del opts[b'__name__']
        return opts.keys()

    def read(self, filenames):
        if isinstance(filenames, basestring):
            filenames = [
             filenames]
        read_ok = []
        for filename in filenames:
            try:
                fp = open(filename)
            except IOError:
                continue

            self._read(fp, filename)
            fp.close()
            read_ok.append(filename)

        return read_ok

    def readfp(self, fp, filename=None):
        if filename is None:
            try:
                filename = fp.name
            except AttributeError:
                filename = b'<???>'

        self._read(fp, filename)
        return

    def get(self, section, option):
        opt = self.optionxform(option)
        if section not in self._sections:
            if section != DEFAULTSECT:
                raise NoSectionError(section)
            if opt in self._defaults:
                return self._defaults[opt]
            raise NoOptionError(option, section)
        elif opt in self._sections[section]:
            return self._sections[section][opt]
        if opt in self._defaults:
            return self._defaults[opt]
        raise NoOptionError(option, section)
        return

    def items(self, section):
        try:
            d2 = self._sections[section]
        except KeyError:
            if section != DEFAULTSECT:
                raise NoSectionError(section)
            d2 = self._dict()

        d = self._defaults.copy()
        d.update(d2)
        if b'__name__' in d:
            del d[b'__name__']
        return d.items()

    def _get(self, section, conv, option):
        return conv(self.get(section, option))

    def getint(self, section, option):
        return self._get(section, int, option)

    def getfloat(self, section, option):
        return self._get(section, float, option)

    _boolean_states = {b'1': True, b'yes': True, b'true': True, b'on': True, b'0': False, 
       b'no': False, b'false': False, b'off': False}

    def getboolean(self, section, option):
        v = self.get(section, option)
        if v.lower() not in self._boolean_states:
            raise ValueError, b'Not a boolean: %s' % v
        return self._boolean_states[v.lower()]

    def optionxform(self, optionstr):
        return optionstr.lower()

    def has_option(self, section, option):
        if not section or section == DEFAULTSECT:
            option = self.optionxform(option)
            return option in self._defaults
        else:
            if section not in self._sections:
                return False
            option = self.optionxform(option)
            return option in self._sections[section] or option in self._defaults

        return

    def set(self, section, option, value=None):
        if not section or section == DEFAULTSECT:
            sectdict = self._defaults
        else:
            try:
                sectdict = self._sections[section]
            except KeyError:
                raise NoSectionError(section)

        sectdict[self.optionxform(option)] = value
        return

    def write(self, fp):
        if self._defaults:
            fp.write(b'[%s]\n' % DEFAULTSECT)
            for key, value in self._defaults.items():
                fp.write(b'%s = %s\n' % (key, str(value).replace(b'\n', b'\n\t')))

            fp.write(b'\n')
        for section in self._sections:
            fp.write(b'[%s]\n' % section)
            for key, value in self._sections[section].items():
                if key == b'__name__':
                    continue
                if value is not None or self._optcre == self.OPTCRE:
                    key = (b' = ').join((key, str(value).replace(b'\n', b'\n\t')))
                fp.write(b'%s\n' % key)

            fp.write(b'\n')

        return

    def remove_option(self, section, option):
        if not section or section == DEFAULTSECT:
            sectdict = self._defaults
        else:
            try:
                sectdict = self._sections[section]
            except KeyError:
                raise NoSectionError(section)

        option = self.optionxform(option)
        existed = option in sectdict
        if existed:
            del sectdict[option]
        return existed

    def remove_section(self, section):
        existed = section in self._sections
        if existed:
            del self._sections[section]
        return existed

    SECTCRE = re.compile(b'\\[(?P<header>[^]]+)\\]')
    OPTCRE = re.compile(b'(?P<option>[^:=\\s][^:=]*)\\s*(?P<vi>[:=])\\s*(?P<value>.*)$')
    OPTCRE_NV = re.compile(b'(?P<option>[^:=\\s][^:=]*)\\s*(?:(?P<vi>[:=])\\s*(?P<value>.*))?$')

    def _read(self, fp, fpname):
        cursect = None
        optname = None
        lineno = 0
        e = None
        while True:
            line = fp.readline()
            if not line:
                break
            lineno = lineno + 1
            if line.strip() == b'' or line[0] in b'#;':
                continue
            if line.split(None, 1)[0].lower() == b'rem' and line[0] in b'rR':
                continue
            if line[0].isspace() and cursect is not None and optname:
                value = line.strip()
                if value:
                    cursect[optname].append(value)
            else:
                mo = self.SECTCRE.match(line)
                if mo:
                    sectname = mo.group(b'header')
                    if sectname in self._sections:
                        cursect = self._sections[sectname]
                    elif sectname == DEFAULTSECT:
                        cursect = self._defaults
                    else:
                        cursect = self._dict()
                        cursect[b'__name__'] = sectname
                        self._sections[sectname] = cursect
                    optname = None
                elif cursect is None:
                    raise MissingSectionHeaderError(fpname, lineno, line)
                else:
                    mo = self._optcre.match(line)
                    if mo:
                        optname, vi, optval = mo.group(b'option', b'vi', b'value')
                        optname = self.optionxform(optname.rstrip())
                        if optval is not None:
                            if vi in (b'=', b':') and b';' in optval:
                                pos = optval.find(b';')
                                if pos != -1 and optval[pos - 1].isspace():
                                    optval = optval[:pos]
                            optval = optval.strip()
                            if optval == b'""':
                                optval = b''
                            cursect[optname] = [
                             optval]
                        else:
                            cursect[optname] = optval
                    elif not e:
                        e = ParsingError(fpname)
                    e.append(lineno, repr(line))

        if e:
            raise e
        all_sections = [
         self._defaults]
        all_sections.extend(self._sections.values())
        for options in all_sections:
            for name, val in options.items():
                if isinstance(val, list):
                    options[name] = (b'\n').join(val)

        return


import UserDict as _UserDict

class _Chainmap(_UserDict.DictMixin):

    def __init__(self, *maps):
        self._maps = maps
        return

    def __getitem__(self, key):
        for mapping in self._maps:
            try:
                return mapping[key]
            except KeyError:
                pass

        raise KeyError(key)
        return

    def keys(self):
        result = []
        seen = set()
        for mapping in self._maps:
            for key in mapping:
                if key not in seen:
                    result.append(key)
                    seen.add(key)

        return result


class ConfigParser(RawConfigParser):

    def get(self, section, option, raw=False, vars=None):
        sectiondict = {}
        try:
            sectiondict = self._sections[section]
        except KeyError:
            if section != DEFAULTSECT:
                raise NoSectionError(section)

        vardict = {}
        if vars:
            for key, value in vars.items():
                vardict[self.optionxform(key)] = value

        d = _Chainmap(vardict, sectiondict, self._defaults)
        option = self.optionxform(option)
        try:
            value = d[option]
        except KeyError:
            raise NoOptionError(option, section)

        if raw or value is None:
            return value
        return self._interpolate(section, option, value, d)
        return

    def items(self, section, raw=False, vars=None):
        d = self._defaults.copy()
        try:
            d.update(self._sections[section])
        except KeyError:
            if section != DEFAULTSECT:
                raise NoSectionError(section)

        if vars:
            for key, value in vars.items():
                d[self.optionxform(key)] = value

        options = d.keys()
        if b'__name__' in options:
            options.remove(b'__name__')
        if raw:
            return [(option, d[option]) for option in options]
        else:
            return [(option, self._interpolate(section, option, d[option], d)) for option in options]

        return

    def _interpolate(self, section, option, rawval, vars):
        value = rawval
        depth = MAX_INTERPOLATION_DEPTH
        while depth:
            depth -= 1
            if value and b'%(' in value:
                value = self._KEYCRE.sub(self._interpolation_replace, value)
                try:
                    value = value % vars
                except KeyError as e:
                    raise InterpolationMissingOptionError(option, section, rawval, e.args[0])

            else:
                break

        if value and b'%(' in value:
            raise InterpolationDepthError(option, section, rawval)
        return value

    _KEYCRE = re.compile(b'%\\(([^)]*)\\)s|.')

    def _interpolation_replace(self, match):
        s = match.group(1)
        if s is None:
            return match.group()
        else:
            return b'%%(%s)s' % self.optionxform(s)
            return


class SafeConfigParser(ConfigParser):

    def _interpolate(self, section, option, rawval, vars):
        L = []
        self._interpolate_some(option, L, rawval, section, vars, 1)
        return (b'').join(L)

    _interpvar_re = re.compile(b'%\\(([^)]+)\\)s')

    def _interpolate_some(self, option, accum, rest, section, map, depth):
        if depth > MAX_INTERPOLATION_DEPTH:
            raise InterpolationDepthError(option, section, rest)
        while rest:
            p = rest.find(b'%')
            if p < 0:
                accum.append(rest)
                return
            if p > 0:
                accum.append(rest[:p])
                rest = rest[p:]
            c = rest[1:2]
            if c == b'%':
                accum.append(b'%')
                rest = rest[2:]
            elif c == b'(':
                m = self._interpvar_re.match(rest)
                if m is None:
                    raise InterpolationSyntaxError(option, section, b'bad interpolation variable reference %r' % rest)
                var = self.optionxform(m.group(1))
                rest = rest[m.end():]
                try:
                    v = map[var]
                except KeyError:
                    raise InterpolationMissingOptionError(option, section, rest, var)

                if b'%' in v:
                    self._interpolate_some(option, accum, v, section, map, depth + 1)
                else:
                    accum.append(v)
            else:
                raise InterpolationSyntaxError(option, section, b"'%%' must be followed by '%%' or '(', found: %r" % (rest,))

        return

    def set(self, section, option, value=None):
        if self._optcre is self.OPTCRE or value:
            if not isinstance(value, basestring):
                raise TypeError(b'option values must be strings')
        if value is not None:
            tmp_value = value.replace(b'%%', b'')
            tmp_value = self._interpvar_re.sub(b'', tmp_value)
            if b'%' in tmp_value:
                raise ValueError(b'invalid interpolation syntax in %r at position %d' % (
                 value, tmp_value.find(b'%')))
        ConfigParser.set(self, section, option, value)
        return
