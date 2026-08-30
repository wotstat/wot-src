import copy
from . import ElementTree
XINCLUDE = b'{http://www.w3.org/2001/XInclude}'
XINCLUDE_INCLUDE = XINCLUDE + b'include'
XINCLUDE_FALLBACK = XINCLUDE + b'fallback'

class FatalIncludeError(SyntaxError):
    pass


def default_loader(href, parse, encoding=None):
    with open(href) as file:
        if parse == b'xml':
            data = ElementTree.parse(file).getroot()
        else:
            data = file.read()
            if encoding:
                data = data.decode(encoding)
    return data


def include(elem, loader=None):
    if loader is None:
        loader = default_loader
    i = 0
    while i < len(elem):
        e = elem[i]
        if e.tag == XINCLUDE_INCLUDE:
            href = e.get(b'href')
            parse = e.get(b'parse', b'xml')
            if parse == b'xml':
                node = loader(href, parse)
                if node is None:
                    raise FatalIncludeError(b'cannot load %r as %r' % (href, parse))
                node = copy.copy(node)
                if e.tail:
                    node.tail = (node.tail or b'') + e.tail
                elem[i] = node
            elif parse == b'text':
                text = loader(href, parse, e.get(b'encoding'))
                if text is None:
                    raise FatalIncludeError(b'cannot load %r as %r' % (href, parse))
                if i:
                    node = elem[i - 1]
                    node.tail = (node.tail or b'') + text + (e.tail or b'')
                else:
                    elem.text = (elem.text or b'') + text + (e.tail or b'')
                del elem[i]
                continue
            else:
                raise FatalIncludeError(b'unknown parse type in xi:include tag (%r)' % parse)
        elif e.tag == XINCLUDE_FALLBACK:
            raise FatalIncludeError(b'xi:fallback tag must be child of xi:include (%r)' % e.tag)
        else:
            include(e, loader)
        i = i + 1

    return
