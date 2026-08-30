import re, distutils.version, operator
re_validPackage = re.compile(b'(?i)^\\s*([a-z_]\\w*(?:\\.[a-z_]\\w*)*)(.*)')
re_paren = re.compile(b'^\\s*\\((.*)\\)\\s*$')
re_splitComparison = re.compile(b'^\\s*(<=|>=|<|>|!=|==)\\s*([^\\s,]+)\\s*$')

def splitUp(pred):
    res = re_splitComparison.match(pred)
    if not res:
        raise ValueError(b'bad package restriction syntax: %r' % pred)
    comp, verStr = res.groups()
    return (comp, distutils.version.StrictVersion(verStr))


compmap = {b'<': (operator.lt), b'<=': (operator.le), b'==': (operator.eq), b'>': (operator.gt), 
   b'>=': (operator.ge), b'!=': (operator.ne)}

class VersionPredicate:

    def __init__(self, versionPredicateStr):
        versionPredicateStr = versionPredicateStr.strip()
        if not versionPredicateStr:
            raise ValueError(b'empty package restriction')
        match = re_validPackage.match(versionPredicateStr)
        if not match:
            raise ValueError(b'bad package name in %r' % versionPredicateStr)
        self.name, paren = match.groups()
        paren = paren.strip()
        if paren:
            match = re_paren.match(paren)
            if not match:
                raise ValueError(b'expected parenthesized list: %r' % paren)
            str = match.groups()[0]
            self.pred = [splitUp(aPred) for aPred in str.split(b',')]
            if not self.pred:
                raise ValueError(b'empty parenthesized list in %r' % versionPredicateStr)
        else:
            self.pred = []
        return

    def __str__(self):
        if self.pred:
            seq = [cond + b' ' + str(ver) for cond, ver in self.pred]
            return self.name + b' (' + (b', ').join(seq) + b')'
        else:
            return self.name

        return

    def satisfied_by(self, version):
        for cond, ver in self.pred:
            if not compmap[cond](version, ver):
                return False

        return True


_provision_rx = None

def split_provision(value):
    global _provision_rx
    if _provision_rx is None:
        _provision_rx = re.compile(b'([a-zA-Z_]\\w*(?:\\.[a-zA-Z_]\\w*)*)(?:\\s*\\(\\s*([^)\\s]+)\\s*\\))?$')
    value = value.strip()
    m = _provision_rx.match(value)
    if not m:
        raise ValueError(b'illegal provides specification: %r' % value)
    ver = m.group(2) or None
    if ver:
        ver = distutils.version.StrictVersion(ver)
    return (
     m.group(1), ver)
