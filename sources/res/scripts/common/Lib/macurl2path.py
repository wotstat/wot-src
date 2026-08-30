import urllib, os
__all__ = [
 b'url2pathname', b'pathname2url']

def url2pathname(pathname):
    tp = urllib.splittype(pathname)[0]
    if tp and tp != b'file':
        raise RuntimeError, b'Cannot convert non-local URL to pathname'
    if pathname[:3] == b'///':
        pathname = pathname[2:]
    elif pathname[:2] == b'//':
        raise RuntimeError, b'Cannot convert non-local URL to pathname'
    components = pathname.split(b'/')
    i = 0
    while i < len(components):
        if components[i] == b'.':
            del components[i]
        elif components[i] == b'..' and i > 0 and components[i - 1] not in (b'', b'..'):
            del components[i - 1:i + 1]
            i = i - 1
        elif components[i] == b'' and i > 0 and components[i - 1] != b'':
            del components[i]
        else:
            i = i + 1

    if not components[0]:
        rv = (b':').join(components[1:])
    else:
        i = 0
        while i < len(components) and components[i] == b'..':
            components[i] = b''
            i = i + 1

        rv = b':' + (b':').join(components)
    return urllib.unquote(rv)


def pathname2url(pathname):
    if b'/' in pathname:
        raise RuntimeError, b'Cannot convert pathname containing slashes'
    components = pathname.split(b':')
    if components[0] == b'':
        del components[0]
    if components[-1] == b'':
        del components[-1]
    for i in range(len(components)):
        if components[i] == b'':
            components[i] = b'..'

    components = map(_pncomp2url, components)
    if os.path.isabs(pathname):
        return b'/' + (b'/').join(components)
    else:
        return (b'/').join(components)

    return


def _pncomp2url(component):
    component = urllib.quote(component[:31], safe=b'')
    return component
