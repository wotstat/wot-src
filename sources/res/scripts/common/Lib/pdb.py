import sys, linecache, cmd, bdb
from repr import Repr
import os, re, pprint, traceback

class Restart(Exception):
    pass


_repr = Repr()
_repr.maxstring = 200
_saferepr = _repr.repr
__all__ = [
 6, 7, 8, 9, 10, 11, 12, 
 13, 14]

def find_function(funcname, filename):
    cre = re.compile(b'def\\s+%s\\s*[(]' % re.escape(funcname))
    try:
        fp = open(filename)
    except IOError:
        return

    lineno = 1
    answer = None
    while 1:
        line = fp.readline()
        if line == b'':
            break
        if cre.match(line):
            answer = (
             funcname, filename, lineno)
            break
        lineno = lineno + 1

    fp.close()
    return answer


line_prefix = b'\n-> '

class Pdb(bdb.Bdb, cmd.Cmd):

    def __init__(self, completekey=b'tab', stdin=None, stdout=None, skip=None):
        bdb.Bdb.__init__(self, skip=skip)
        cmd.Cmd.__init__(self, completekey, stdin, stdout)
        if stdout:
            self.use_rawinput = 0
        self.prompt = b'(Pdb) '
        self.aliases = {}
        self.mainpyfile = b''
        self._wait_for_mainpyfile = 0
        try:
            import readline
        except ImportError:
            pass

        self.rcLines = []
        if b'HOME' in os.environ:
            envHome = os.environ[b'HOME']
            try:
                rcFile = open(os.path.join(envHome, b'.pdbrc'))
            except IOError:
                pass
            else:
                for line in rcFile.readlines():
                    self.rcLines.append(line)

                rcFile.close()

        try:
            rcFile = open(b'.pdbrc')
        except IOError:
            pass
        else:
            for line in rcFile.readlines():
                self.rcLines.append(line)

            rcFile.close()

        self.commands = {}
        self.commands_doprompt = {}
        self.commands_silent = {}
        self.commands_defining = False
        self.commands_bnum = None
        return

    def reset(self):
        bdb.Bdb.reset(self)
        self.forget()
        return

    def forget(self):
        self.lineno = None
        self.stack = []
        self.curindex = 0
        self.curframe = None
        return

    def setup(self, f, t):
        self.forget()
        self.stack, self.curindex = self.get_stack(f, t)
        self.curframe = self.stack[self.curindex][0]
        self.curframe_locals = self.curframe.f_locals
        self.execRcLines()
        return

    def execRcLines(self):
        if self.rcLines:
            rcLines = self.rcLines
            self.rcLines = []
            for line in rcLines:
                line = line[:-1]
                if len(line) > 0 and line[0] != b'#':
                    self.onecmd(line)

        return

    def user_call(self, frame, argument_list):
        if self._wait_for_mainpyfile:
            return
        else:
            if self.stop_here(frame):
                print >> self.stdout, b'--Call--'
                self.interaction(frame, None)
            return

    def user_line(self, frame):
        if self._wait_for_mainpyfile:
            if self.mainpyfile != self.canonic(frame.f_code.co_filename) or frame.f_lineno <= 0:
                return
            self._wait_for_mainpyfile = 0
        if self.bp_commands(frame):
            self.interaction(frame, None)
        return

    def bp_commands(self, frame):
        if getattr(self, b'currentbp', False) and self.currentbp in self.commands:
            currentbp = self.currentbp
            self.currentbp = 0
            lastcmd_back = self.lastcmd
            self.setup(frame, None)
            for line in self.commands[currentbp]:
                self.onecmd(line)

            self.lastcmd = lastcmd_back
            if not self.commands_silent[currentbp]:
                self.print_stack_entry(self.stack[self.curindex])
            if self.commands_doprompt[currentbp]:
                self.cmdloop()
            self.forget()
            return
        else:
            return 1

    def user_return(self, frame, return_value):
        if self._wait_for_mainpyfile:
            return
        else:
            frame.f_locals[b'__return__'] = return_value
            print >> self.stdout, b'--Return--'
            self.interaction(frame, None)
            return

    def user_exception(self, frame, exc_info):
        if self._wait_for_mainpyfile:
            return
        exc_type, exc_value, exc_traceback = exc_info
        frame.f_locals[b'__exception__'] = (exc_type, exc_value)
        if type(exc_type) == type(b''):
            exc_type_name = exc_type
        else:
            exc_type_name = exc_type.__name__
        print >> self.stdout, exc_type_name + b':', _saferepr(exc_value)
        self.interaction(frame, exc_traceback)
        return

    def interaction(self, frame, traceback):
        self.setup(frame, traceback)
        self.print_stack_entry(self.stack[self.curindex])
        self.cmdloop()
        self.forget()
        return

    def displayhook(self, obj):
        if obj is not None:
            print repr(obj)
        return

    def default(self, line):
        if line[:1] == b'!':
            line = line[1:]
        locals = self.curframe_locals
        globals = self.curframe.f_globals
        try:
            code = compile(line + b'\n', b'<stdin>', b'single')
            save_stdout = sys.stdout
            save_stdin = sys.stdin
            save_displayhook = sys.displayhook
            try:
                sys.stdin = self.stdin
                sys.stdout = self.stdout
                sys.displayhook = self.displayhook
                exec code in globals, locals
            finally:
                sys.stdout = save_stdout
                sys.stdin = save_stdin
                sys.displayhook = save_displayhook

        except:
            t, v = sys.exc_info()[:2]
            if type(t) == type(b''):
                exc_type_name = t
            else:
                exc_type_name = t.__name__
            print >> self.stdout, b'***', exc_type_name + b':', v

        return

    def precmd(self, line):
        if not line.strip():
            return line
        args = line.split()
        while args[0] in self.aliases:
            line = self.aliases[args[0]]
            ii = 1
            for tmpArg in args[1:]:
                line = line.replace(b'%' + str(ii), tmpArg)
                ii = ii + 1

            line = line.replace(b'%*', (b' ').join(args[1:]))
            args = line.split()

        if args[0] != b'alias':
            marker = line.find(b';;')
            if marker >= 0:
                next = line[marker + 2:].lstrip()
                self.cmdqueue.append(next)
                line = line[:marker].rstrip()
        return line

    def onecmd(self, line):
        if not self.commands_defining:
            return cmd.Cmd.onecmd(self, line)
        else:
            return self.handle_command_def(line)

        return

    def handle_command_def(self, line):
        cmd, arg, line = self.parseline(line)
        if not cmd:
            return
        if cmd == b'silent':
            self.commands_silent[self.commands_bnum] = True
            return
        if cmd == b'end':
            self.cmdqueue = []
            return 1
        cmdlist = self.commands[self.commands_bnum]
        if arg:
            cmdlist.append(cmd + b' ' + arg)
        else:
            cmdlist.append(cmd)
        try:
            func = getattr(self, b'do_' + cmd)
        except AttributeError:
            func = self.default

        if func.func_name in self.commands_resuming:
            self.commands_doprompt[self.commands_bnum] = False
            self.cmdqueue = []
            return 1
        return

    do_h = cmd.Cmd.do_help

    def do_commands(self, arg):
        if not arg:
            bnum = len(bdb.Breakpoint.bpbynumber) - 1
        else:
            try:
                bnum = int(arg)
            except:
                print >> self.stdout, b'Usage : commands [bnum]\n        ...\n        end'
                return

        self.commands_bnum = bnum
        self.commands[bnum] = []
        self.commands_doprompt[bnum] = True
        self.commands_silent[bnum] = False
        prompt_back = self.prompt
        self.prompt = b'(com) '
        self.commands_defining = True
        try:
            self.cmdloop()
        finally:
            self.commands_defining = False
            self.prompt = prompt_back

        return

    def do_break(self, arg, temporary=0):
        if not arg:
            if self.breaks:
                print >> self.stdout, b'Num Type         Disp Enb   Where'
                for bp in bdb.Breakpoint.bpbynumber:
                    if bp:
                        bp.bpprint(self.stdout)

            return
        filename = None
        lineno = None
        cond = None
        comma = arg.find(b',')
        if comma > 0:
            cond = arg[comma + 1:].lstrip()
            arg = arg[:comma].rstrip()
        colon = arg.rfind(b':')
        funcname = None
        if colon >= 0:
            filename = arg[:colon].rstrip()
            f = self.lookupmodule(filename)
            if not f:
                print >> self.stdout, b'*** ', repr(filename),
                print >> self.stdout, b'not found from sys.path'
                return
            filename = f
            arg = arg[colon + 1:].lstrip()
            try:
                lineno = int(arg)
            except ValueError as msg:
                print >> self.stdout, b'*** Bad lineno:', arg
                return

        else:
            try:
                lineno = int(arg)
            except ValueError:
                try:
                    func = eval(arg, self.curframe.f_globals, self.curframe_locals)
                except:
                    func = arg

                try:
                    if hasattr(func, b'im_func'):
                        func = func.im_func
                    code = func.func_code
                    funcname = code.co_name
                    lineno = code.co_firstlineno
                    filename = code.co_filename
                except:
                    ok, filename, ln = self.lineinfo(arg)
                    if not ok:
                        print >> self.stdout, b'*** The specified object',
                        print >> self.stdout, repr(arg),
                        print >> self.stdout, b'is not a function'
                        print >> self.stdout, b'or was not found along sys.path.'
                        return
                    funcname = ok
                    lineno = int(ln)

        if not filename:
            filename = self.defaultFile()
        line = self.checkline(filename, lineno)
        if line:
            err = self.set_break(filename, line, temporary, cond, funcname)
            if err:
                print >> self.stdout, b'***', err
            else:
                bp = self.get_breaks(filename, line)[-1]
                print >> self.stdout, b'Breakpoint %d at %s:%d' % (bp.number,
                 bp.file,
                 bp.line)
        return

    def defaultFile(self):
        filename = self.curframe.f_code.co_filename
        if filename == b'<string>' and self.mainpyfile:
            filename = self.mainpyfile
        return filename

    do_b = do_break

    def do_tbreak(self, arg):
        self.do_break(arg, 1)
        return

    def lineinfo(self, identifier):
        failed = (None, None, None)
        idstring = identifier.split(b"'")
        if len(idstring) == 1:
            id = idstring[0].strip()
        elif len(idstring) == 3:
            id = idstring[1].strip()
        else:
            return failed
        if id == b'':
            return failed
        else:
            parts = id.split(b'.')
            if parts[0] == b'self':
                del parts[0]
                if len(parts) == 0:
                    return failed
            fname = self.defaultFile()
            if len(parts) == 1:
                item = parts[0]
            else:
                f = self.lookupmodule(parts[0])
                if f:
                    fname = f
                item = parts[1]
            answer = find_function(item, fname)
            return answer or failed

    def checkline(self, filename, lineno):
        globs = self.curframe.f_globals if hasattr(self, b'curframe') else None
        line = linecache.getline(filename, lineno, globs)
        if not line:
            print >> self.stdout, b'End of file'
            return 0
        else:
            line = line.strip()
            if not line or line[0] == b'#' or line[:3] == b'"""' or line[:3] == b"'''":
                print >> self.stdout, b'*** Blank or comment'
                return 0
            return lineno

    def do_enable(self, arg):
        args = arg.split()
        for i in args:
            try:
                i = int(i)
            except ValueError:
                print >> self.stdout, b'Breakpoint index %r is not a number' % i
                continue

            if not 0 <= i < len(bdb.Breakpoint.bpbynumber):
                print >> self.stdout, b'No breakpoint numbered', i
                continue
            bp = bdb.Breakpoint.bpbynumber[i]
            if bp:
                bp.enable()

        return

    def do_disable(self, arg):
        args = arg.split()
        for i in args:
            try:
                i = int(i)
            except ValueError:
                print >> self.stdout, b'Breakpoint index %r is not a number' % i
                continue

            if not 0 <= i < len(bdb.Breakpoint.bpbynumber):
                print >> self.stdout, b'No breakpoint numbered', i
                continue
            bp = bdb.Breakpoint.bpbynumber[i]
            if bp:
                bp.disable()

        return

    def do_condition(self, arg):
        args = arg.split(b' ', 1)
        try:
            bpnum = int(args[0].strip())
        except ValueError:
            print >> self.stdout, b'Breakpoint index %r is not a number' % args[0]
            return

        try:
            cond = args[1]
        except:
            cond = None

        try:
            bp = bdb.Breakpoint.bpbynumber[bpnum]
        except IndexError:
            print >> self.stdout, b'Breakpoint index %r is not valid' % args[0]
            return

        if bp:
            bp.cond = cond
            if not cond:
                print >> self.stdout, b'Breakpoint', bpnum,
                print >> self.stdout, b'is now unconditional.'
        return

    def do_ignore(self, arg):
        args = arg.split()
        try:
            bpnum = int(args[0].strip())
        except ValueError:
            print >> self.stdout, b'Breakpoint index %r is not a number' % args[0]
            return

        try:
            count = int(args[1].strip())
        except:
            count = 0

        try:
            bp = bdb.Breakpoint.bpbynumber[bpnum]
        except IndexError:
            print >> self.stdout, b'Breakpoint index %r is not valid' % args[0]
            return

        if bp:
            bp.ignore = count
            if count > 0:
                reply = b'Will ignore next '
                if count > 1:
                    reply = reply + b'%d crossings' % count
                else:
                    reply = reply + b'1 crossing'
                print >> self.stdout, reply + b' of breakpoint %d.' % bpnum
            else:
                print >> self.stdout, b'Will stop next time breakpoint',
                print >> self.stdout, bpnum, b'is reached.'
        return

    def do_clear(self, arg):
        if not arg:
            try:
                reply = raw_input(b'Clear all breaks? ')
            except EOFError:
                reply = b'no'

            reply = reply.strip().lower()
            if reply in (b'y', b'yes'):
                self.clear_all_breaks()
            return
        if b':' in arg:
            i = arg.rfind(b':')
            filename = arg[:i]
            arg = arg[i + 1:]
            try:
                lineno = int(arg)
            except ValueError:
                err = b'Invalid line number (%s)' % arg
            else:
                err = self.clear_break(filename, lineno)

            if err:
                print >> self.stdout, b'***', err
            return
        numberlist = arg.split()
        for i in numberlist:
            try:
                i = int(i)
            except ValueError:
                print >> self.stdout, b'Breakpoint index %r is not a number' % i
                continue

            if not 0 <= i < len(bdb.Breakpoint.bpbynumber):
                print >> self.stdout, b'No breakpoint numbered', i
                continue
            err = self.clear_bpbynumber(i)
            if err:
                print >> self.stdout, b'***', err
            else:
                print >> self.stdout, b'Deleted breakpoint', i

        return

    do_cl = do_clear

    def do_where(self, arg):
        self.print_stack_trace()
        return

    do_w = do_where
    do_bt = do_where

    def do_up(self, arg):
        if self.curindex == 0:
            print >> self.stdout, b'*** Oldest frame'
        else:
            self.curindex = self.curindex - 1
            self.curframe = self.stack[self.curindex][0]
            self.curframe_locals = self.curframe.f_locals
            self.print_stack_entry(self.stack[self.curindex])
            self.lineno = None
        return

    do_u = do_up

    def do_down(self, arg):
        if self.curindex + 1 == len(self.stack):
            print >> self.stdout, b'*** Newest frame'
        else:
            self.curindex = self.curindex + 1
            self.curframe = self.stack[self.curindex][0]
            self.curframe_locals = self.curframe.f_locals
            self.print_stack_entry(self.stack[self.curindex])
            self.lineno = None
        return

    do_d = do_down

    def do_until(self, arg):
        self.set_until(self.curframe)
        return 1

    do_unt = do_until

    def do_step(self, arg):
        self.set_step()
        return 1

    do_s = do_step

    def do_next(self, arg):
        self.set_next(self.curframe)
        return 1

    do_n = do_next

    def do_run(self, arg):
        if arg:
            import shlex
            argv0 = sys.argv[0:1]
            sys.argv = shlex.split(arg)
            sys.argv[:0] = argv0
        raise Restart
        return

    do_restart = do_run

    def do_return(self, arg):
        self.set_return(self.curframe)
        return 1

    do_r = do_return

    def do_continue(self, arg):
        self.set_continue()
        return 1

    do_c = do_cont = do_continue

    def do_jump(self, arg):
        if self.curindex + 1 != len(self.stack):
            print >> self.stdout, b'*** You can only jump within the bottom frame'
            return
        try:
            arg = int(arg)
        except ValueError:
            print >> self.stdout, b"*** The 'jump' command requires a line number."
        else:
            try:
                self.curframe.f_lineno = arg
                self.stack[self.curindex] = (self.stack[self.curindex][0], arg)
                self.print_stack_entry(self.stack[self.curindex])
            except ValueError as e:
                print >> self.stdout, b'*** Jump failed:', e

        return

    do_j = do_jump

    def do_debug(self, arg):
        sys.settrace(None)
        globals = self.curframe.f_globals
        locals = self.curframe_locals
        p = Pdb(self.completekey, self.stdin, self.stdout)
        p.prompt = b'(%s) ' % self.prompt.strip()
        print >> self.stdout, b'ENTERING RECURSIVE DEBUGGER'
        sys.call_tracing(p.run, (arg, globals, locals))
        print >> self.stdout, b'LEAVING RECURSIVE DEBUGGER'
        sys.settrace(self.trace_dispatch)
        self.lastcmd = p.lastcmd
        return

    def do_quit(self, arg):
        self._user_requested_quit = 1
        self.set_quit()
        return 1

    do_q = do_quit
    do_exit = do_quit

    def do_EOF(self, arg):
        print >> self.stdout
        self._user_requested_quit = 1
        self.set_quit()
        return 1

    def do_args(self, arg):
        co = self.curframe.f_code
        dict = self.curframe_locals
        n = co.co_argcount
        if co.co_flags & 4:
            n = n + 1
        if co.co_flags & 8:
            n = n + 1
        for i in range(n):
            name = co.co_varnames[i]
            print >> self.stdout, name, b'=',
            if name in dict:
                print >> self.stdout, dict[name]
            else:
                print >> self.stdout, b'*** undefined ***'

        return

    do_a = do_args

    def do_retval(self, arg):
        if b'__return__' in self.curframe_locals:
            print >> self.stdout, self.curframe_locals[b'__return__']
        else:
            print >> self.stdout, b'*** Not yet returned!'
        return

    do_rv = do_retval

    def _getval(self, arg):
        try:
            return eval(arg, self.curframe.f_globals, self.curframe_locals)
        except:
            t, v = sys.exc_info()[:2]
            if isinstance(t, str):
                exc_type_name = t
            else:
                exc_type_name = t.__name__
            print >> self.stdout, b'***', exc_type_name + b':', repr(v)
            raise

        return

    def do_p(self, arg):
        try:
            print >> self.stdout, repr(self._getval(arg))
        except:
            pass

        return

    def do_pp(self, arg):
        try:
            pprint.pprint(self._getval(arg), self.stdout)
        except:
            pass

        return

    def do_list(self, arg):
        self.lastcmd = b'list'
        last = None
        if arg:
            try:
                x = eval(arg, {}, {})
                if type(x) == type(()):
                    first, last = x
                    first = int(first)
                    last = int(last)
                    if last < first:
                        last = first + last
                else:
                    first = max(1, int(x) - 5)
            except:
                print >> self.stdout, b'*** Error in argument:', repr(arg)
                return

        elif self.lineno is None:
            first = max(1, self.curframe.f_lineno - 5)
        else:
            first = self.lineno + 1
        if last is None:
            last = first + 10
        filename = self.curframe.f_code.co_filename
        breaklist = self.get_file_breaks(filename)
        try:
            for lineno in range(first, last + 1):
                line = linecache.getline(filename, lineno, self.curframe.f_globals)
                if not line:
                    print >> self.stdout, b'[EOF]'
                    break
                else:
                    s = repr(lineno).rjust(3)
                    if len(s) < 4:
                        s = s + b' '
                    if lineno in breaklist:
                        s = s + b'B'
                    else:
                        s = s + b' '
                    if lineno == self.curframe.f_lineno:
                        s = s + b'->'
                    print >> self.stdout, s + b'\t' + line,
                    self.lineno = lineno

        except KeyboardInterrupt:
            pass

        return

    do_l = do_list

    def do_whatis(self, arg):
        try:
            value = eval(arg, self.curframe.f_globals, self.curframe_locals)
        except:
            t, v = sys.exc_info()[:2]
            if type(t) == type(b''):
                exc_type_name = t
            else:
                exc_type_name = t.__name__
            print >> self.stdout, b'***', exc_type_name + b':', repr(v)
            return

        code = None
        try:
            code = value.func_code
        except:
            pass

        if code:
            print >> self.stdout, b'Function', code.co_name
            return
        else:
            try:
                code = value.im_func.func_code
            except:
                pass

            if code:
                print >> self.stdout, b'Method', code.co_name
                return
            print >> self.stdout, type(value)
            return

    def do_alias(self, arg):
        args = arg.split()
        if len(args) == 0:
            keys = self.aliases.keys()
            keys.sort()
            for alias in keys:
                print >> self.stdout, b'%s = %s' % (alias, self.aliases[alias])

            return
        if args[0] in self.aliases and len(args) == 1:
            print >> self.stdout, b'%s = %s' % (args[0], self.aliases[args[0]])
        else:
            self.aliases[args[0]] = (b' ').join(args[1:])
        return

    def do_unalias(self, arg):
        args = arg.split()
        if len(args) == 0:
            return
        if args[0] in self.aliases:
            del self.aliases[args[0]]
        return

    commands_resuming = [51, 52, 53, 54, 
     55, 56]

    def print_stack_trace(self):
        try:
            for frame_lineno in self.stack:
                self.print_stack_entry(frame_lineno)

        except KeyboardInterrupt:
            pass

        return

    def print_stack_entry(self, frame_lineno, prompt_prefix=line_prefix):
        frame, lineno = frame_lineno
        if frame is self.curframe:
            print >> self.stdout, b'>',
        else:
            print >> self.stdout, b' ',
        print >> self.stdout, self.format_stack_entry(frame_lineno, prompt_prefix)
        return

    def help_help(self):
        self.help_h()
        return

    def help_h(self):
        print >> self.stdout, b'h(elp)\nWithout argument, print the list of available commands.\nWith a command name as argument, print help about that command\n"help pdb" pipes the full documentation file to the $PAGER\n"help exec" gives help on the ! command'
        return

    def help_where(self):
        self.help_w()
        return

    def help_w(self):
        print >> self.stdout, b'w(here)\nPrint a stack trace, with the most recent frame at the bottom.\nAn arrow indicates the "current frame", which determines the\ncontext of most commands.  \'bt\' is an alias for this command.'
        return

    help_bt = help_w

    def help_down(self):
        self.help_d()
        return

    def help_d(self):
        print >> self.stdout, b'd(own)\nMove the current frame one level down in the stack trace\n(to a newer frame).'
        return

    def help_up(self):
        self.help_u()
        return

    def help_u(self):
        print >> self.stdout, b'u(p)\nMove the current frame one level up in the stack trace\n(to an older frame).'
        return

    def help_break(self):
        self.help_b()
        return

    def help_b(self):
        print >> self.stdout, b"b(reak) ([file:]lineno | function) [, condition]\nWith a line number argument, set a break there in the current\nfile.  With a function name, set a break at first executable line\nof that function.  Without argument, list all breaks.  If a second\nargument is present, it is a string specifying an expression\nwhich must evaluate to true before the breakpoint is honored.\n\nThe line number may be prefixed with a filename and a colon,\nto specify a breakpoint in another file (probably one that\nhasn't been loaded yet).  The file is searched for on sys.path;\nthe .py suffix may be omitted."
        return

    def help_clear(self):
        self.help_cl()
        return

    def help_cl(self):
        print >> self.stdout, b'cl(ear) filename:lineno'
        print >> self.stdout, b'cl(ear) [bpnumber [bpnumber...]]\nWith a space separated list of breakpoint numbers, clear\nthose breakpoints.  Without argument, clear all breaks (but\nfirst ask confirmation).  With a filename:lineno argument,\nclear all breaks at that line in that file.\n\nNote that the argument is different from previous versions of\nthe debugger (in python distributions 1.5.1 and before) where\na linenumber was used instead of either filename:lineno or\nbreakpoint numbers.'
        return

    def help_tbreak(self):
        print >> self.stdout, b'tbreak  same arguments as break, but breakpoint\nis removed when first hit.'
        return

    def help_enable(self):
        print >> self.stdout, b'enable bpnumber [bpnumber ...]\nEnables the breakpoints given as a space separated list of\nbp numbers.'
        return

    def help_disable(self):
        print >> self.stdout, b'disable bpnumber [bpnumber ...]\nDisables the breakpoints given as a space separated list of\nbp numbers.'
        return

    def help_ignore(self):
        print >> self.stdout, b'ignore bpnumber count\nSets the ignore count for the given breakpoint number.  A breakpoint\nbecomes active when the ignore count is zero.  When non-zero, the\ncount is decremented each time the breakpoint is reached and the\nbreakpoint is not disabled and any associated condition evaluates\nto true.'
        return

    def help_condition(self):
        print >> self.stdout, b'condition bpnumber str_condition\nstr_condition is a string specifying an expression which\nmust evaluate to true before the breakpoint is honored.\nIf str_condition is absent, any existing condition is removed;\ni.e., the breakpoint is made unconditional.'
        return

    def help_step(self):
        self.help_s()
        return

    def help_s(self):
        print >> self.stdout, b's(tep)\nExecute the current line, stop at the first possible occasion\n(either in a function that is called or in the current function).'
        return

    def help_until(self):
        self.help_unt()
        return

    def help_unt(self):
        print b'unt(il)\nContinue execution until the line with a number greater than the current\none is reached or until the current frame returns'
        return

    def help_next(self):
        self.help_n()
        return

    def help_n(self):
        print >> self.stdout, b'n(ext)\nContinue execution until the next line in the current function\nis reached or it returns.'
        return

    def help_return(self):
        self.help_r()
        return

    def help_r(self):
        print >> self.stdout, b'r(eturn)\nContinue execution until the current function returns.'
        return

    def help_continue(self):
        self.help_c()
        return

    def help_cont(self):
        self.help_c()
        return

    def help_c(self):
        print >> self.stdout, b'c(ont(inue))\nContinue execution, only stop when a breakpoint is encountered.'
        return

    def help_jump(self):
        self.help_j()
        return

    def help_j(self):
        print >> self.stdout, b'j(ump) lineno\nSet the next line that will be executed.'
        return

    def help_debug(self):
        print >> self.stdout, b'debug code\nEnter a recursive debugger that steps through the code argument\n(which is an arbitrary expression or statement to be executed\nin the current environment).'
        return

    def help_list(self):
        self.help_l()
        return

    def help_l(self):
        print >> self.stdout, b'l(ist) [first [,last]]\nList source code for the current file.\nWithout arguments, list 11 lines around the current line\nor continue the previous listing.\nWith one argument, list 11 lines starting at that line.\nWith two arguments, list the given range;\nif the second argument is less than the first, it is a count.'
        return

    def help_args(self):
        self.help_a()
        return

    def help_a(self):
        print >> self.stdout, b'a(rgs)\nPrint the arguments of the current function.'
        return

    def help_p(self):
        print >> self.stdout, b'p expression\nPrint the value of the expression.'
        return

    def help_pp(self):
        print >> self.stdout, b'pp expression\nPretty-print the value of the expression.'
        return

    def help_exec(self):
        print >> self.stdout, b"(!) statement\nExecute the (one-line) statement in the context of\nthe current stack frame.\nThe exclamation point can be omitted unless the first word\nof the statement resembles a debugger command.\nTo assign to a global variable you must always prefix the\ncommand with a 'global' command, e.g.:\n(Pdb) global list_options; list_options = ['-l']\n(Pdb)"
        return

    def help_run(self):
        print b'run [args...]\nRestart the debugged python program. If a string is supplied, it is\nsplit with "shlex" and the result is used as the new sys.argv.\nHistory, breakpoints, actions and debugger options are preserved.\n"restart" is an alias for "run".'
        return

    help_restart = help_run

    def help_quit(self):
        self.help_q()
        return

    def help_q(self):
        print >> self.stdout, b'q(uit) or exit - Quit from the debugger.\nThe program being executed is aborted.'
        return

    help_exit = help_q

    def help_whatis(self):
        print >> self.stdout, b'whatis arg\nPrints the type of the argument.'
        return

    def help_EOF(self):
        print >> self.stdout, b'EOF\nHandles the receipt of EOF as a command.'
        return

    def help_alias(self):
        print >> self.stdout, b'alias [name [command [parameter parameter ...]]]\nCreates an alias called \'name\' the executes \'command\'.  The command\nmust *not* be enclosed in quotes.  Replaceable parameters are\nindicated by %1, %2, and so on, while %* is replaced by all the\nparameters.  If no command is given, the current alias for name\nis shown. If no name is given, all aliases are listed.\n\nAliases may be nested and can contain anything that can be\nlegally typed at the pdb prompt.  Note!  You *can* override\ninternal pdb commands with aliases!  Those internal commands\nare then hidden until the alias is removed.  Aliasing is recursively\napplied to the first word of the command line; all other words\nin the line are left alone.\n\nSome useful aliases (especially when placed in the .pdbrc file) are:\n\n#Print instance variables (usage "pi classInst")\nalias pi for k in %1.__dict__.keys(): print "%1.",k,"=",%1.__dict__[k]\n\n#Print instance variables in self\nalias ps pi self\n'
        return

    def help_unalias(self):
        print >> self.stdout, b'unalias name\nDeletes the specified alias.'
        return

    def help_commands(self):
        print >> self.stdout, b"commands [bpnumber]\n(com) ...\n(com) end\n(Pdb)\n\nSpecify a list of commands for breakpoint number bpnumber.  The\ncommands themselves appear on the following lines.  Type a line\ncontaining just 'end' to terminate the commands.\n\nTo remove all commands from a breakpoint, type commands and\nfollow it immediately with  end; that is, give no commands.\n\nWith no bpnumber argument, commands refers to the last\nbreakpoint set.\n\nYou can use breakpoint commands to start your program up again.\nSimply use the continue command, or step, or any other\ncommand that resumes execution.\n\nSpecifying any command resuming execution (currently continue,\nstep, next, return, jump, quit and their abbreviations) terminates\nthe command list (as if that command was immediately followed by end).\nThis is because any time you resume execution\n(even with a simple next or step), you may encounter\nanother breakpoint--which could have its own command list, leading to\nambiguities about which list to execute.\n\n   If you use the 'silent' command in the command list, the\nusual message about stopping at a breakpoint is not printed.  This may\nbe desirable for breakpoints that are to print a specific message and\nthen continue.  If none of the other commands print anything, you\nsee no sign that the breakpoint was reached.\n"
        return

    def help_pdb(self):
        help()
        return

    def lookupmodule(self, filename):
        if os.path.isabs(filename) and os.path.exists(filename):
            return filename
        else:
            f = os.path.join(sys.path[0], filename)
            if os.path.exists(f) and self.canonic(f) == self.mainpyfile:
                return f
            root, ext = os.path.splitext(filename)
            if ext == b'':
                filename = filename + b'.py'
            if os.path.isabs(filename):
                return filename
            for dirname in sys.path:
                while os.path.islink(dirname):
                    dirname = os.readlink(dirname)

                fullname = os.path.join(dirname, filename)
                if os.path.exists(fullname):
                    return fullname

            return

    def _runscript(self, filename):
        import __main__
        __main__.__dict__.clear()
        __main__.__dict__.update({b'__name__': b'__main__', b'__file__': filename, 
           b'__builtins__': __builtins__})
        self._wait_for_mainpyfile = 1
        self.mainpyfile = self.canonic(filename)
        self._user_requested_quit = 0
        statement = b'execfile(%r)' % filename
        self.run(statement)
        return


def run(statement, globals=None, locals=None):
    Pdb().run(statement, globals, locals)
    return


def runeval(expression, globals=None, locals=None):
    return Pdb().runeval(expression, globals, locals)


def runctx(statement, globals, locals):
    run(statement, globals, locals)
    return


def runcall(*args, **kwds):
    return Pdb().runcall(*args, **kwds)


def set_trace():
    Pdb().set_trace(sys._getframe().f_back)
    return


def post_mortem(t=None):
    if t is None:
        t = sys.exc_info()[2]
        if t is None:
            raise ValueError(b'A valid traceback must be passed if no exception is being handled')
    p = Pdb()
    p.reset()
    p.interaction(None, t)
    return


def pm():
    post_mortem(sys.last_traceback)
    return


TESTCMD = b'import x; x.main()'

def test():
    run(TESTCMD)
    return


def help():
    for dirname in sys.path:
        fullname = os.path.join(dirname, b'pdb.doc')
        if os.path.exists(fullname):
            sts = os.system(b'${PAGER-more} ' + fullname)
            if sts:
                print b'*** Pager exit status:', sts
            break
    else:
        print b'Sorry, can\'t find the help file "pdb.doc"',
        print b'along the Python search path'

    return


def main():
    if not sys.argv[1:] or sys.argv[1] in (b'--help', b'-h'):
        print b'usage: pdb.py scriptfile [arg] ...'
        sys.exit(2)
    mainpyfile = sys.argv[1]
    if not os.path.exists(mainpyfile):
        print b'Error:', mainpyfile, b'does not exist'
        sys.exit(1)
    del sys.argv[0]
    sys.path[0] = os.path.dirname(mainpyfile)
    pdb = Pdb()
    while True:
        try:
            pdb._runscript(mainpyfile)
            if pdb._user_requested_quit:
                break
            print b'The program finished and will be restarted'
        except Restart:
            print b'Restarting', mainpyfile, b'with arguments:'
            print b'\t' + (b' ').join(sys.argv[1:])
        except SystemExit:
            print b'The program exited via sys.exit(). Exit status: ',
            print sys.exc_info()[1]
        except SyntaxError:
            traceback.print_exc()
            sys.exit(1)
        except:
            traceback.print_exc()
            print b'Uncaught exception. Entering post mortem debugging'
            print b"Running 'cont' or 'step' will restart the program"
            t = sys.exc_info()[2]
            pdb.interaction(None, t)
            print b'Post mortem debugger finished. The ' + mainpyfile + b' will be restarted'

    return


if __name__ == b'__main__':
    import pdb
    pdb.main()
