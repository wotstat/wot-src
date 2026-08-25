from tkCommonDialog import Dialog

class _Dialog(Dialog):

    def _fixoptions(self):
        try:
            self.options[b'filetypes'] = tuple(self.options[b'filetypes'])
        except KeyError:
            pass

        return

    def _fixresult(self, widget, result):
        if result:
            import os
            try:
                result = result.string
            except AttributeError:
                pass

            path, file = os.path.split(result)
            self.options[b'initialdir'] = path
            self.options[b'initialfile'] = file
        self.filename = result
        return result


class Open(_Dialog):
    command = b'tk_getOpenFile'

    def _fixresult(self, widget, result):
        if isinstance(result, tuple):
            result = tuple([getattr(r, b'string', r) for r in result])
            if result:
                import os
                path, file = os.path.split(result[0])
                self.options[b'initialdir'] = path
            return result
        if not widget.tk.wantobjects() and b'multiple' in self.options:
            return self._fixresult(widget, widget.tk.splitlist(result))
        return _Dialog._fixresult(self, widget, result)


class SaveAs(_Dialog):
    command = b'tk_getSaveFile'


class Directory(Dialog):
    command = b'tk_chooseDirectory'

    def _fixresult(self, widget, result):
        if result:
            try:
                result = result.string
            except AttributeError:
                pass

            self.options[b'initialdir'] = result
        self.directory = result
        return result


def askopenfilename(**options):
    return Open(**options).show()


def asksaveasfilename(**options):
    return SaveAs(**options).show()


def askopenfilenames(**options):
    options[b'multiple'] = 1
    return Open(**options).show()


def askopenfile(mode=b'r', **options):
    filename = Open(**options).show()
    if filename:
        return open(filename, mode)
    else:
        return


def askopenfiles(mode=b'r', **options):
    files = askopenfilenames(**options)
    if files:
        ofiles = []
        for filename in files:
            ofiles.append(open(filename, mode))

        files = ofiles
    return files


def asksaveasfile(mode=b'w', **options):
    filename = SaveAs(**options).show()
    if filename:
        return open(filename, mode)
    else:
        return


def askdirectory(**options):
    return Directory(**options).show()


if __name__ == b'__main__':
    enc = b'utf-8'
    import sys
    try:
        import locale
        locale.setlocale(locale.LC_ALL, b'')
        enc = locale.nl_langinfo(locale.CODESET)
    except (ImportError, AttributeError):
        pass

    openfilename = askopenfilename(filetypes=[(b'all files', b'*')])
    try:
        fp = open(openfilename, b'r')
        fp.close()
    except:
        print b'Could not open File: '
        print sys.exc_info()[1]

    print b'open', openfilename.encode(enc)
    saveasfilename = asksaveasfilename()
    print b'saveas', saveasfilename.encode(enc)
