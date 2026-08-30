from __future__ import with_statement
import sys, os, difflib, logging, shutil, optparse
from . import refactor

def diff_texts(a, b, filename):
    a = a.splitlines()
    b = b.splitlines()
    return difflib.unified_diff(a, b, filename, filename, b'(original)', b'(refactored)', lineterm=b'')


class StdoutRefactoringTool(refactor.MultiprocessRefactoringTool):

    def __init__(self, fixers, options, explicit, nobackups, show_diffs, input_base_dir=b'', output_dir=b'', append_suffix=b''):
        self.nobackups = nobackups
        self.show_diffs = show_diffs
        if input_base_dir and not input_base_dir.endswith(os.sep):
            input_base_dir += os.sep
        self._input_base_dir = input_base_dir
        self._output_dir = output_dir
        self._append_suffix = append_suffix
        super(StdoutRefactoringTool, self).__init__(fixers, options, explicit)
        return

    def log_error(self, msg, *args, **kwargs):
        self.errors.append((msg, args, kwargs))
        self.logger.error(msg, *args, **kwargs)
        return

    def write_file(self, new_text, filename, old_text, encoding):
        orig_filename = filename
        if self._output_dir:
            if filename.startswith(self._input_base_dir):
                filename = os.path.join(self._output_dir, filename[len(self._input_base_dir):])
            else:
                raise ValueError(b'filename %s does not start with the input_base_dir %s' % (
                 filename, self._input_base_dir))
        if self._append_suffix:
            filename += self._append_suffix
        if orig_filename != filename:
            output_dir = os.path.dirname(filename)
            if not os.path.isdir(output_dir):
                os.makedirs(output_dir)
            self.log_message(b'Writing converted %s to %s.', orig_filename, filename)
        if not self.nobackups:
            backup = filename + b'.bak'
            if os.path.lexists(backup):
                try:
                    os.remove(backup)
                except os.error as err:
                    self.log_message(b"Can't remove backup %s", backup)

            try:
                os.rename(filename, backup)
            except os.error as err:
                self.log_message(b"Can't rename %s to %s", filename, backup)

        write = super(StdoutRefactoringTool, self).write_file
        write(new_text, filename, old_text, encoding)
        if not self.nobackups:
            shutil.copymode(backup, filename)
        if orig_filename != filename:
            shutil.copymode(orig_filename, filename)
        return

    def print_output(self, old, new, filename, equal):
        if equal:
            self.log_message(b'No changes to %s', filename)
        else:
            self.log_message(b'Refactored %s', filename)
            if self.show_diffs:
                diff_lines = diff_texts(old, new, filename)
                try:
                    if self.output_lock is not None:
                        with self.output_lock:
                            for line in diff_lines:
                                print line

                            sys.stdout.flush()
                    else:
                        for line in diff_lines:
                            print line

                except UnicodeEncodeError:
                    warn(b"couldn't encode %s's diff for your terminal" % (
                     filename,))
                    return

        return


def warn(msg):
    print >> sys.stderr, b'WARNING: %s' % (msg,)
    return


def main(fixer_pkg, args=None):
    parser = optparse.OptionParser(usage=b'2to3 [options] file|dir ...')
    parser.add_option(b'-d', b'--doctests_only', action=b'store_true', help=b'Fix up doctests only')
    parser.add_option(b'-f', b'--fix', action=b'append', default=[], help=b'Each FIX specifies a transformation; default: all')
    parser.add_option(b'-j', b'--processes', action=b'store', default=1, type=b'int', help=b'Run 2to3 concurrently')
    parser.add_option(b'-x', b'--nofix', action=b'append', default=[], help=b'Prevent a transformation from being run')
    parser.add_option(b'-l', b'--list-fixes', action=b'store_true', help=b'List available transformations')
    parser.add_option(b'-p', b'--print-function', action=b'store_true', help=b'Modify the grammar so that print() is a function')
    parser.add_option(b'-v', b'--verbose', action=b'store_true', help=b'More verbose logging')
    parser.add_option(b'--no-diffs', action=b'store_true', help=b"Don't show diffs of the refactoring")
    parser.add_option(b'-w', b'--write', action=b'store_true', help=b'Write back modified files')
    parser.add_option(b'-n', b'--nobackups', action=b'store_true', default=False, help=b"Don't write backups for modified files")
    parser.add_option(b'-o', b'--output-dir', action=b'store', type=b'str', default=b'', help=b'Put output files in this directory instead of overwriting the input files.  Requires -n.')
    parser.add_option(b'-W', b'--write-unchanged-files', action=b'store_true', help=b'Also write files even if no changes were required (useful with --output-dir); implies -w.')
    parser.add_option(b'--add-suffix', action=b'store', type=b'str', default=b'', help=b"Append this string to all output filenames. Requires -n if non-empty.  ex: --add-suffix='3' will generate .py3 files.")
    refactor_stdin = False
    flags = {}
    options, args = parser.parse_args(args)
    if options.write_unchanged_files:
        flags[b'write_unchanged_files'] = True
        if not options.write:
            warn(b'--write-unchanged-files/-W implies -w.')
        options.write = True
    if options.output_dir and not options.nobackups:
        parser.error(b"Can't use --output-dir/-o without -n.")
    if options.add_suffix and not options.nobackups:
        parser.error(b"Can't use --add-suffix without -n.")
    if not options.write and options.no_diffs:
        warn(b"not writing files and not printing diffs; that's not very useful")
    if not options.write and options.nobackups:
        parser.error(b"Can't use -n without -w")
    if options.list_fixes:
        print b'Available transformations for the -f/--fix option:'
        for fixname in refactor.get_all_fix_names(fixer_pkg):
            print fixname

        if not args:
            return 0
    if not args:
        print >> sys.stderr, b'At least one file or directory argument required.'
        print >> sys.stderr, b'Use --help to show usage.'
        return 2
    if b'-' in args:
        refactor_stdin = True
        if options.write:
            print >> sys.stderr, b"Can't write to stdin."
            return 2
    if options.print_function:
        flags[b'print_function'] = True
    level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(format=b'%(name)s: %(message)s', level=level)
    logger = logging.getLogger(b'lib2to3.main')
    avail_fixes = set(refactor.get_fixers_from_package(fixer_pkg))
    unwanted_fixes = set(fixer_pkg + b'.fix_' + fix for fix in options.nofix)
    explicit = set()
    if options.fix:
        all_present = False
        for fix in options.fix:
            if fix == b'all':
                all_present = True
            else:
                explicit.add(fixer_pkg + b'.fix_' + fix)

        requested = avail_fixes.union(explicit) if all_present else explicit
    else:
        requested = avail_fixes.union(explicit)
    fixer_names = requested.difference(unwanted_fixes)
    input_base_dir = os.path.commonprefix(args)
    if input_base_dir and not input_base_dir.endswith(os.sep) and not os.path.isdir(input_base_dir):
        input_base_dir = os.path.dirname(input_base_dir)
    if options.output_dir:
        input_base_dir = input_base_dir.rstrip(os.sep)
        logger.info(b'Output in %r will mirror the input directory %r layout.', options.output_dir, input_base_dir)
    rt = StdoutRefactoringTool(sorted(fixer_names), flags, sorted(explicit), options.nobackups, not options.no_diffs, input_base_dir=input_base_dir, output_dir=options.output_dir, append_suffix=options.add_suffix)
    if not rt.errors:
        if refactor_stdin:
            rt.refactor_stdin()
        else:
            try:
                rt.refactor(args, options.write, options.doctests_only, options.processes)
            except refactor.MultiprocessingUnsupported:
                print >> sys.stderr, b"Sorry, -j isn't supported on this platform."
                return 1

        rt.summarize()
    return int(bool(rt.errors))
