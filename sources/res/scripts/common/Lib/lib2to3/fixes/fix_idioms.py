from .. import fixer_base
from ..fixer_util import Call, Comma, Name, Node, BlankLine, syms
CMP = b"(n='!=' | '==' | 'is' | n=comp_op< 'is' 'not' >)"
TYPE = b"power< 'type' trailer< '(' x=any ')' > >"

class FixIdioms(fixer_base.BaseFix):
    explicit = True
    PATTERN = b"\n        isinstance=comparison< %s %s T=any >\n        |\n        isinstance=comparison< T=any %s %s >\n        |\n        while_stmt< 'while' while='1' ':' any+ >\n        |\n        sorted=any<\n            any*\n            simple_stmt<\n              expr_stmt< id1=any '='\n                         power< list='list' trailer< '(' (not arglist<any+>) any ')' > >\n              >\n              '\\n'\n            >\n            sort=\n            simple_stmt<\n              power< id2=any\n                     trailer< '.' 'sort' > trailer< '(' ')' >\n              >\n              '\\n'\n            >\n            next=any*\n        >\n        |\n        sorted=any<\n            any*\n            simple_stmt< expr_stmt< id1=any '=' expr=any > '\\n' >\n            sort=\n            simple_stmt<\n              power< id2=any\n                     trailer< '.' 'sort' > trailer< '(' ')' >\n              >\n              '\\n'\n            >\n            next=any*\n        >\n    " % (TYPE, CMP, CMP, TYPE)

    def match(self, node):
        r = super(FixIdioms, self).match(node)
        if r and b'sorted' in r:
            if r[b'id1'] == r[b'id2']:
                return r
            return None
        return r

    def transform(self, node, results):
        if b'isinstance' in results:
            return self.transform_isinstance(node, results)
        if b'while' in results:
            return self.transform_while(node, results)
        if b'sorted' in results:
            return self.transform_sort(node, results)
        raise RuntimeError(b'Invalid match')
        return

    def transform_isinstance(self, node, results):
        x = results[b'x'].clone()
        T = results[b'T'].clone()
        x.prefix = u''
        T.prefix = u' '
        test = Call(Name(u'isinstance'), [x, Comma(), T])
        if b'n' in results:
            test.prefix = u' '
            test = Node(syms.not_test, [Name(u'not'), test])
        test.prefix = node.prefix
        return test

    def transform_while(self, node, results):
        one = results[b'while']
        one.replace(Name(u'True', prefix=one.prefix))
        return

    def transform_sort(self, node, results):
        sort_stmt = results[b'sort']
        next_stmt = results[b'next']
        list_call = results.get(b'list')
        simple_expr = results.get(b'expr')
        if list_call:
            list_call.replace(Name(u'sorted', prefix=list_call.prefix))
        elif simple_expr:
            new = simple_expr.clone()
            new.prefix = u''
            simple_expr.replace(Call(Name(u'sorted'), [new], prefix=simple_expr.prefix))
        else:
            raise RuntimeError(b'should not have reached here')
        sort_stmt.remove()
        btwn = sort_stmt.prefix
        if u'\n' in btwn:
            if next_stmt:
                prefix_lines = (
                 btwn.rpartition(u'\n')[0], next_stmt[0].prefix)
                next_stmt[0].prefix = (u'\n').join(prefix_lines)
            else:
                end_line = BlankLine()
                list_call.parent.append_child(end_line)
                end_line.prefix = btwn.rpartition(u'\n')[0]
        return
