from .. import pytree
from .. import fixer_base
from ..fixer_util import Name, Attr, touch_import

class FixIntern(fixer_base.BaseFix):
    BM_compatible = True
    order = b'pre'
    PATTERN = b"\n    power< 'intern'\n           trailer< lpar='('\n                    ( not(arglist | argument<any '=' any>) obj=any\n                      | obj=arglist<(not argument<any '=' any>) any ','> )\n                    rpar=')' >\n           after=any*\n    >\n    "

    def transform(self, node, results):
        if results:
            obj = results[b'obj']
            if obj:
                if obj.type == self.syms.star_expr:
                    return
                if obj.type == self.syms.argument and obj.children[0].value == b'**':
                    return
        syms = self.syms
        obj = results[b'obj'].clone()
        if obj.type == syms.arglist:
            newarglist = obj.clone()
        else:
            newarglist = pytree.Node(syms.arglist, [obj.clone()])
        after = results[b'after']
        if after:
            after = [n.clone() for n in after]
        new = pytree.Node(syms.power, Attr(Name(u'sys'), Name(u'intern')) + [pytree.Node(syms.trailer, [results[b'lpar'].clone(), newarglist, results[b'rpar'].clone()])] + after)
        new.prefix = node.prefix
        touch_import(None, u'sys', node)
        return new
