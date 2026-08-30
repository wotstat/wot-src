__all__ = [
 b'what']

def what(file, h=None):
    f = None
    try:
        if h is None:
            if isinstance(file, basestring):
                f = open(file, b'rb')
                h = f.read(32)
            else:
                location = file.tell()
                h = file.read(32)
                file.seek(location)
        for tf in tests:
            res = tf(h, f)
            if res:
                return res

    finally:
        if f:
            f.close()

    return


tests = []

def test_jpeg(h, f):
    if h[6:10] == b'JFIF':
        return b'jpeg'
    return


tests.append(test_jpeg)

def test_exif(h, f):
    if h[6:10] == b'Exif':
        return b'jpeg'
    return


tests.append(test_exif)

def test_png(h, f):
    if h[:8] == b'\x89PNG\r\n\x1a\n':
        return b'png'
    return


tests.append(test_png)

def test_gif(h, f):
    if h[:6] in (b'GIF87a', b'GIF89a'):
        return b'gif'
    return


tests.append(test_gif)

def test_tiff(h, f):
    if h[:2] in (b'MM', b'II'):
        return b'tiff'
    return


tests.append(test_tiff)

def test_rgb(h, f):
    if h[:2] == b'\x01\xda':
        return b'rgb'
    return


tests.append(test_rgb)

def test_pbm(h, f):
    if len(h) >= 3 and h[0] == b'P' and h[1] in b'14' and h[2] in b' \t\n\r':
        return b'pbm'
    return


tests.append(test_pbm)

def test_pgm(h, f):
    if len(h) >= 3 and h[0] == b'P' and h[1] in b'25' and h[2] in b' \t\n\r':
        return b'pgm'
    return


tests.append(test_pgm)

def test_ppm(h, f):
    if len(h) >= 3 and h[0] == b'P' and h[1] in b'36' and h[2] in b' \t\n\r':
        return b'ppm'
    return


tests.append(test_ppm)

def test_rast(h, f):
    if h[:4] == b'Y\xa6j\x95':
        return b'rast'
    return


tests.append(test_rast)

def test_xbm(h, f):
    s = b'#define '
    if h[:len(s)] == s:
        return b'xbm'
    return


tests.append(test_xbm)

def test_bmp(h, f):
    if h[:2] == b'BM':
        return b'bmp'
    return


tests.append(test_bmp)

def test():
    import sys
    recursive = 0
    if sys.argv[1:] and sys.argv[1] == b'-r':
        del sys.argv[1:2]
        recursive = 1
    try:
        if sys.argv[1:]:
            testall(sys.argv[1:], recursive, 1)
        else:
            testall([b'.'], recursive, 1)
    except KeyboardInterrupt:
        sys.stderr.write(b'\n[Interrupted]\n')
        sys.exit(1)

    return


def testall(list, recursive, toplevel):
    import sys, os
    for filename in list:
        if os.path.isdir(filename):
            print filename + b'/:',
            if recursive or toplevel:
                print b'recursing down:'
                import glob
                names = glob.glob(os.path.join(filename, b'*'))
                testall(names, recursive, 0)
            else:
                print b'*** directory (use -r) ***'
        else:
            print filename + b':',
            sys.stdout.flush()
            try:
                print what(filename)
            except IOError:
                print b'*** not found ***'

    return
