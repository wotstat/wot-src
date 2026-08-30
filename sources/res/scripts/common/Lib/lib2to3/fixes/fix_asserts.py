from ..fixer_base import BaseFix
from ..fixer_util import Name
NAMES = dict(assert_=b'assertTrue', assertEquals=b'assertEqual', assertNotEquals=b'assertNotEqual', assertAlmostEquals=b'assertAlmostEqual', assertNotAlmostEquals=b'assertNotAlmostEqual', assertRegexpMatches=b'assertRegex', assertRaisesRegexp=b'assertRaisesRegex', failUnlessEqual=b'assertEqual', failIfEqual=b'assertNotEqual', failUnlessAlmostEqual=b'assertAlmostEqual', failIfAlmostEqual=b'assertNotAlmostEqual', failUnless=b'assertTrue', failUnlessRaises=b'assertRaises', failIf=b'assertFalse')

class FixAsserts(BaseFix):
    PATTERN = b"\n              power< any+ trailer< '.' meth=(%s)> any* >\n              " % (b'|').join(map(repr, NAMES))

    def transform(self, node, results):
        name = results[b'meth'][0]
        name.replace(Name(NAMES[str(name)], prefix=name.prefix))
        return
