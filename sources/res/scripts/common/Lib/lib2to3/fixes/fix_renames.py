from .. import fixer_base
from ..fixer_util import Name, attr_chain
MAPPING = {b'sys': {b'maxint': b'maxsize'}}
LOOKUP = {}

def alternates(members):
    return b'(' + (b'|').join(map(repr, members)) + b')'


def build_pattern():
    for module, replace in MAPPING.items():
        for old_attr, new_attr in replace.items():
            LOOKUP[(module, old_attr)] = new_attr
            yield b"\n                  import_from< 'from' module_name=%r 'import'\n                      ( attr_name=%r | import_as_name< attr_name=%r 'as' any >) >\n                  " % (module, old_attr, old_attr)
            yield b"\n                  power< module_name=%r trailer< '.' attr_name=%r > any* >\n                  " % (module, old_attr)

    return


class FixRenames(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = (b'|').join(build_pattern())
    order = b'pre'

    def match(self, node):
        match = super(FixRenames, self).match
        results = match(node)
        if results:
            if any(match(obj) for obj in attr_chain(node, b'parent')):
                return False
            return results
        return False

    def transform(self, node, results):
        mod_name = results.get(b'module_name')
        attr_name = results.get(b'attr_name')
        if mod_name and attr_name:
            new_attr = unicode(LOOKUP[mod_name.value, attr_name.value])
            attr_name.replace(Name(new_attr, prefix=attr_name.prefix))
        return
