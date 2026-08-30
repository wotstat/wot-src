import mimetools
__all__ = [
 b'MimeWriter']
import warnings
warnings.warn(b'the MimeWriter module is deprecated; use the email package instead', DeprecationWarning, 2)

class MimeWriter:

    def __init__(self, fp):
        self._fp = fp
        self._headers = []
        return

    def addheader(self, key, value, prefix=0):
        lines = value.split(b'\n')
        while lines and not lines[-1]:
            del lines[-1]

        while lines and not lines[0]:
            del lines[0]

        for i in range(1, len(lines)):
            lines[i] = b'    ' + lines[i].strip()

        value = (b'\n').join(lines) + b'\n'
        line = key + b': ' + value
        if prefix:
            self._headers.insert(0, line)
        else:
            self._headers.append(line)
        return

    def flushheaders(self):
        self._fp.writelines(self._headers)
        self._headers = []
        return

    def startbody(self, ctype, plist=[], prefix=1):
        for name, value in plist:
            ctype = ctype + b';\n %s="%s"' % (name, value)

        self.addheader(b'Content-Type', ctype, prefix=prefix)
        self.flushheaders()
        self._fp.write(b'\n')
        return self._fp

    def startmultipartbody(self, subtype, boundary=None, plist=[], prefix=1):
        self._boundary = boundary or mimetools.choose_boundary()
        return self.startbody(b'multipart/' + subtype, [
         (
          b'boundary', self._boundary)] + plist, prefix=prefix)

    def nextpart(self):
        self._fp.write(b'\n--' + self._boundary + b'\n')
        return self.__class__(self._fp)

    def lastpart(self):
        self._fp.write(b'\n--' + self._boundary + b'--\n')
        return


if __name__ == b'__main__':
    import test.test_MimeWriter
