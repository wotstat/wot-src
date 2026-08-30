from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, ArgList, Attr, is_tuple

class FixThrow(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = b"\n    power< any trailer< '.' 'throw' >\n           trailer< '(' args=arglist< exc=any ',' val=any [',' tb=any] > ')' >\n    >\n    |\n    power< any trailer< '.' 'throw' > trailer< '(' exc=any ')' > >\n    "

    def transform(self, node, results):
        syms = self.syms
        exc = results[b'exc'].clone()
        if exc.type is token.STRING:
            self.cannot_convert(node, b'Python 3 does not support string exceptions')
            return
        else:
            val = results.get(u'val')
            if val is None:
                return
            val = val.clone()
            if is_tuple(val):
                args = [c.clone() for c in val.children[1:-1]]
            else:
                val.prefix = u''
                args = [val]
            throw_args = results[b'args']
            if b'tb' in results:
                tb = results[b'tb'].clone()
                tb.prefix = u''
                e = Call(exc, args)
                with_tb = Attr(e, Name(u'with_traceback')) + [ArgList([tb])]
                throw_args.replace(pytree.Node(syms.power, with_tb))
            else:
                throw_args.replace(Call(exc, args))
            return
