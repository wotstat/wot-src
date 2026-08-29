import re
from idlelib.configHandler import idleConf

class FormatParagraph:
    menudefs = [
     (
      b'format',
      [
       (b'Format Paragraph', b'<<format-paragraph>>')])]

    def __init__(self, editwin):
        self.editwin = editwin
        return

    def close(self):
        self.editwin = None
        return

    def format_paragraph_event(self, event, limit=None):
        if limit is None:
            limit = idleConf.GetOption(b'extensions', b'FormatParagraph', b'max-width', type=b'int', default=72)
        text = self.editwin.text
        first, last = self.editwin.get_selection_indices()
        if first and last:
            data = text.get(first, last)
            comment_header = get_comment_header(data)
        else:
            first, last, comment_header, data = find_paragraph(text, text.index(b'insert'))
        if comment_header:
            newdata = reformat_comment(data, limit, comment_header)
        else:
            newdata = reformat_paragraph(data, limit)
        text.tag_remove(b'sel', b'1.0', b'end')
        if newdata != data:
            text.mark_set(b'insert', first)
            text.undo_block_start()
            text.delete(first, last)
            text.insert(first, newdata)
            text.undo_block_stop()
        else:
            text.mark_set(b'insert', last)
        text.see(b'insert')
        return b'break'


def find_paragraph(text, mark):
    lineno, col = map(int, mark.split(b'.'))
    line = text.get(b'%d.0' % lineno, b'%d.end' % lineno)
    while text.compare(b'%d.0' % lineno, b'<', b'end') and is_all_white(line):
        lineno = lineno + 1
        line = text.get(b'%d.0' % lineno, b'%d.end' % lineno)

    first_lineno = lineno
    comment_header = get_comment_header(line)
    comment_header_len = len(comment_header)
    while get_comment_header(line) == comment_header and not is_all_white(line[comment_header_len:]):
        lineno = lineno + 1
        line = text.get(b'%d.0' % lineno, b'%d.end' % lineno)

    last = b'%d.0' % lineno
    lineno = first_lineno - 1
    line = text.get(b'%d.0' % lineno, b'%d.end' % lineno)
    while lineno > 0 and get_comment_header(line) == comment_header and not is_all_white(line[comment_header_len:]):
        lineno = lineno - 1
        line = text.get(b'%d.0' % lineno, b'%d.end' % lineno)

    first = b'%d.0' % (lineno + 1)
    return (
     first, last, comment_header, text.get(first, last))


def reformat_paragraph(data, limit):
    lines = data.split(b'\n')
    i = 0
    n = len(lines)
    while i < n and is_all_white(lines[i]):
        i = i + 1

    if i >= n:
        return data
    indent1 = get_indent(lines[i])
    if i + 1 < n and not is_all_white(lines[i + 1]):
        indent2 = get_indent(lines[i + 1])
    else:
        indent2 = indent1
    new = lines[:i]
    partial = indent1
    while i < n and not is_all_white(lines[i]):
        words = re.split(b'(\\s+)', lines[i])
        for j in range(0, len(words), 2):
            word = words[j]
            if not word:
                continue
            if len((partial + word).expandtabs()) > limit and partial != indent1:
                new.append(partial.rstrip())
                partial = indent2
            partial = partial + word + b' '
            if j + 1 < len(words) and words[j + 1] != b' ':
                partial = partial + b' '

        i = i + 1

    new.append(partial.rstrip())
    new.extend(lines[i:])
    return (b'\n').join(new)


def reformat_comment(data, limit, comment_header):
    lc = len(comment_header)
    data = (b'\n').join(line[lc:] for line in data.split(b'\n'))
    format_width = max(limit - len(comment_header), 20)
    newdata = reformat_paragraph(data, format_width)
    newdata = newdata.split(b'\n')
    block_suffix = b''
    if not newdata[-1]:
        block_suffix = b'\n'
        newdata = newdata[:-1]
    return (b'\n').join(comment_header + line for line in newdata) + block_suffix


def is_all_white(line):
    return re.match(b'^\\s*$', line) is not None


def get_indent(line):
    return re.match(b'^([ \\t]*)', line).group()


def get_comment_header(line):
    m = re.match(b'^([ \\t]*#*)', line)
    if m is None:
        return b''
    else:
        return m.group(1)


if __name__ == b'__main__':
    import unittest
    unittest.main(b'idlelib.idle_test.test_formatparagraph', verbosity=2, exit=False)
