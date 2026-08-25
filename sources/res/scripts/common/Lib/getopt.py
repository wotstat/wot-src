__all__ = [
 b'GetoptError', b'error', b'getopt', b'gnu_getopt']
import os

class GetoptError(Exception):
    opt = b''
    msg = b''

    def __init__(self, msg, opt=b''):
        self.msg = msg
        self.opt = opt
        Exception.__init__(self, msg, opt)
        return

    def __str__(self):
        return self.msg


error = GetoptError

def getopt(args, shortopts, longopts=[]):
    opts = []
    if type(longopts) == type(b''):
        longopts = [
         longopts]
    else:
        longopts = list(longopts)
    while args and args[0].startswith(b'-') and args[0] != b'-':
        if args[0] == b'--':
            args = args[1:]
            break
        if args[0].startswith(b'--'):
            opts, args = do_longs(opts, args[0][2:], longopts, args[1:])
        else:
            opts, args = do_shorts(opts, args[0][1:], shortopts, args[1:])

    return (
     opts, args)


def gnu_getopt(args, shortopts, longopts=[]):
    opts = []
    prog_args = []
    if isinstance(longopts, str):
        longopts = [
         longopts]
    else:
        longopts = list(longopts)
    if shortopts.startswith(b'+'):
        shortopts = shortopts[1:]
        all_options_first = True
    elif os.environ.get(b'POSIXLY_CORRECT'):
        all_options_first = True
    else:
        all_options_first = False
    while args:
        if args[0] == b'--':
            prog_args += args[1:]
            break
        if args[0][:2] == b'--':
            opts, args = do_longs(opts, args[0][2:], longopts, args[1:])
        elif args[0][:1] == b'-' and args[0] != b'-':
            opts, args = do_shorts(opts, args[0][1:], shortopts, args[1:])
        elif all_options_first:
            prog_args += args
            break
        else:
            prog_args.append(args[0])
            args = args[1:]

    return (
     opts, prog_args)


def do_longs(opts, opt, longopts, args):
    try:
        i = opt.index(b'=')
    except ValueError:
        optarg = None
    else:
        opt, optarg = opt[:i], opt[i + 1:]

    has_arg, opt = long_has_args(opt, longopts)
    if has_arg:
        if optarg is None:
            if not args:
                raise GetoptError(b'option --%s requires argument' % opt, opt)
            optarg, args = args[0], args[1:]
    elif optarg is not None:
        raise GetoptError(b'option --%s must not have an argument' % opt, opt)
    opts.append((b'--' + opt, optarg or b''))
    return (opts, args)


def long_has_args(opt, longopts):
    possibilities = [o for o in longopts if o.startswith(opt)]
    if not possibilities:
        raise GetoptError(b'option --%s not recognized' % opt, opt)
    if opt in possibilities:
        return (False, opt)
    if opt + b'=' in possibilities:
        return (True, opt)
    if len(possibilities) > 1:
        raise GetoptError(b'option --%s not a unique prefix' % opt, opt)
    unique_match = possibilities[0]
    has_arg = unique_match.endswith(b'=')
    if has_arg:
        unique_match = unique_match[:-1]
    return (
     has_arg, unique_match)


def do_shorts(opts, optstring, shortopts, args):
    while optstring != b'':
        opt, optstring = optstring[0], optstring[1:]
        if short_has_arg(opt, shortopts):
            if optstring == b'':
                if not args:
                    raise GetoptError(b'option -%s requires argument' % opt, opt)
                optstring, args = args[0], args[1:]
            optarg, optstring = optstring, b''
        else:
            optarg = b''
        opts.append((b'-' + opt, optarg))

    return (
     opts, args)


def short_has_arg(opt, shortopts):
    for i in range(len(shortopts)):
        if opt == shortopts[i] != b':':
            return shortopts.startswith(b':', i + 1)

    raise GetoptError(b'option -%s not recognized' % opt, opt)
    return


if __name__ == b'__main__':
    import sys
    print getopt(sys.argv[1:], b'a:b', [b'alpha=', b'beta'])
