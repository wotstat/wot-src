from .. import pytree
from .. import patcomp
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, LParen, RParen, ArgList, Dot
from .. import fixer_util
iter_exempt = fixer_util.consuming_calls | set([b'iter'])

class FixDict(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = b"\n    power< head=any+\n         trailer< '.' method=('keys'|'items'|'values'|\n                              'iterkeys'|'iteritems'|'itervalues'|\n                              'viewkeys'|'viewitems'|'viewvalues') >\n         parens=trailer< '(' ')' >\n         tail=any*\n    >\n    "

    def transform(self, node, results):
        head = results[b'head']
        method = results[b'method'][0]
        tail = results[b'tail']
        syms = self.syms
        method_name = method.value
        isiter = method_name.startswith(u'iter')
        isview = method_name.startswith(u'view')
        if isiter or isview:
            method_name = method_name[4:]
        head = [n.clone() for n in head]
        tail = [n.clone() for n in tail]
        special = not tail and self.in_special_context(node, isiter)
        args = head + [
         pytree.Node(syms.trailer, [
          Dot(),
          Name(method_name, prefix=method.prefix)]),
         results[b'parens'].clone()]
        new = pytree.Node(syms.power, args)
        if not (special or isview):
            new.prefix = u''
            new = Call(Name(u'iter' if isiter else u'list'), [new])
        if tail:
            new = pytree.Node(syms.power, [new] + tail)
        new.prefix = node.prefix
        return new

    P1 = b"power< func=NAME trailer< '(' node=any ')' > any* >"
    p1 = patcomp.compile_pattern(P1)
    P2 = b"for_stmt< 'for' any 'in' node=any ':' any* >\n            | comp_for< 'for' any 'in' node=any any* >\n         "
    p2 = patcomp.compile_pattern(P2)

    def in_special_context(self, node, isiter):
        if node.parent is None:
            return False
        else:
            results = {}
            if node.parent.parent is not None and self.p1.match(node.parent.parent, results):
                if results[b'node'] is node:
                    if isiter:
                        return results[b'func'].value in iter_exempt
                    return results[b'func'].value in fixer_util.consuming_calls
            if not isiter:
                return False
            return self.p2.match(node.parent, results) and results[b'node'] is node
