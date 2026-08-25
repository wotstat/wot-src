from .. import fixer_base
from ..fixer_util import Name, Call, consuming_calls
from .. import patcomp

class FixXrange(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = b"\n              power<\n                 (name='range'|name='xrange') trailer< '(' args=any ')' >\n              rest=any* >\n              "

    def start_tree(self, tree, filename):
        super(FixXrange, self).start_tree(tree, filename)
        self.transformed_xranges = set()
        return

    def finish_tree(self, tree, filename):
        self.transformed_xranges = None
        return

    def transform(self, node, results):
        name = results[b'name']
        if name.value == u'xrange':
            return self.transform_xrange(node, results)
        if name.value == u'range':
            return self.transform_range(node, results)
        raise ValueError(repr(name))
        return

    def transform_xrange(self, node, results):
        name = results[b'name']
        name.replace(Name(u'range', prefix=name.prefix))
        self.transformed_xranges.add(id(node))
        return

    def transform_range(self, node, results):
        if id(node) not in self.transformed_xranges and not self.in_special_context(node):
            range_call = Call(Name(u'range'), [results[b'args'].clone()])
            list_call = Call(Name(u'list'), [range_call], prefix=node.prefix)
            for n in results[b'rest']:
                list_call.append_child(n)

            return list_call
        return

    P1 = b"power< func=NAME trailer< '(' node=any ')' > any* >"
    p1 = patcomp.compile_pattern(P1)
    P2 = b"for_stmt< 'for' any 'in' node=any ':' any* >\n            | comp_for< 'for' any 'in' node=any any* >\n            | comparison< any 'in' node=any any*>\n         "
    p2 = patcomp.compile_pattern(P2)

    def in_special_context(self, node):
        if node.parent is None:
            return False
        else:
            results = {}
            if node.parent.parent is not None and self.p1.match(node.parent.parent, results) and results[b'node'] is node:
                return results[b'func'].value in consuming_calls
            return self.p2.match(node.parent, results) and results[b'node'] is node
