import string, re

class AutoExpand:
    menudefs = [
     (
      b'edit',
      [
       (b'E_xpand Word', b'<<expand-word>>')])]
    wordchars = string.ascii_letters + string.digits + b'_'

    def __init__(self, editwin):
        self.text = editwin.text
        self.state = None
        return

    def expand_word_event(self, event):
        curinsert = self.text.index(b'insert')
        curline = self.text.get(b'insert linestart', b'insert lineend')
        if not self.state:
            words = self.getwords()
            index = 0
        else:
            words, index, insert, line = self.state
            if insert != curinsert or line != curline:
                words = self.getwords()
                index = 0
        if not words:
            self.text.bell()
            return b'break'
        word = self.getprevword()
        self.text.delete(b'insert - %d chars' % len(word), b'insert')
        newword = words[index]
        index = (index + 1) % len(words)
        if index == 0:
            self.text.bell()
        self.text.insert(b'insert', newword)
        curinsert = self.text.index(b'insert')
        curline = self.text.get(b'insert linestart', b'insert lineend')
        self.state = (words, index, curinsert, curline)
        return b'break'

    def getwords(self):
        word = self.getprevword()
        if not word:
            return []
        before = self.text.get(b'1.0', b'insert wordstart')
        wbefore = re.findall(b'\\b' + word + b'\\w+\\b', before)
        del before
        after = self.text.get(b'insert wordend', b'end')
        wafter = re.findall(b'\\b' + word + b'\\w+\\b', after)
        del after
        if not wbefore and not wafter:
            return []
        words = []
        dict = {}
        wbefore.reverse()
        for w in wbefore:
            if dict.get(w):
                continue
            words.append(w)
            dict[w] = w

        for w in wafter:
            if dict.get(w):
                continue
            words.append(w)
            dict[w] = w

        words.append(word)
        return words

    def getprevword(self):
        line = self.text.get(b'insert linestart', b'insert')
        i = len(line)
        while i > 0 and line[i - 1] in self.wordchars:
            i = i - 1

        return line[i:]


if __name__ == b'__main__':
    import unittest
    unittest.main(b'idlelib.idle_test.test_autoexpand', verbosity=2)
