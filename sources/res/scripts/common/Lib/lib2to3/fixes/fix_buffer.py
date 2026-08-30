from .. import fixer_base
from ..fixer_util import Name

class FixBuffer(fixer_base.BaseFix):
    BM_compatible = True
    explicit = True
    PATTERN = b"\n              power< name='buffer' trailer< '(' [any] ')' > any* >\n              "

    def transform(self, node, results):
        name = results[b'name']
        name.replace(Name(u'memoryview', prefix=name.prefix))
        return
