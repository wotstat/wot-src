from tkCommonDialog import Dialog

class Chooser(Dialog):
    command = b'tk_chooseColor'

    def _fixoptions(self):
        try:
            color = self.options[b'initialcolor']
            if isinstance(color, tuple):
                self.options[b'initialcolor'] = b'#%02x%02x%02x' % color
        except KeyError:
            pass

        return

    def _fixresult(self, widget, result):
        if not result or not str(result):
            return (None, None)
        r, g, b = widget.winfo_rgb(result)
        return ((r / 256, g / 256, b / 256), str(result))


def askcolor(color=None, **options):
    if color:
        options = options.copy()
        options[b'initialcolor'] = color
    return Chooser(**options).show()


if __name__ == b'__main__':
    print b'color', askcolor()
