from .. import pytree
from .. import fixer_base
from ..fixer_util import Comma, Name, Call

class FixExec(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = b"\n    exec_stmt< 'exec' a=any 'in' b=any [',' c=any] >\n    |\n    exec_stmt< 'exec' (not atom<'(' [any] ')'>) a=any >\n    "

    def transform(self, node, results):
        syms = self.syms
        a = results[b'a']
        b = results.get(b'b')
        c = results.get(b'c')
        args = [a.clone()]
        args[0].prefix = b''
        if b is not None:
            args.extend([Comma(), b.clone()])
        if c is not None:
            args.extend([Comma(), c.clone()])
        return Call(Name(u'exec'), args, prefix=node.prefix)
