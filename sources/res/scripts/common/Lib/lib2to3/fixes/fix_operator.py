from lib2to3 import fixer_base
from lib2to3.fixer_util import Call, Name, String, touch_import

def invocation(s):

    def dec(f):
        f.invocation = s
        return f

    return dec


class FixOperator(fixer_base.BaseFix):
    BM_compatible = True
    order = b'pre'
    methods = b"\n              method=('isCallable'|'sequenceIncludes'\n                     |'isSequenceType'|'isMappingType'|'isNumberType'\n                     |'repeat'|'irepeat')\n              "
    obj = b"'(' obj=any ')'"
    PATTERN = b"\n              power< module='operator'\n                trailer< '.' %(methods)s > trailer< %(obj)s > >\n              |\n              power< %(methods)s trailer< %(obj)s > >\n              " % dict(methods=methods, obj=obj)

    def transform(self, node, results):
        method = self._check_method(node, results)
        if method is not None:
            return method(node, results)
        else:
            return

    @invocation(b'operator.contains(%s)')
    def _sequenceIncludes(self, node, results):
        return self._handle_rename(node, results, u'contains')

    @invocation(b"hasattr(%s, '__call__')")
    def _isCallable(self, node, results):
        obj = results[b'obj']
        args = [obj.clone(), String(u', '), String(u"'__call__'")]
        return Call(Name(u'hasattr'), args, prefix=node.prefix)

    @invocation(b'operator.mul(%s)')
    def _repeat(self, node, results):
        return self._handle_rename(node, results, u'mul')

    @invocation(b'operator.imul(%s)')
    def _irepeat(self, node, results):
        return self._handle_rename(node, results, u'imul')

    @invocation(b'isinstance(%s, collections.Sequence)')
    def _isSequenceType(self, node, results):
        return self._handle_type2abc(node, results, u'collections', u'Sequence')

    @invocation(b'isinstance(%s, collections.Mapping)')
    def _isMappingType(self, node, results):
        return self._handle_type2abc(node, results, u'collections', u'Mapping')

    @invocation(b'isinstance(%s, numbers.Number)')
    def _isNumberType(self, node, results):
        return self._handle_type2abc(node, results, u'numbers', u'Number')

    def _handle_rename(self, node, results, name):
        method = results[b'method'][0]
        method.value = name
        method.changed()
        return

    def _handle_type2abc(self, node, results, module, abc):
        touch_import(None, module, node)
        obj = results[b'obj']
        args = [obj.clone(), String(u', ' + (u'.').join([module, abc]))]
        return Call(Name(u'isinstance'), args, prefix=node.prefix)

    def _check_method(self, node, results):
        method = getattr(self, b'_' + results[b'method'][0].value.encode(b'ascii'))
        if callable(method):
            if b'module' in results:
                return method
            sub = (unicode(results[b'obj']),)
            invocation_str = unicode(method.invocation) % sub
            self.warning(node, u"You should use '%s' here." % invocation_str)
        return
