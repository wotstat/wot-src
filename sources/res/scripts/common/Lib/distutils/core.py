__revision__ = b'$Id$'
import sys, os
from distutils.debug import DEBUG
from distutils.errors import DistutilsSetupError, DistutilsArgError, DistutilsError, CCompilerError
from distutils.dist import Distribution
from distutils.cmd import Command
from distutils.config import PyPIRCCommand
from distutils.extension import Extension
USAGE = b'usage: %(script)s [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]\n   or: %(script)s --help [cmd1 cmd2 ...]\n   or: %(script)s --help-commands\n   or: %(script)s cmd --help\n'

def gen_usage(script_name):
    script = os.path.basename(script_name)
    return USAGE % {b'script': script}


_setup_stop_after = None
_setup_distribution = None
setup_keywords = (b'distclass', b'script_name', b'script_args', b'options', b'name', b'version', b'author', b'author_email', b'maintainer', b'maintainer_email', b'url', b'license', b'description', b'long_description', b'keywords', b'platforms', b'classifiers', b'download_url', b'requires', b'provides', b'obsoletes')
extension_keywords = (b'name', b'sources', b'include_dirs', b'define_macros', b'undef_macros', b'library_dirs', b'libraries', b'runtime_library_dirs', b'extra_objects', b'extra_compile_args', b'extra_link_args', b'swig_opts', b'export_symbols', b'depends', b'language')

def setup(**attrs):
    global _setup_distribution
    global _setup_stop_after
    klass = attrs.get(b'distclass')
    if klass:
        del attrs[b'distclass']
    else:
        klass = Distribution
    if b'script_name' not in attrs:
        attrs[b'script_name'] = os.path.basename(sys.argv[0])
    if b'script_args' not in attrs:
        attrs[b'script_args'] = sys.argv[1:]
    try:
        _setup_distribution = dist = klass(attrs)
    except DistutilsSetupError as msg:
        if b'name' in attrs:
            raise SystemExit, b'error in %s setup command: %s' % (
             attrs[b'name'], msg)
        else:
            raise SystemExit, b'error in setup command: %s' % msg

    if _setup_stop_after == b'init':
        return dist
    dist.parse_config_files()
    if DEBUG:
        print b'options (after parsing config files):'
        dist.dump_option_dicts()
    if _setup_stop_after == b'config':
        return dist
    try:
        ok = dist.parse_command_line()
    except DistutilsArgError as msg:
        raise SystemExit, gen_usage(dist.script_name) + b'\nerror: %s' % msg

    if DEBUG:
        print b'options (after parsing command line):'
        dist.dump_option_dicts()
    if _setup_stop_after == b'commandline':
        return dist
    if ok:
        try:
            dist.run_commands()
        except KeyboardInterrupt:
            raise SystemExit, b'interrupted'
        except (IOError, os.error) as exc:
            if DEBUG:
                sys.stderr.write(b'error: %s\n' % (exc,))
                raise
            else:
                raise SystemExit, b'error: %s' % (exc,)
        except (DistutilsError, CCompilerError) as msg:
            if DEBUG:
                raise
            else:
                raise SystemExit, b'error: ' + str(msg)

    return dist


def run_setup(script_name, script_args=None, stop_after=b'run'):
    global _setup_stop_after
    if stop_after not in (b'init', b'config', b'commandline', b'run'):
        raise ValueError, b"invalid value for 'stop_after': %r" % (stop_after,)
    _setup_stop_after = stop_after
    save_argv = sys.argv
    g = {b'__file__': script_name}
    l = {}
    try:
        try:
            sys.argv[0] = script_name
            if script_args is not None:
                sys.argv[1:] = script_args
            f = open(script_name)
            try:
                exec f.read() in g, l
            finally:
                f.close()

        finally:
            sys.argv = save_argv
            _setup_stop_after = None

    except SystemExit:
        pass
    except:
        raise

    if _setup_distribution is None:
        raise RuntimeError, b"'distutils.core.setup()' was never called -- perhaps '%s' is not a Distutils setup script?" % script_name
    return _setup_distribution
