__revision__ = b'$Id$'
import os, re, fnmatch
from distutils.util import convert_path
from distutils.errors import DistutilsTemplateError, DistutilsInternalError
from distutils import log

class FileList:

    def __init__(self, warn=None, debug_print=None):
        self.allfiles = None
        self.files = []
        return

    def set_allfiles(self, allfiles):
        self.allfiles = allfiles
        return

    def findall(self, dir=os.curdir):
        self.allfiles = findall(dir)
        return

    def debug_print(self, msg):
        from distutils.debug import DEBUG
        if DEBUG:
            print msg
        return

    def append(self, item):
        self.files.append(item)
        return

    def extend(self, items):
        self.files.extend(items)
        return

    def sort(self):
        sortable_files = map(os.path.split, self.files)
        sortable_files.sort()
        self.files = []
        for sort_tuple in sortable_files:
            self.files.append(os.path.join(*sort_tuple))

        return

    def remove_duplicates(self):
        for i in range(len(self.files) - 1, 0, -1):
            if self.files[i] == self.files[i - 1]:
                del self.files[i]

        return

    def _parse_template_line(self, line):
        words = line.split()
        action = words[0]
        patterns = dir = dir_pattern = None
        if action in (b'include', b'exclude', b'global-include', b'global-exclude'):
            if len(words) < 2:
                raise DistutilsTemplateError, b"'%s' expects <pattern1> <pattern2> ..." % action
            patterns = map(convert_path, words[1:])
        elif action in (b'recursive-include', b'recursive-exclude'):
            if len(words) < 3:
                raise DistutilsTemplateError, b"'%s' expects <dir> <pattern1> <pattern2> ..." % action
            dir = convert_path(words[1])
            patterns = map(convert_path, words[2:])
        elif action in (b'graft', b'prune'):
            if len(words) != 2:
                raise DistutilsTemplateError, b"'%s' expects a single <dir_pattern>" % action
            dir_pattern = convert_path(words[1])
        else:
            raise DistutilsTemplateError, b"unknown action '%s'" % action
        return (action, patterns, dir, dir_pattern)

    def process_template_line(self, line):
        action, patterns, dir, dir_pattern = self._parse_template_line(line)
        if action == b'include':
            self.debug_print(b'include ' + (b' ').join(patterns))
            for pattern in patterns:
                if not self.include_pattern(pattern, anchor=1):
                    log.warn(b"warning: no files found matching '%s'", pattern)

        elif action == b'exclude':
            self.debug_print(b'exclude ' + (b' ').join(patterns))
            for pattern in patterns:
                if not self.exclude_pattern(pattern, anchor=1):
                    log.warn(b"warning: no previously-included files found matching '%s'", pattern)

        elif action == b'global-include':
            self.debug_print(b'global-include ' + (b' ').join(patterns))
            for pattern in patterns:
                if not self.include_pattern(pattern, anchor=0):
                    log.warn(b"warning: no files found matching '%s' " + b'anywhere in distribution', pattern)

        elif action == b'global-exclude':
            self.debug_print(b'global-exclude ' + (b' ').join(patterns))
            for pattern in patterns:
                if not self.exclude_pattern(pattern, anchor=0):
                    log.warn(b"warning: no previously-included files matching '%s' found anywhere in distribution", pattern)

        elif action == b'recursive-include':
            self.debug_print(b'recursive-include %s %s' % (
             dir, (b' ').join(patterns)))
            for pattern in patterns:
                if not self.include_pattern(pattern, prefix=dir):
                    log.warn(b"warning: no files found matching '%s' " + b"under directory '%s'", pattern, dir)

        elif action == b'recursive-exclude':
            self.debug_print(b'recursive-exclude %s %s' % (
             dir, (b' ').join(patterns)))
            for pattern in patterns:
                if not self.exclude_pattern(pattern, prefix=dir):
                    log.warn(b"warning: no previously-included files matching '%s' found under directory '%s'", pattern, dir)

        elif action == b'graft':
            self.debug_print(b'graft ' + dir_pattern)
            if not self.include_pattern(None, prefix=dir_pattern):
                log.warn(b"warning: no directories found matching '%s'", dir_pattern)
        elif action == b'prune':
            self.debug_print(b'prune ' + dir_pattern)
            if not self.exclude_pattern(None, prefix=dir_pattern):
                log.warn(b'no previously-included directories found ' + b"matching '%s'", dir_pattern)
        else:
            raise DistutilsInternalError, b"this cannot happen: invalid action '%s'" % action
        return

    def include_pattern(self, pattern, anchor=1, prefix=None, is_regex=0):
        files_found = 0
        pattern_re = translate_pattern(pattern, anchor, prefix, is_regex)
        self.debug_print(b"include_pattern: applying regex r'%s'" % pattern_re.pattern)
        if self.allfiles is None:
            self.findall()
        for name in self.allfiles:
            if pattern_re.search(name):
                self.debug_print(b' adding ' + name)
                self.files.append(name)
                files_found = 1

        return files_found

    def exclude_pattern(self, pattern, anchor=1, prefix=None, is_regex=0):
        files_found = 0
        pattern_re = translate_pattern(pattern, anchor, prefix, is_regex)
        self.debug_print(b"exclude_pattern: applying regex r'%s'" % pattern_re.pattern)
        for i in range(len(self.files) - 1, -1, -1):
            if pattern_re.search(self.files[i]):
                self.debug_print(b' removing ' + self.files[i])
                del self.files[i]
                files_found = 1

        return files_found


def findall(dir=os.curdir):
    from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK
    list = []
    stack = [
     dir]
    pop = stack.pop
    push = stack.append
    while stack:
        dir = pop()
        names = os.listdir(dir)
        for name in names:
            if dir != os.curdir:
                fullname = os.path.join(dir, name)
            else:
                fullname = name
            stat = os.stat(fullname)
            mode = stat[ST_MODE]
            if S_ISREG(mode):
                list.append(fullname)
            elif S_ISDIR(mode) and not S_ISLNK(mode):
                push(fullname)

    return list


def glob_to_re(pattern):
    pattern_re = fnmatch.translate(pattern)
    sep = os.sep
    if os.sep == b'\\':
        sep = b'\\\\\\\\'
    escaped = b'\\1[^%s]' % sep
    pattern_re = re.sub(b'((?<!\\\\)(\\\\\\\\)*)\\.', escaped, pattern_re)
    return pattern_re


def translate_pattern(pattern, anchor=1, prefix=None, is_regex=0):
    if is_regex:
        if isinstance(pattern, str):
            return re.compile(pattern)
        else:
            return pattern

    if pattern:
        pattern_re = glob_to_re(pattern)
    else:
        pattern_re = b''
    if prefix is not None:
        empty_pattern = glob_to_re(b'')
        prefix_re = glob_to_re(prefix)[:-len(empty_pattern)]
        sep = os.sep
        if os.sep == b'\\':
            sep = b'\\\\'
        pattern_re = b'^' + sep.join((prefix_re, b'.*' + pattern_re))
    elif anchor:
        pattern_re = b'^' + pattern_re
    return re.compile(pattern_re)
