from .. import fixer_base
from ..fixer_util import Name

class FixRawInput(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = b"\n              power< name='raw_input' trailer< '(' [any] ')' > any* >\n              "

    def transform(self, node, results):
        name = results[b'name']
        name.replace(Name(u'input', prefix=name.prefix))
        return
