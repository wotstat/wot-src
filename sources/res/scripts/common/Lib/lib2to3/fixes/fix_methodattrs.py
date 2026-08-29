from .. import fixer_base
from ..fixer_util import Name
MAP = {b'im_func': b'__func__', 
   b'im_self': b'__self__', 
   b'im_class': b'__self__.__class__'}

class FixMethodattrs(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = b"\n    power< any+ trailer< '.' attr=('im_func' | 'im_self' | 'im_class') > any* >\n    "

    def transform(self, node, results):
        attr = results[b'attr'][0]
        new = unicode(MAP[attr.value])
        attr.replace(Name(new, prefix=attr.prefix))
        return
