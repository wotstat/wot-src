import re
xpath_tokenizer_re = re.compile(b'(\'[^\']*\'|"[^"]*"|::|//?|\\.\\.|\\(\\)|[/.*:\\[\\]\\(\\)@=])|((?:\\{[^}]+\\})?[^/\\[\\]\\(\\)@=\\s]+)|\\s+')

def xpath_tokenizer(pattern, namespaces=None):
    for token in xpath_tokenizer_re.findall(pattern):
        tag = token[1]
        if tag and tag[0] != b'{' and b':' in tag:
            try:
                prefix, uri = tag.split(b':', 1)
                if not namespaces:
                    raise KeyError
                yield (
                 token[0], b'{%s}%s' % (namespaces[prefix], uri))
            except KeyError:
                raise SyntaxError(b'prefix %r not found in prefix map' % prefix)

        else:
            yield token

    return


def get_parent_map(context):
    parent_map = context.parent_map
    if parent_map is None:
        context.parent_map = parent_map = {}
        for p in context.root.iter():
            for e in p:
                parent_map[e] = p

    return parent_map


def prepare_child(next, token):
    tag = token[1]

    def select(context, result):
        for elem in result:
            for e in elem:
                if e.tag == tag:
                    yield e

        return

    return select


def prepare_star(next, token):

    def select(context, result):
        for elem in result:
            for e in elem:
                yield e

        return

    return select


def prepare_self(next, token):

    def select(context, result):
        for elem in result:
            yield elem

        return

    return select


def prepare_descendant(next, token):
    token = next()
    if token[0] == b'*':
        tag = b'*'
    elif not token[0]:
        tag = token[1]
    else:
        raise SyntaxError(b'invalid descendant')

    def select(context, result):
        for elem in result:
            for e in elem.iter(tag):
                if e is not elem:
                    yield e

        return

    return select


def prepare_parent(next, token):

    def select(context, result):
        parent_map = get_parent_map(context)
        result_map = {}
        for elem in result:
            if elem in parent_map:
                parent = parent_map[elem]
                if parent not in result_map:
                    result_map[parent] = None
                    yield parent

        return

    return select


def prepare_predicate(next, token):
    signature = []
    predicate = []
    while 1:
        token = next()
        if token[0] == b']':
            break
        if token[0] and token[0][:1] in b'\'"':
            token = (
             b"'", token[0][1:-1])
        signature.append(token[0] or b'-')
        predicate.append(token[1])

    signature = (b'').join(signature)
    if signature == b'@-':
        key = predicate[1]

        def select(context, result):
            for elem in result:
                if elem.get(key) is not None:
                    yield elem

            return

        return select
    if signature == b"@-='":
        key = predicate[1]
        value = predicate[-1]

        def select(context, result):
            for elem in result:
                if elem.get(key) == value:
                    yield elem

            return

        return select
    if signature == b'-' and not re.match(b'\\d+$', predicate[0]):
        tag = predicate[0]

        def select(context, result):
            for elem in result:
                if elem.find(tag) is not None:
                    yield elem

            return

        return select
    if signature == b"-='" and not re.match(b'\\d+$', predicate[0]):
        tag = predicate[0]
        value = predicate[-1]

        def select(context, result):
            for elem in result:
                for e in elem.findall(tag):
                    if (b'').join(e.itertext()) == value:
                        yield elem
                        break

            return

        return select
    if signature == b'-' or signature == b'-()' or signature == b'-()-':
        if signature == b'-':
            index = int(predicate[0]) - 1
        elif predicate[0] != b'last':
            raise SyntaxError(b'unsupported function')
        if signature == b'-()-':
            try:
                index = int(predicate[2]) - 1
            except ValueError:
                raise SyntaxError(b'unsupported expression')

        else:
            index = -1

        def select(context, result):
            parent_map = get_parent_map(context)
            for elem in result:
                try:
                    parent = parent_map[elem]
                    elems = list(parent.findall(elem.tag))
                    if elems[index] is elem:
                        yield elem
                except (IndexError, KeyError):
                    pass

            return

        return select
    raise SyntaxError(b'invalid predicate')
    return


ops = {b'': prepare_child, 
   b'*': prepare_star, 
   b'.': prepare_self, 
   b'..': prepare_parent, 
   b'//': prepare_descendant, 
   b'[': prepare_predicate}
_cache = {}

class _SelectorContext:
    parent_map = None

    def __init__(self, root):
        self.root = root
        return


def iterfind(elem, path, namespaces=None):
    if path[-1:] == b'/':
        path = path + b'*'
    try:
        selector = _cache[path]
    except KeyError:
        if len(_cache) > 100:
            _cache.clear()
        if path[:1] == b'/':
            raise SyntaxError(b'cannot use absolute path on element')
        next = iter(xpath_tokenizer(path, namespaces)).next
        token = next()
        selector = []
        while 1:
            try:
                selector.append(ops[token[0]](next, token))
            except StopIteration:
                raise SyntaxError(b'invalid path')

            try:
                token = next()
                if token[0] == b'/':
                    token = next()
            except StopIteration:
                break

        _cache[path] = selector

    result = [elem]
    context = _SelectorContext(elem)
    for select in selector:
        result = select(context, result)

    return result


def find(elem, path, namespaces=None):
    try:
        return iterfind(elem, path, namespaces).next()
    except StopIteration:
        return

    return


def findall(elem, path, namespaces=None):
    return list(iterfind(elem, path, namespaces))


def findtext(elem, path, default=None, namespaces=None):
    try:
        elem = iterfind(elem, path, namespaces).next()
        return elem.text or b''
    except StopIteration:
        return default

    return
