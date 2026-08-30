__version__ = b'1.5.3'
__all__ = [
 1, 
 2, 
 3, 
 4, 
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11, 
 12, 
 13, 
 14, 
 15, 
 16]
__copyright__ = b'\nCopyright (c) 2001-2006 Gregory P. Ward.  All rights reserved.\nCopyright (c) 2002-2006 Python Software Foundation.  All rights reserved.\n\nRedistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are\nmet:\n\n  * Redistributions of source code must retain the above copyright\n    notice, this list of conditions and the following disclaimer.\n\n  * Redistributions in binary form must reproduce the above copyright\n    notice, this list of conditions and the following disclaimer in the\n    documentation and/or other materials provided with the distribution.\n\n  * Neither the name of the author nor the names of its\n    contributors may be used to endorse or promote products derived from\n    this software without specific prior written permission.\n\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS\nIS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED\nTO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A\nPARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR\nCONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,\nEXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,\nPROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR\nPROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF\nLIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING\nNEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS\nSOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n'
import sys, os, types, textwrap

def _repr(self):
    return b'<%s at 0x%x: %s>' % (self.__class__.__name__, id(self), self)


try:
    from gettext import gettext
except ImportError:

    def gettext(message):
        return message


_ = gettext

class OptParseError(Exception):

    def __init__(self, msg):
        self.msg = msg
        return

    def __str__(self):
        return self.msg


class OptionError(OptParseError):

    def __init__(self, msg, option):
        self.msg = msg
        self.option_id = str(option)
        return

    def __str__(self):
        if self.option_id:
            return b'option %s: %s' % (self.option_id, self.msg)
        else:
            return self.msg

        return


class OptionConflictError(OptionError):
    pass


class OptionValueError(OptParseError):
    pass


class BadOptionError(OptParseError):

    def __init__(self, opt_str):
        self.opt_str = opt_str
        return

    def __str__(self):
        return _(b'no such option: %s') % self.opt_str


class AmbiguousOptionError(BadOptionError):

    def __init__(self, opt_str, possibilities):
        BadOptionError.__init__(self, opt_str)
        self.possibilities = possibilities
        return

    def __str__(self):
        return _(b'ambiguous option: %s (%s?)') % (
         self.opt_str, (b', ').join(self.possibilities))


class HelpFormatter():
    NO_DEFAULT_VALUE = b'none'

    def __init__(self, indent_increment, max_help_position, width, short_first):
        self.parser = None
        self.indent_increment = indent_increment
        if width is None:
            try:
                width = int(os.environ[b'COLUMNS'])
            except (KeyError, ValueError):
                width = 80

            width -= 2
        self.width = width
        self.help_position = self.max_help_position = min(max_help_position, max(width - 20, indent_increment * 2))
        self.current_indent = 0
        self.level = 0
        self.help_width = None
        self.short_first = short_first
        self.default_tag = b'%default'
        self.option_strings = {}
        self._short_opt_fmt = b'%s %s'
        self._long_opt_fmt = b'%s=%s'
        return

    def set_parser(self, parser):
        self.parser = parser
        return

    def set_short_opt_delimiter(self, delim):
        if delim not in (b'', b' '):
            raise ValueError(b'invalid metavar delimiter for short options: %r' % delim)
        self._short_opt_fmt = b'%s' + delim + b'%s'
        return

    def set_long_opt_delimiter(self, delim):
        if delim not in (b'=', b' '):
            raise ValueError(b'invalid metavar delimiter for long options: %r' % delim)
        self._long_opt_fmt = b'%s' + delim + b'%s'
        return

    def indent(self):
        self.current_indent += self.indent_increment
        self.level += 1
        return

    def dedent(self):
        self.current_indent -= self.indent_increment
        self.level -= 1
        return

    def format_usage(self, usage):
        raise NotImplementedError, b'subclasses must implement'
        return

    def format_heading(self, heading):
        raise NotImplementedError, b'subclasses must implement'
        return

    def _format_text(self, text):
        text_width = max(self.width - self.current_indent, 11)
        indent = b' ' * self.current_indent
        return textwrap.fill(text, text_width, initial_indent=indent, subsequent_indent=indent)

    def format_description(self, description):
        if description:
            return self._format_text(description) + b'\n'
        else:
            return b''

        return

    def format_epilog(self, epilog):
        if epilog:
            return b'\n' + self._format_text(epilog) + b'\n'
        else:
            return b''

        return

    def expand_default(self, option):
        if self.parser is None or not self.default_tag:
            return option.help
        else:
            default_value = self.parser.defaults.get(option.dest)
            if default_value is NO_DEFAULT or default_value is None:
                default_value = self.NO_DEFAULT_VALUE
            return option.help.replace(self.default_tag, str(default_value))

    def format_option(self, option):
        result = []
        opts = self.option_strings[option]
        opt_width = self.help_position - self.current_indent - 2
        if len(opts) > opt_width:
            opts = b'%*s%s\n' % (self.current_indent, b'', opts)
            indent_first = self.help_position
        else:
            opts = b'%*s%-*s  ' % (self.current_indent, b'', opt_width, opts)
            indent_first = 0
        result.append(opts)
        if option.help:
            help_text = self.expand_default(option)
            help_lines = textwrap.wrap(help_text, self.help_width)
            result.append(b'%*s%s\n' % (indent_first, b'', help_lines[0]))
            result.extend([b'%*s%s\n' % (self.help_position, b'', line) for line in help_lines[1:]])
        elif opts[-1] != b'\n':
            result.append(b'\n')
        return (b'').join(result)

    def store_option_strings(self, parser):
        self.indent()
        max_len = 0
        for opt in parser.option_list:
            strings = self.format_option_strings(opt)
            self.option_strings[opt] = strings
            max_len = max(max_len, len(strings) + self.current_indent)

        self.indent()
        for group in parser.option_groups:
            for opt in group.option_list:
                strings = self.format_option_strings(opt)
                self.option_strings[opt] = strings
                max_len = max(max_len, len(strings) + self.current_indent)

        self.dedent()
        self.dedent()
        self.help_position = min(max_len + 2, self.max_help_position)
        self.help_width = max(self.width - self.help_position, 11)
        return

    def format_option_strings(self, option):
        if option.takes_value():
            metavar = option.metavar or option.dest.upper()
            short_opts = [self._short_opt_fmt % (sopt, metavar) for sopt in option._short_opts]
            long_opts = [self._long_opt_fmt % (lopt, metavar) for lopt in option._long_opts]
        else:
            short_opts = option._short_opts
            long_opts = option._long_opts
        if self.short_first:
            opts = short_opts + long_opts
        else:
            opts = long_opts + short_opts
        return (b', ').join(opts)


class IndentedHelpFormatter(HelpFormatter):

    def __init__(self, indent_increment=2, max_help_position=24, width=None, short_first=1):
        HelpFormatter.__init__(self, indent_increment, max_help_position, width, short_first)
        return

    def format_usage(self, usage):
        return _(b'Usage: %s\n') % usage

    def format_heading(self, heading):
        return b'%*s%s:\n' % (self.current_indent, b'', heading)


class TitledHelpFormatter(HelpFormatter):

    def __init__(self, indent_increment=0, max_help_position=24, width=None, short_first=0):
        HelpFormatter.__init__(self, indent_increment, max_help_position, width, short_first)
        return

    def format_usage(self, usage):
        return b'%s  %s\n' % (self.format_heading(_(b'Usage')), usage)

    def format_heading(self, heading):
        return b'%s\n%s\n' % (heading, b'=-'[self.level] * len(heading))


def _parse_num(val, type):
    if val[:2].lower() == b'0x':
        radix = 16
    elif val[:2].lower() == b'0b':
        radix = 2
        val = val[2:] or b'0'
    elif val[:1] == b'0':
        radix = 8
    else:
        radix = 10
    return type(val, radix)


def _parse_int(val):
    return _parse_num(val, int)


def _parse_long(val):
    return _parse_num(val, long)


_builtin_cvt = {b'int': (_parse_int, _(b'integer')), b'long': (
           _parse_long, _(b'long integer')), 
   b'float': (
            float, _(b'floating-point')), 
   b'complex': (
              complex, _(b'complex'))}

def check_builtin(option, opt, value):
    cvt, what = _builtin_cvt[option.type]
    try:
        return cvt(value)
    except ValueError:
        raise OptionValueError(_(b'option %s: invalid %s value: %r') % (opt, what, value))

    return


def check_choice(option, opt, value):
    if value in option.choices:
        return value
    choices = (b', ').join(map(repr, option.choices))
    raise OptionValueError(_(b'option %s: invalid choice: %r (choose from %s)') % (
     opt, value, choices))
    return


NO_DEFAULT = (
 b'NO', b'DEFAULT')

class Option():
    ATTRS = [
     0, 
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11]
    ACTIONS = (b'store', b'store_const', b'store_true', b'store_false', b'append', b'append_const', b'count', b'callback', b'help', b'version')
    STORE_ACTIONS = (b'store', b'store_const', b'store_true', b'store_false', b'append', b'append_const', b'count')
    TYPED_ACTIONS = (b'store', b'append', b'callback')
    ALWAYS_TYPED_ACTIONS = (b'store', b'append')
    CONST_ACTIONS = (b'store_const', b'append_const')
    TYPES = (b'string', b'int', b'long', b'float', b'complex', b'choice')
    TYPE_CHECKER = {b'int': check_builtin, b'long': check_builtin, 
       b'float': check_builtin, 
       b'complex': check_builtin, 
       b'choice': check_choice}
    CHECK_METHODS = None

    def __init__(self, *opts, **attrs):
        self._short_opts = []
        self._long_opts = []
        opts = self._check_opt_strings(opts)
        self._set_opt_strings(opts)
        self._set_attrs(attrs)
        for checker in self.CHECK_METHODS:
            checker(self)

        return

    def _check_opt_strings(self, opts):
        opts = filter(None, opts)
        if not opts:
            raise TypeError(b'at least one option string must be supplied')
        return opts

    def _set_opt_strings(self, opts):
        for opt in opts:
            if len(opt) < 2:
                raise OptionError(b'invalid option string %r: must be at least two characters long' % opt, self)
            elif len(opt) == 2:
                if not (opt[0] == b'-' and opt[1] != b'-'):
                    raise OptionError(b'invalid short option string %r: must be of the form -x, (x any non-dash char)' % opt, self)
                self._short_opts.append(opt)
            elif not (opt[0:2] == b'--' and opt[2] != b'-'):
                raise OptionError(b'invalid long option string %r: must start with --, followed by non-dash' % opt, self)
            self._long_opts.append(opt)

        return

    def _set_attrs(self, attrs):
        for attr in self.ATTRS:
            if attr in attrs:
                setattr(self, attr, attrs[attr])
                del attrs[attr]
            elif attr == b'default':
                setattr(self, attr, NO_DEFAULT)
            else:
                setattr(self, attr, None)

        if attrs:
            attrs = attrs.keys()
            attrs.sort()
            raise OptionError(b'invalid keyword arguments: %s' % (b', ').join(attrs), self)
        return

    def _check_action(self):
        if self.action is None:
            self.action = b'store'
        elif self.action not in self.ACTIONS:
            raise OptionError(b'invalid action: %r' % self.action, self)
        return

    def _check_type(self):
        if self.type is None:
            if self.action in self.ALWAYS_TYPED_ACTIONS:
                if self.choices is not None:
                    self.type = b'choice'
                else:
                    self.type = b'string'
        else:
            import __builtin__
            if type(self.type) is types.TypeType or hasattr(self.type, b'__name__') and getattr(__builtin__, self.type.__name__, None) is self.type:
                self.type = self.type.__name__
            if self.type == b'str':
                self.type = b'string'
            if self.type not in self.TYPES:
                raise OptionError(b'invalid option type: %r' % self.type, self)
            if self.action not in self.TYPED_ACTIONS:
                raise OptionError(b'must not supply a type for action %r' % self.action, self)
        return

    def _check_choice(self):
        if self.type == b'choice':
            if self.choices is None:
                raise OptionError(b"must supply a list of choices for type 'choice'", self)
            elif type(self.choices) not in (types.TupleType, types.ListType):
                raise OptionError(b"choices must be a list of strings ('%s' supplied)" % str(type(self.choices)).split(b"'")[1], self)
        elif self.choices is not None:
            raise OptionError(b'must not supply choices for type %r' % self.type, self)
        return

    def _check_dest(self):
        takes_value = self.action in self.STORE_ACTIONS or self.type is not None
        if self.dest is None and takes_value:
            if self._long_opts:
                self.dest = self._long_opts[0][2:].replace(b'-', b'_')
            else:
                self.dest = self._short_opts[0][1]
        return

    def _check_const(self):
        if self.action not in self.CONST_ACTIONS and self.const is not None:
            raise OptionError(b"'const' must not be supplied for action %r" % self.action, self)
        return

    def _check_nargs(self):
        if self.action in self.TYPED_ACTIONS:
            if self.nargs is None:
                self.nargs = 1
        elif self.nargs is not None:
            raise OptionError(b"'nargs' must not be supplied for action %r" % self.action, self)
        return

    def _check_callback(self):
        if self.action == b'callback':
            if not hasattr(self.callback, b'__call__'):
                raise OptionError(b'callback not callable: %r' % self.callback, self)
            if self.callback_args is not None and type(self.callback_args) is not types.TupleType:
                raise OptionError(b'callback_args, if supplied, must be a tuple: not %r' % self.callback_args, self)
            if self.callback_kwargs is not None and type(self.callback_kwargs) is not types.DictType:
                raise OptionError(b'callback_kwargs, if supplied, must be a dict: not %r' % self.callback_kwargs, self)
        elif self.callback is not None:
            raise OptionError(b'callback supplied (%r) for non-callback option' % self.callback, self)
        if self.callback_args is not None:
            raise OptionError(b'callback_args supplied for non-callback option', self)
        if self.callback_kwargs is not None:
            raise OptionError(b'callback_kwargs supplied for non-callback option', self)
        return

    CHECK_METHODS = [_check_action, 
     _check_type, 
     _check_choice, 
     _check_dest, 
     _check_const, 
     _check_nargs, 
     _check_callback]

    def __str__(self):
        return (b'/').join(self._short_opts + self._long_opts)

    __repr__ = _repr

    def takes_value(self):
        return self.type is not None

    def get_opt_string(self):
        if self._long_opts:
            return self._long_opts[0]
        else:
            return self._short_opts[0]

        return

    def check_value(self, opt, value):
        checker = self.TYPE_CHECKER.get(self.type)
        if checker is None:
            return value
        else:
            return checker(self, opt, value)
            return

    def convert_value(self, opt, value):
        if value is not None:
            if self.nargs == 1:
                return self.check_value(opt, value)
            else:
                return tuple([self.check_value(opt, v) for v in value])

        return

    def process(self, opt, value, values, parser):
        value = self.convert_value(opt, value)
        return self.take_action(self.action, self.dest, opt, value, values, parser)

    def take_action(self, action, dest, opt, value, values, parser):
        if action == b'store':
            setattr(values, dest, value)
        elif action == b'store_const':
            setattr(values, dest, self.const)
        elif action == b'store_true':
            setattr(values, dest, True)
        elif action == b'store_false':
            setattr(values, dest, False)
        elif action == b'append':
            values.ensure_value(dest, []).append(value)
        elif action == b'append_const':
            values.ensure_value(dest, []).append(self.const)
        elif action == b'count':
            setattr(values, dest, values.ensure_value(dest, 0) + 1)
        elif action == b'callback':
            args = self.callback_args or ()
            kwargs = self.callback_kwargs or {}
            self.callback(self, opt, value, parser, *args, **kwargs)
        elif action == b'help':
            parser.print_help()
            parser.exit()
        elif action == b'version':
            parser.print_version()
            parser.exit()
        else:
            raise ValueError(b'unknown action %r' % self.action)
        return 1


SUPPRESS_HELP = b'SUPPRESS' + b'HELP'
SUPPRESS_USAGE = b'SUPPRESS' + b'USAGE'
try:
    basestring
except NameError:

    def isbasestring(x):
        return isinstance(x, (types.StringType, types.UnicodeType))


else:

    def isbasestring(x):
        return isinstance(x, basestring)


class Values():

    def __init__(self, defaults=None):
        if defaults:
            for attr, val in defaults.items():
                setattr(self, attr, val)

        return

    def __str__(self):
        return str(self.__dict__)

    __repr__ = _repr

    def __cmp__(self, other):
        if isinstance(other, Values):
            return cmp(self.__dict__, other.__dict__)
        else:
            if isinstance(other, types.DictType):
                return cmp(self.__dict__, other)
            return -1

        return

    def _update_careful(self, dict):
        for attr in dir(self):
            if attr in dict:
                dval = dict[attr]
                if dval is not None:
                    setattr(self, attr, dval)

        return

    def _update_loose(self, dict):
        self.__dict__.update(dict)
        return

    def _update(self, dict, mode):
        if mode == b'careful':
            self._update_careful(dict)
        elif mode == b'loose':
            self._update_loose(dict)
        else:
            raise ValueError, b'invalid update mode: %r' % mode
        return

    def read_module(self, modname, mode=b'careful'):
        __import__(modname)
        mod = sys.modules[modname]
        self._update(vars(mod), mode)
        return

    def read_file(self, filename, mode=b'careful'):
        vars = {}
        execfile(filename, vars)
        self._update(vars, mode)
        return

    def ensure_value(self, attr, value):
        if not hasattr(self, attr) or getattr(self, attr) is None:
            setattr(self, attr, value)
        return getattr(self, attr)


class OptionContainer():

    def __init__(self, option_class, conflict_handler, description):
        self._create_option_list()
        self.option_class = option_class
        self.set_conflict_handler(conflict_handler)
        self.set_description(description)
        return

    def _create_option_mappings(self):
        self._short_opt = {}
        self._long_opt = {}
        self.defaults = {}
        return

    def _share_option_mappings(self, parser):
        self._short_opt = parser._short_opt
        self._long_opt = parser._long_opt
        self.defaults = parser.defaults
        return

    def set_conflict_handler(self, handler):
        if handler not in (b'error', b'resolve'):
            raise ValueError, b'invalid conflict_resolution value %r' % handler
        self.conflict_handler = handler
        return

    def set_description(self, description):
        self.description = description
        return

    def get_description(self):
        return self.description

    def destroy(self):
        del self._short_opt
        del self._long_opt
        del self.defaults
        return

    def _check_conflict(self, option):
        conflict_opts = []
        for opt in option._short_opts:
            if opt in self._short_opt:
                conflict_opts.append((opt, self._short_opt[opt]))

        for opt in option._long_opts:
            if opt in self._long_opt:
                conflict_opts.append((opt, self._long_opt[opt]))

        if conflict_opts:
            handler = self.conflict_handler
            if handler == b'error':
                raise OptionConflictError(b'conflicting option string(s): %s' % (b', ').join([co[0] for co in conflict_opts]), option)
            elif handler == b'resolve':
                for opt, c_option in conflict_opts:
                    if opt.startswith(b'--'):
                        c_option._long_opts.remove(opt)
                        del self._long_opt[opt]
                    else:
                        c_option._short_opts.remove(opt)
                        del self._short_opt[opt]
                    if not (c_option._short_opts or c_option._long_opts):
                        c_option.container.option_list.remove(c_option)

        return

    def add_option(self, *args, **kwargs):
        if type(args[0]) in types.StringTypes:
            option = self.option_class(*args, **kwargs)
        elif len(args) == 1 and not kwargs:
            option = args[0]
            if not isinstance(option, Option):
                raise TypeError, b'not an Option instance: %r' % option
        else:
            raise TypeError, b'invalid arguments'
        self._check_conflict(option)
        self.option_list.append(option)
        option.container = self
        for opt in option._short_opts:
            self._short_opt[opt] = option

        for opt in option._long_opts:
            self._long_opt[opt] = option

        if option.dest is not None:
            if option.default is not NO_DEFAULT:
                self.defaults[option.dest] = option.default
            elif option.dest not in self.defaults:
                self.defaults[option.dest] = None
        return option

    def add_options(self, option_list):
        for option in option_list:
            self.add_option(option)

        return

    def get_option(self, opt_str):
        return self._short_opt.get(opt_str) or self._long_opt.get(opt_str)

    def has_option(self, opt_str):
        return opt_str in self._short_opt or opt_str in self._long_opt

    def remove_option(self, opt_str):
        option = self._short_opt.get(opt_str)
        if option is None:
            option = self._long_opt.get(opt_str)
        if option is None:
            raise ValueError(b'no such option %r' % opt_str)
        for opt in option._short_opts:
            del self._short_opt[opt]

        for opt in option._long_opts:
            del self._long_opt[opt]

        option.container.option_list.remove(option)
        return

    def format_option_help(self, formatter):
        if not self.option_list:
            return b''
        result = []
        for option in self.option_list:
            if option.help is not SUPPRESS_HELP:
                result.append(formatter.format_option(option))

        return (b'').join(result)

    def format_description(self, formatter):
        return formatter.format_description(self.get_description())

    def format_help(self, formatter):
        result = []
        if self.description:
            result.append(self.format_description(formatter))
        if self.option_list:
            result.append(self.format_option_help(formatter))
        return (b'\n').join(result)


class OptionGroup(OptionContainer):

    def __init__(self, parser, title, description=None):
        self.parser = parser
        OptionContainer.__init__(self, parser.option_class, parser.conflict_handler, description)
        self.title = title
        return

    def _create_option_list(self):
        self.option_list = []
        self._share_option_mappings(self.parser)
        return

    def set_title(self, title):
        self.title = title
        return

    def destroy(self):
        OptionContainer.destroy(self)
        del self.option_list
        return

    def format_help(self, formatter):
        result = formatter.format_heading(self.title)
        formatter.indent()
        result += OptionContainer.format_help(self, formatter)
        formatter.dedent()
        return result


class OptionParser(OptionContainer):
    standard_option_list = []

    def __init__(self, usage=None, option_list=None, option_class=Option, version=None, conflict_handler=b'error', description=None, formatter=None, add_help_option=True, prog=None, epilog=None):
        OptionContainer.__init__(self, option_class, conflict_handler, description)
        self.set_usage(usage)
        self.prog = prog
        self.version = version
        self.allow_interspersed_args = True
        self.process_default_values = True
        if formatter is None:
            formatter = IndentedHelpFormatter()
        self.formatter = formatter
        self.formatter.set_parser(self)
        self.epilog = epilog
        self._populate_option_list(option_list, add_help=add_help_option)
        self._init_parsing_state()
        return

    def destroy(self):
        OptionContainer.destroy(self)
        for group in self.option_groups:
            group.destroy()

        del self.option_list
        del self.option_groups
        del self.formatter
        return

    def _create_option_list(self):
        self.option_list = []
        self.option_groups = []
        self._create_option_mappings()
        return

    def _add_help_option(self):
        self.add_option(b'-h', b'--help', action=b'help', help=_(b'show this help message and exit'))
        return

    def _add_version_option(self):
        self.add_option(b'--version', action=b'version', help=_(b"show program's version number and exit"))
        return

    def _populate_option_list(self, option_list, add_help=True):
        if self.standard_option_list:
            self.add_options(self.standard_option_list)
        if option_list:
            self.add_options(option_list)
        if self.version:
            self._add_version_option()
        if add_help:
            self._add_help_option()
        return

    def _init_parsing_state(self):
        self.rargs = None
        self.largs = None
        self.values = None
        return

    def set_usage(self, usage):
        if usage is None:
            self.usage = _(b'%prog [options]')
        elif usage is SUPPRESS_USAGE:
            self.usage = None
        elif usage.lower().startswith(b'usage: '):
            self.usage = usage[7:]
        else:
            self.usage = usage
        return

    def enable_interspersed_args(self):
        self.allow_interspersed_args = True
        return

    def disable_interspersed_args(self):
        self.allow_interspersed_args = False
        return

    def set_process_default_values(self, process):
        self.process_default_values = process
        return

    def set_default(self, dest, value):
        self.defaults[dest] = value
        return

    def set_defaults(self, **kwargs):
        self.defaults.update(kwargs)
        return

    def _get_all_options(self):
        options = self.option_list[:]
        for group in self.option_groups:
            options.extend(group.option_list)

        return options

    def get_default_values(self):
        if not self.process_default_values:
            return Values(self.defaults)
        defaults = self.defaults.copy()
        for option in self._get_all_options():
            default = defaults.get(option.dest)
            if isbasestring(default):
                opt_str = option.get_opt_string()
                defaults[option.dest] = option.check_value(opt_str, default)

        return Values(defaults)

    def add_option_group(self, *args, **kwargs):
        if type(args[0]) is types.StringType:
            group = OptionGroup(self, *args, **kwargs)
        elif len(args) == 1 and not kwargs:
            group = args[0]
            if not isinstance(group, OptionGroup):
                raise TypeError, b'not an OptionGroup instance: %r' % group
            if group.parser is not self:
                raise ValueError, b'invalid OptionGroup (wrong parser)'
        else:
            raise TypeError, b'invalid arguments'
        self.option_groups.append(group)
        return group

    def get_option_group(self, opt_str):
        option = self._short_opt.get(opt_str) or self._long_opt.get(opt_str)
        if option and option.container is not self:
            return option.container
        else:
            return

    def _get_args(self, args):
        if args is None:
            return sys.argv[1:]
        else:
            return args[:]
            return

    def parse_args(self, args=None, values=None):
        rargs = self._get_args(args)
        if values is None:
            values = self.get_default_values()
        self.rargs = rargs
        self.largs = largs = []
        self.values = values
        try:
            stop = self._process_args(largs, rargs, values)
        except (BadOptionError, OptionValueError) as err:
            self.error(str(err))

        args = largs + rargs
        return self.check_values(values, args)

    def check_values(self, values, args):
        return (
         values, args)

    def _process_args(self, largs, rargs, values):
        while rargs:
            arg = rargs[0]
            if arg == b'--':
                del rargs[0]
                return
            if arg[0:2] == b'--':
                self._process_long_opt(rargs, values)
            elif arg[:1] == b'-' and len(arg) > 1:
                self._process_short_opts(rargs, values)
            elif self.allow_interspersed_args:
                largs.append(arg)
                del rargs[0]
            else:
                return

        return

    def _match_long_opt(self, opt):
        return _match_abbrev(opt, self._long_opt)

    def _process_long_opt(self, rargs, values):
        arg = rargs.pop(0)
        if b'=' in arg:
            opt, next_arg = arg.split(b'=', 1)
            rargs.insert(0, next_arg)
            had_explicit_value = True
        else:
            opt = arg
            had_explicit_value = False
        opt = self._match_long_opt(opt)
        option = self._long_opt[opt]
        if option.takes_value():
            nargs = option.nargs
            if len(rargs) < nargs:
                if nargs == 1:
                    self.error(_(b'%s option requires an argument') % opt)
                else:
                    self.error(_(b'%s option requires %d arguments') % (
                     opt, nargs))
            elif nargs == 1:
                value = rargs.pop(0)
            else:
                value = tuple(rargs[0:nargs])
                del rargs[0:nargs]
        elif had_explicit_value:
            self.error(_(b'%s option does not take a value') % opt)
        else:
            value = None
        option.process(opt, value, values, self)
        return

    def _process_short_opts(self, rargs, values):
        arg = rargs.pop(0)
        stop = False
        i = 1
        for ch in arg[1:]:
            opt = b'-' + ch
            option = self._short_opt.get(opt)
            i += 1
            if not option:
                raise BadOptionError(opt)
            if option.takes_value():
                if i < len(arg):
                    rargs.insert(0, arg[i:])
                    stop = True
                nargs = option.nargs
                if len(rargs) < nargs:
                    if nargs == 1:
                        self.error(_(b'%s option requires an argument') % opt)
                    else:
                        self.error(_(b'%s option requires %d arguments') % (
                         opt, nargs))
                elif nargs == 1:
                    value = rargs.pop(0)
                else:
                    value = tuple(rargs[0:nargs])
                    del rargs[0:nargs]
            else:
                value = None
            option.process(opt, value, values, self)
            if stop:
                break

        return

    def get_prog_name(self):
        if self.prog is None:
            return os.path.basename(sys.argv[0])
        else:
            return self.prog
            return

    def expand_prog_name(self, s):
        return s.replace(b'%prog', self.get_prog_name())

    def get_description(self):
        return self.expand_prog_name(self.description)

    def exit(self, status=0, msg=None):
        if msg:
            sys.stderr.write(msg)
        sys.exit(status)
        return

    def error(self, msg):
        self.print_usage(sys.stderr)
        self.exit(2, b'%s: error: %s\n' % (self.get_prog_name(), msg))
        return

    def get_usage(self):
        if self.usage:
            return self.formatter.format_usage(self.expand_prog_name(self.usage))
        else:
            return b''

        return

    def print_usage(self, file=None):
        if self.usage:
            print >> file, self.get_usage()
        return

    def get_version(self):
        if self.version:
            return self.expand_prog_name(self.version)
        else:
            return b''

        return

    def print_version(self, file=None):
        if self.version:
            print >> file, self.get_version()
        return

    def format_option_help(self, formatter=None):
        if formatter is None:
            formatter = self.formatter
        formatter.store_option_strings(self)
        result = []
        result.append(formatter.format_heading(_(b'Options')))
        formatter.indent()
        if self.option_list:
            result.append(OptionContainer.format_option_help(self, formatter))
            result.append(b'\n')
        for group in self.option_groups:
            result.append(group.format_help(formatter))
            result.append(b'\n')

        formatter.dedent()
        return (b'').join(result[:-1])

    def format_epilog(self, formatter):
        return formatter.format_epilog(self.epilog)

    def format_help(self, formatter=None):
        if formatter is None:
            formatter = self.formatter
        result = []
        if self.usage:
            result.append(self.get_usage() + b'\n')
        if self.description:
            result.append(self.format_description(formatter) + b'\n')
        result.append(self.format_option_help(formatter))
        result.append(self.format_epilog(formatter))
        return (b'').join(result)

    def _get_encoding(self, file):
        encoding = getattr(file, b'encoding', None)
        if not encoding:
            encoding = sys.getdefaultencoding()
        return encoding

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout
        encoding = self._get_encoding(file)
        file.write(self.format_help().encode(encoding, b'replace'))
        return


def _match_abbrev(s, wordmap):
    if s in wordmap:
        return s
    possibilities = [word for word in wordmap.keys() if word.startswith(s)]
    if len(possibilities) == 1:
        return possibilities[0]
    if not possibilities:
        raise BadOptionError(s)
    else:
        possibilities.sort()
        raise AmbiguousOptionError(s, possibilities)
    return


make_option = Option
