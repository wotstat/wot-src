from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, ListComp, in_special_context
from ..pygram import python_symbols as syms

class FixMap(fixer_base.ConditionalFix):
    BM_compatible = True
    PATTERN = b"\n    map_none=power<\n        'map'\n        trailer< '(' arglist< 'None' ',' arg=any [','] > ')' >\n    >\n    |\n    map_lambda=power<\n        'map'\n        trailer<\n            '('\n            arglist<\n                lambdef< 'lambda'\n                         (fp=NAME | vfpdef< '(' fp=NAME ')'> ) ':' xp=any\n                >\n                ','\n                it=any\n            >\n            ')'\n        >\n    >\n    |\n    power<\n        'map' trailer< '(' [arglist=any] ')' >\n    >\n    "
    skip_on = b'future_builtins.map'

    def transform(self, node, results):
        if self.should_skip(node):
            return None
        else:
            if node.parent.type == syms.simple_stmt:
                self.warning(node, b'You should use a for loop here')
                new = node.clone()
                new.prefix = u''
                new = Call(Name(u'list'), [new])
            elif b'map_lambda' in results:
                new = ListComp(results[b'xp'].clone(), results[b'fp'].clone(), results[b'it'].clone())
            else:
                if b'map_none' in results:
                    new = results[b'arg'].clone()
                elif b'arglist' in results:
                    args = results[b'arglist']
                    if args.type == syms.arglist and args.children[0].type == token.NAME and args.children[0].value == b'None':
                        self.warning(node, b'cannot convert map(None, ...) with multiple arguments because map() now truncates to the shortest sequence')
                        return None
                if in_special_context(node):
                    return None
                new = node.clone()
                new.prefix = u''
                new = Call(Name(u'list'), [new])
            new.prefix = node.prefix
            return new
