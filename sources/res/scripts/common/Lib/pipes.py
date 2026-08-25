import re, os, tempfile, string
__all__ = [
 b'Template']
FILEIN_FILEOUT = b'ff'
STDIN_FILEOUT = b'-f'
FILEIN_STDOUT = b'f-'
STDIN_STDOUT = b'--'
SOURCE = b'.-'
SINK = b'-.'
stepkinds = [
 FILEIN_FILEOUT, STDIN_FILEOUT, FILEIN_STDOUT, STDIN_STDOUT, 
 SOURCE, SINK]

class Template:

    def __init__(self):
        self.debugging = 0
        self.reset()
        return

    def __repr__(self):
        return b'<Template instance, steps=%r>' % (self.steps,)

    def reset(self):
        self.steps = []
        return

    def clone(self):
        t = Template()
        t.steps = self.steps[:]
        t.debugging = self.debugging
        return t

    def debug(self, flag):
        self.debugging = flag
        return

    def append(self, cmd, kind):
        if type(cmd) is not type(b''):
            raise TypeError, b'Template.append: cmd must be a string'
        if kind not in stepkinds:
            raise ValueError, b'Template.append: bad kind %r' % (kind,)
        if kind == SOURCE:
            raise ValueError, b'Template.append: SOURCE can only be prepended'
        if self.steps and self.steps[-1][1] == SINK:
            raise ValueError, b'Template.append: already ends with SINK'
        if kind[0] == b'f' and not re.search(b'\\$IN\\b', cmd):
            raise ValueError, b'Template.append: missing $IN in cmd'
        if kind[1] == b'f' and not re.search(b'\\$OUT\\b', cmd):
            raise ValueError, b'Template.append: missing $OUT in cmd'
        self.steps.append((cmd, kind))
        return

    def prepend(self, cmd, kind):
        if type(cmd) is not type(b''):
            raise TypeError, b'Template.prepend: cmd must be a string'
        if kind not in stepkinds:
            raise ValueError, b'Template.prepend: bad kind %r' % (kind,)
        if kind == SINK:
            raise ValueError, b'Template.prepend: SINK can only be appended'
        if self.steps and self.steps[0][1] == SOURCE:
            raise ValueError, b'Template.prepend: already begins with SOURCE'
        if kind[0] == b'f' and not re.search(b'\\$IN\\b', cmd):
            raise ValueError, b'Template.prepend: missing $IN in cmd'
        if kind[1] == b'f' and not re.search(b'\\$OUT\\b', cmd):
            raise ValueError, b'Template.prepend: missing $OUT in cmd'
        self.steps.insert(0, (cmd, kind))
        return

    def open(self, file, rw):
        if rw == b'r':
            return self.open_r(file)
        if rw == b'w':
            return self.open_w(file)
        raise ValueError, b"Template.open: rw must be 'r' or 'w', not %r" % (rw,)
        return

    def open_r(self, file):
        if not self.steps:
            return open(file, b'r')
        if self.steps[-1][1] == SINK:
            raise ValueError, b'Template.open_r: pipeline ends width SINK'
        cmd = self.makepipeline(file, b'')
        return os.popen(cmd, b'r')

    def open_w(self, file):
        if not self.steps:
            return open(file, b'w')
        if self.steps[0][1] == SOURCE:
            raise ValueError, b'Template.open_w: pipeline begins with SOURCE'
        cmd = self.makepipeline(b'', file)
        return os.popen(cmd, b'w')

    def copy(self, infile, outfile):
        return os.system(self.makepipeline(infile, outfile))

    def makepipeline(self, infile, outfile):
        cmd = makepipeline(infile, self.steps, outfile)
        if self.debugging:
            print cmd
            cmd = b'set -x; ' + cmd
        return cmd


def makepipeline(infile, steps, outfile):
    list = []
    for cmd, kind in steps:
        list.append([b'', cmd, kind, b''])

    if not list:
        list.append([b'', b'cat', b'--', b''])
    cmd, kind = list[0][1:3]
    if kind[0] == b'f' and not infile:
        list.insert(0, [b'', b'cat', b'--', b''])
    list[0][0] = infile
    cmd, kind = list[-1][1:3]
    if kind[1] == b'f' and not outfile:
        list.append([b'', b'cat', b'--', b''])
    list[-1][-1] = outfile
    garbage = []
    for i in range(1, len(list)):
        lkind = list[i - 1][2]
        rkind = list[i][2]
        if lkind[1] == b'f' or rkind[0] == b'f':
            fd, temp = tempfile.mkstemp()
            os.close(fd)
            garbage.append(temp)
            list[i - 1][-1] = list[i][0] = temp

    for item in list:
        inf, cmd, kind, outf = item
        if kind[1] == b'f':
            cmd = b'OUT=' + quote(outf) + b'; ' + cmd
        if kind[0] == b'f':
            cmd = b'IN=' + quote(inf) + b'; ' + cmd
        if kind[0] == b'-' and inf:
            cmd = cmd + b' <' + quote(inf)
        if kind[1] == b'-' and outf:
            cmd = cmd + b' >' + quote(outf)
        item[1] = cmd

    cmdlist = list[0][1]
    for item in list[1:]:
        cmd, kind = item[1:3]
        if item[0] == b'':
            if b'f' in kind:
                cmd = b'{ ' + cmd + b'; }'
            cmdlist = cmdlist + b' |\n' + cmd
        else:
            cmdlist = cmdlist + b'\n' + cmd

    if garbage:
        rmcmd = b'rm -f'
        for file in garbage:
            rmcmd = rmcmd + b' ' + quote(file)

        trapcmd = b'trap ' + quote(rmcmd + b'; exit') + b' 1 2 3 13 14 15'
        cmdlist = trapcmd + b'\n' + cmdlist + b'\n' + rmcmd
    return cmdlist


_safechars = frozenset(string.ascii_letters + string.digits + b'@%_-+=:,./')

def quote(file):
    for c in file:
        if c not in _safechars:
            break
    else:
        if not file:
            return b"''"
        else:
            return file

    return b"'" + file.replace(b"'", b'\'"\'"\'') + b"'"
