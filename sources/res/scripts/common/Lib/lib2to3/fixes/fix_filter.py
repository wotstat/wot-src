from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, ListComp, in_special_context

class FixFilter(fixer_base.ConditionalFix):
    BM_compatible = True
    PATTERN = b"\n    filter_lambda=power<\n        'filter'\n        trailer<\n            '('\n            arglist<\n                lambdef< 'lambda'\n                         (fp=NAME | vfpdef< '(' fp=NAME ')'> ) ':' xp=any\n                >\n                ','\n                it=any\n            >\n            ')'\n        >\n    >\n    |\n    power<\n        'filter'\n        trailer< '(' arglist< none='None' ',' seq=any > ')' >\n    >\n    |\n    power<\n        'filter'\n        args=trailer< '(' [any] ')' >\n    >\n    "
    skip_on = b'future_builtins.filter'

    def transform(self, node, results):
        if self.should_skip(node):
            return None
        else:
            if b'filter_lambda' in results:
                new = ListComp(results.get(b'fp').clone(), results.get(b'fp').clone(), results.get(b'it').clone(), results.get(b'xp').clone())
            elif b'none' in results:
                new = ListComp(Name(u'_f'), Name(u'_f'), results[b'seq'].clone(), Name(u'_f'))
            elif in_special_context(node):
                return None
            new = node.clone()
            new.prefix = u''
            new = Call(Name(u'list'), [new])
            new.prefix = node.prefix
            return new
