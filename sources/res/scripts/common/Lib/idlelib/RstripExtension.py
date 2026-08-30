class RstripExtension:
    menudefs = [
     (
      b'format', [None, (b'Strip trailing whitespace', b'<<do-rstrip>>')])]

    def __init__(self, editwin):
        self.editwin = editwin
        self.editwin.text.bind(b'<<do-rstrip>>', self.do_rstrip)
        return

    def do_rstrip(self, event=None):
        text = self.editwin.text
        undo = self.editwin.undo
        undo.undo_block_start()
        end_line = int(float(text.index(b'end')))
        for cur in range(1, end_line):
            txt = text.get(b'%i.0' % cur, b'%i.end' % cur)
            raw = len(txt)
            cut = len(txt.rstrip())
            if cut < raw:
                text.delete(b'%i.%i' % (cur, cut), b'%i.end' % cur)

        undo.undo_block_stop()
        return


if __name__ == b'__main__':
    import unittest
    unittest.main(b'idlelib.idle_test.test_rstrip', verbosity=2, exit=False)
