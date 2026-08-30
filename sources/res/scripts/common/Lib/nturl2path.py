def url2pathname(url):
    import string, urllib
    url = url.replace(b':', b'|')
    if b'|' not in url:
        if url[:4] == b'////':
            url = url[2:]
        components = url.split(b'/')
        return urllib.unquote((b'\\').join(components))
    comp = url.split(b'|')
    if len(comp) != 2 or comp[0][-1] not in string.ascii_letters:
        error = b'Bad URL: ' + url
        raise IOError, error
    drive = comp[0][-1].upper()
    path = drive + b':'
    components = comp[1].split(b'/')
    for comp in components:
        if comp:
            path = path + b'\\' + urllib.unquote(comp)

    if path.endswith(b':') and url.endswith(b'/'):
        path += b'\\'
    return path


def pathname2url(p):
    import urllib
    if b':' not in p:
        if p[:2] == b'\\\\':
            p = b'\\\\' + p
        components = p.split(b'\\')
        return urllib.quote((b'/').join(components))
    comp = p.split(b':')
    if len(comp) != 2 or len(comp[0]) > 1:
        error = b'Bad path: ' + p
        raise IOError, error
    drive = urllib.quote(comp[0].upper())
    components = comp[1].split(b'\\')
    path = b'///' + drive + b':'
    for comp in components:
        if comp:
            path = path + b'/' + urllib.quote(comp)

    return path
