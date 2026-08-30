from compiler import ast, walk

def is_future(stmt):
    if not isinstance(stmt, ast.From):
        return 0
    else:
        if stmt.modname == b'__future__':
            return 1
        return 0

    return


class FutureParser:
    features = (b'nested_scopes', b'generators', b'division', b'absolute_import', b'with_statement', b'print_function', b'unicode_literals')

    def __init__(self):
        self.found = {}
        return

    def visitModule(self, node):
        stmt = node.node
        for s in stmt.nodes:
            if not self.check_stmt(s):
                break

        return

    def check_stmt(self, stmt):
        if is_future(stmt):
            for name, asname in stmt.names:
                if name in self.features:
                    self.found[name] = 1
                else:
                    raise SyntaxError, b'future feature %s is not defined' % name

            stmt.valid_future = 1
            return 1
        return 0

    def get_features(self):
        return self.found.keys()


class BadFutureParser:

    def visitFrom(self, node):
        if hasattr(node, b'valid_future'):
            return
        if node.modname != b'__future__':
            return
        raise SyntaxError, b'invalid future statement ' + repr(node)
        return


def find_futures(node):
    p1 = FutureParser()
    p2 = BadFutureParser()
    walk(node, p1)
    walk(node, p2)
    return p1.get_features()


if __name__ == b'__main__':
    import sys
    from compiler import parseFile, walk
    for file in sys.argv[1:]:
        print file
        tree = parseFile(file)
        v = FutureParser()
        walk(tree, v)
        print v.found
        print
