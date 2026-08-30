from idlelib.configHandler import idleConf

class History:

    def __init__(self, text):
        self.text = text
        self.history = []
        self.prefix = None
        self.pointer = None
        self.cyclic = idleConf.GetOption(b'main', b'History', b'cyclic', 1, b'bool')
        text.bind(b'<<history-previous>>', self.history_prev)
        text.bind(b'<<history-next>>', self.history_next)
        return

    def history_next(self, event):
        self.fetch(reverse=False)
        return b'break'

    def history_prev(self, event):
        self.fetch(reverse=True)
        return b'break'

    def fetch(self, reverse):
        nhist = len(self.history)
        pointer = self.pointer
        prefix = self.prefix
        if pointer is not None and prefix is not None:
            if self.text.compare(b'insert', b'!=', b'end-1c') or self.text.get(b'iomark', b'end-1c') != self.history[pointer]:
                pointer = prefix = None
                self.text.mark_set(b'insert', b'end-1c')
        if pointer is None or prefix is None:
            prefix = self.text.get(b'iomark', b'end-1c')
            if reverse:
                pointer = nhist
            elif self.cyclic:
                pointer = -1
            else:
                self.text.bell()
                return
        nprefix = len(prefix)
        while 1:
            pointer += -1 if reverse else 1
            if pointer < 0 or pointer >= nhist:
                self.text.bell()
                if not self.cyclic and pointer < 0:
                    return
                if self.text.get(b'iomark', b'end-1c') != prefix:
                    self.text.delete(b'iomark', b'end-1c')
                    self.text.insert(b'iomark', prefix)
                pointer = prefix = None
                break
            item = self.history[pointer]
            if item[:nprefix] == prefix and len(item) > nprefix:
                self.text.delete(b'iomark', b'end-1c')
                self.text.insert(b'iomark', item)
                break

        self.text.see(b'insert')
        self.text.tag_remove(b'sel', b'1.0', b'end')
        self.pointer = pointer
        self.prefix = prefix
        return

    def store(self, source):
        source = source.strip()
        if len(source) > 2:
            try:
                self.history.remove(source)
            except ValueError:
                pass

            self.history.append(source)
        self.pointer = None
        self.prefix = None
        return


if __name__ == b'__main__':
    from unittest import main
    main(b'idlelib.idle_test.test_idlehistory', verbosity=2, exit=False)
