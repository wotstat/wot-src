from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name
_TYPE_MAPPING = {b'BooleanType': b'bool', 
   b'BufferType': b'memoryview', 
   b'ClassType': b'type', 
   b'ComplexType': b'complex', 
   b'DictType': b'dict', 
   b'DictionaryType': b'dict', 
   b'EllipsisType': b'type(Ellipsis)', 
   b'FloatType': b'float', 
   b'IntType': b'int', 
   b'ListType': b'list', 
   b'LongType': b'int', 
   b'ObjectType': b'object', 
   b'NoneType': b'type(None)', 
   b'NotImplementedType': b'type(NotImplemented)', 
   b'SliceType': b'slice', 
   b'StringType': b'bytes', 
   b'StringTypes': b'(str,)', 
   b'TupleType': b'tuple', 
   b'TypeType': b'type', 
   b'UnicodeType': b'str', 
   b'XRangeType': b'range'}
_pats = [b"power< 'types' trailer< '.' name='%s' > >" % t for t in _TYPE_MAPPING]

class FixTypes(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = (b'|').join(_pats)

    def transform(self, node, results):
        new_value = unicode(_TYPE_MAPPING.get(results[b'name'].value))
        if new_value:
            return Name(new_value, prefix=node.prefix)
        else:
            return
